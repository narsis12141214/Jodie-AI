# Arman Dev Brief — Performance Anchor Feature (Click Desk AI)

Copy everything below the divider and send to Arman.

---

## Feature: Performance Anchor Measurement

### Why we're building this

We're using a performance guarantee in our sales pitch:

> "If we don't capture at least 10 new bookings during hours your phone wouldn't otherwise be answered in Month 1, you get the month refunded."

For this to work, Click Desk needs to (a) know each tenant's reception hours, (b) classify every incoming call as either "recovered" or "normal," and (c) display the recovery numbers on the client's overview dashboard so they can see the value in real time.

This is the v0.5 build. No Stripe automation for refunds — refunds are manual for now. Build the measurement and reporting layer only.

---

## 1. Data model changes

### 1a. New table: `tenant_reception_hours`

Per-tenant config for when a human staff member is normally available to answer the phone. One row per weekday per tenant. Multiple time windows per day allowed (e.g. restaurant with split shift).

```
tenant_reception_hours
- id (uuid, pk)
- tenant_id (uuid, fk → tenants)
- day_of_week (int 0–6, where 0 = Monday)
- open_time (time, tenant local time)
- close_time (time, tenant local time)
- created_at, updated_at
```

Notes:
- Tenant timezone lives on the `tenants` table — add `timezone` column there if it doesn't exist (default `Europe/London`).
- Multiple rows per (tenant_id, day_of_week) are valid (split shift).
- A day with zero rows = closed all day (everything that day is "outside reception hours").

### 1b. New columns on `calls` table

```
- routing_classification (enum: 'outside_hours' | 'human_no_answer' | 'human_answered' | 'other')
- classification_reason (text, nullable — for debug/audit)
- human_answer_attempted_at (timestamp, nullable)
- human_answer_elapsed_seconds (int, nullable)
```

If the `calls` table doesn't exist yet, create it with at minimum: `id, tenant_id, twilio_call_sid, started_at, ended_at, from_number, to_number, duration_seconds, outcome, plus the four above`.

### 1c. New columns on `bookings` table

```
- source_call_id (uuid, nullable, fk → calls.id)
- is_recovered (boolean, default false)
- recovery_reason (enum: 'outside_hours' | 'human_no_answer' | null)
```

A booking is "recovered" when it was made by the AI voice agent AND the originating call was classified as either `outside_hours` or `human_no_answer`. This is the **inclusive** definition.

---

## 2. Backend logic

### 2a. Call classification (runs on every inbound call)

When Twilio sends a webhook for an inbound call to a tenant's number, classify it before or alongside routing:

1. **Check reception hours** for that tenant in their timezone, for `started_at`.
   - If the call time falls **outside** all configured reception-hour windows for that day → `routing_classification = 'outside_hours'`. Route the call straight to the AI agent. Done.

2. **Inside reception hours** → attempt human transfer. Start a 12-second timer (= ~4 rings on a mobile, verified by real test).
   - If a human answers within 12 seconds → `routing_classification = 'human_answered'`. Set `human_answer_attempted_at` and `human_answer_elapsed_seconds`.
   - If 12 seconds elapse with no human answer → `routing_classification = 'human_no_answer'`. Hand off to the AI agent. Set `human_answer_attempted_at` to the start of the attempt and `human_answer_elapsed_seconds = 12`.

3. Anything that doesn't fit (test calls, system errors, voicemail-only, etc.) → `routing_classification = 'other'`. Log `classification_reason`.

The 12-second threshold is configurable per-tenant. For v0.5 hard-code it as a constant (`HUMAN_ANSWER_TIMEOUT_SECONDS = 12`, expressed in seconds) so we can change it in one place. Acceptable per-tenant override range is 10-20 seconds — values outside this should be rejected by the admin UI.

### 2b. Booking attribution

When the AI agent creates a booking, link the booking to the originating call via `source_call_id`.

Then:
- If `source_call_id.routing_classification IN ('outside_hours', 'human_no_answer')` → `is_recovered = true` and `recovery_reason` = the classification.
- Otherwise → `is_recovered = false`.

This logic runs at booking-creation time, not later. We don't want to recompute historical bookings every time reception hours change — the classification at the moment of the call is the source of truth.

### 2c. Reception-hours admin API

Endpoints needed for the internal admin (Hadi/team) to configure per-tenant reception hours during onboarding:

```
GET    /admin/tenants/:tenant_id/reception-hours
POST   /admin/tenants/:tenant_id/reception-hours
PATCH  /admin/tenants/:tenant_id/reception-hours/:id
DELETE /admin/tenants/:tenant_id/reception-hours/:id
```

These must be gated to admin role only. Clients cannot hit these endpoints.

### 2d. Reception-hours read API (for client dashboard)

```
GET /api/tenant/reception-hours
```

Returns the current tenant's hours. Read-only. No write endpoint exposed to clients in v0.5.

---

## 3. Dashboard UI

### 3a. Overview page — add two new cards

The overview page currently shows two KPI cards: **Total Bookings** and **Bookings Made**. Add two more, side by side, for a 2×2 or 1×4 grid (your call on layout):

1. **Recovered Reservations** (or "Recovered Bookings" — match the tenant's terminology if we have a config flag for it; otherwise default to "Recovered Bookings")
   - Count of bookings where `is_recovered = true`
   - Same date-range filter as the other cards on the page
   - Tooltip / info icon: "Bookings the AI captured that would otherwise have been missed — either outside your reception hours or when no one answered within 60 seconds."

2. **Busy Hour Bookings**
   - Count of bookings where `is_recovered = true AND recovery_reason = 'human_no_answer'`
   - This is the subset that came in during reception hours but no human picked up — i.e. the team was too busy to answer.
   - Tooltip: "Bookings the AI captured during your open hours when your team couldn't answer within 60 seconds."

Note that "Recovered Reservations" is the parent metric; "Busy Hour Bookings" is a subset of it. The other subset (outside hours) is just `Recovered − Busy Hour`. We could add a third card for "After Hours Bookings" later but Hadi wants the two above for v0.5.

### 3b. Reception hours read-only display

On the tenant's settings page (or wherever the existing tenant profile lives), display the configured reception hours as a read-only table:

```
Monday    09:00 – 18:00
Tuesday   09:00 – 18:00
...
Sunday    Closed
```

No edit button for v0.5. Add a small note: "To update your reception hours, contact your Click AI account manager." Hadi/team manages this via the admin API.

---

## 4. Multi-tenant isolation (non-negotiable)

- Every query on `tenant_reception_hours`, `calls`, and `bookings` must filter by `tenant_id` derived from the authenticated session.
- No endpoint may accept a `tenant_id` query parameter from a client user — always read it from the auth context.
- The admin endpoints in §2c are the only place where `tenant_id` is taken as a URL parameter, and those are admin-role gated.
- Verify with at least two tenant accounts in your test environment that tenant A cannot see tenant B's calls, bookings, or reception hours under any endpoint.

---

## 5. Acceptance criteria

The feature is done when all of the following are true:

1. I (Hadi) can log into the admin panel, pick a tenant, and add/edit/delete that tenant's reception hours.
2. A call arriving outside the configured reception hours is logged with `routing_classification = 'outside_hours'` and routed to the AI agent.
3. A call arriving inside reception hours waits up to 12 seconds (~4 rings on mobile) for a human, then either marks `human_answered` (with elapsed seconds) or `human_no_answer` (at 12s exactly).
4. A booking created by the AI agent gets `is_recovered = true` and the correct `recovery_reason` when the source call was outside hours or human-no-answer.
5. The client dashboard overview page shows four KPI cards: Total Bookings, Bookings Made, Recovered Reservations, Busy Hour Bookings — and the numbers reconcile (Recovered ≥ Busy Hour, both ≤ Total).
6. The client's settings page shows reception hours as a read-only table.
7. Tenant A cannot access tenant B's data via any endpoint, including the admin endpoints when authenticated as a non-admin user.

---

## 6. Out of scope for v0.5

Do not build any of the following in this round:

- Stripe refund automation. Refunds are issued manually by Hadi if a tenant misses the 10-booking threshold in Month 1.
- Client self-serve editing of reception hours.
- Client-facing UI to adjust the human-answer timeout (admin-only configurability is enough for v0.5; clients cannot edit).
- Email/SMS alerts when the recovered count crosses a threshold.
- Historical re-classification of calls that happened before this feature ships.
- A "10 Recovered Bookings Progress" goal widget — we'll add this in v1 once we have a few weeks of real data.

---

## 7. Suggested build order

1. Migrations: add `timezone` to `tenants`, create `tenant_reception_hours`, add columns to `calls` and `bookings`.
2. Admin reception-hours CRUD endpoints.
3. Call classification logic in the Twilio webhook handler.
4. Booking attribution at booking-creation time.
5. Client read API for reception hours + the new dashboard cards.
6. Multi-tenant isolation tests.

---

If anything in this brief is unclear or you spot a gap, message Hadi before writing the code. Don't guess on the classification logic — it's the most important part of the feature.
