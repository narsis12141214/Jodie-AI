# Contract Clause Revisions — For Replacement

**Date:** 12 May 2026
**Status:** Proposed rewrites for three contract clauses identified in the Strategist diagnostic
**Owner:** Hadi
**Applies to:** All new agency contracts generated after this date. Existing signed contracts (Haleh Cake) are unaffected.

These rewrites address structural friction in the current contract language that may be contributing to buyer cooling between verbal yes and signature. Each clause is shown old vs new for direct replacement in the contract generator script.

---

## REVISION 1 — Section 3.2 (Monthly Service Fee, sub-clauses a and b)

### Why
The phrase "24 months of this Agreement" reads as a 24-month commitment. The contract is monthly rolling per Section 5.1, but the loyalty discount language muddies that. An anxious owner reading this at home sees the words "24 months" and feels locked in.

### Current language
> a) The 10% loyalty discount applies for the duration of the first 24 months of this Agreement
>
> b) After 24 months, the monthly fee will be reviewed. The Service Provider will provide 30 days written notice of any pricing changes.

### Replacement language
> a) The 10% loyalty discount applies for the first 24 months of continuous service under this Agreement. This Agreement remains monthly rolling at all times per Section 5.1, and nothing in this clause creates a minimum contract term or commitment.
>
> b) After 24 months of continuous service, the Service Provider may review the standard monthly fee. Any change to the standard fee will be communicated to the Client with at least 30 days written notice in advance. If the new fee is not acceptable to the Client, the Client retains the right to terminate this Agreement under Section 5.2 without penalty.

### Schedule A line item — also update

Current: "Loyalty discount term: 24 months, then review with 30 days notice"

Replacement: "Loyalty discount duration: 24 months of continuous service. No minimum contract term. Monthly rolling per Section 5.1."

---

## REVISION 2 — Section 2.5 (Case Study Permission)

### Why
The current clause grants broad permissions with approval and withdrawal rights mentioned but not strongly framed. For a case-study tier client, this is the clause that may scare them at the kitchen table. Strengthening the client's rights of approval, withdrawal, and confidentiality protection removes a perceived risk without weakening our right to use the case study.

### Current language
> In consideration of the waived setup fee (see Section 3.1), the Client grants the Service Provider permission to:
>
> a) Use the Client's business name, logo, and a description of the services delivered as a case study on the Service Provider's website, social media, and marketing materials
>
> b) Reference the Client's business in proposals, presentations, and sales conversations with prospective clients
>
> c) Share anonymised performance metrics (e.g., calls answered, engagement growth) as part of the case study
>
> The Service Provider will share the case study content with the Client for approval before publishing. The Client may request removal of the case study at any time by providing written notice.

### Replacement language
> In consideration of the waived setup fee (see Section 3.1), the Client grants the Service Provider permission to feature the Client as a case study, subject to the following terms:
>
> **a) Use Permission.** The Service Provider may use the Client's business name, logo, a description of the services delivered, and anonymised performance metrics (for example: calls answered, response times, engagement growth) as a case study on the Service Provider's website, social media, marketing materials, proposals, presentations, and sales conversations with prospective clients.
>
> **b) Client Approval Before Publication.** The Service Provider will share all case study content with the Client in writing before any public publication. The Client has 10 business days to approve, request changes, or reject the content. No case study content will be published without the Client's written approval.
>
> **c) Right to Withdraw.** The Client may withdraw permission for any or all case study content at any time, for any reason, by providing 30 days written notice to the Service Provider. On receipt of such notice, the Service Provider will remove the relevant content from all public-facing channels within 30 days and will not use the Client's name or assets in future marketing.
>
> **d) No Confidential Information.** The Service Provider will not disclose customer data, financial information, pricing arrangements, or any information designated by the Client as confidential in any case study material.

---

## REVISION 3 — Section 4 (Trial Period)

### Why
The current clause hides the critical trigger in the first sentence. "Beginning on the go-live date of the system" reads quickly and may not register. An owner reading this anxiously at 11pm may assume the trial starts from signature, which creates fear of being billed before the system is even built. Making the trigger explicit and impossible to miss removes that fear.

### Current language
> The Client is entitled to a 7-day trial period beginning on the go-live date of the system. During this period:
>
> a) The Client may use all services as described in Section 2
>
> b) No monthly fee is charged during the trial period
>
> c) If the Client wishes to cancel during the trial period, they must notify the Service Provider in writing before the trial expires
>
> d) If the Client cancels during the trial period, no monthly fees will be charged
>
> e) If the Client does not cancel during the trial period, monthly billing begins automatically on the day following the trial expiry

### Replacement language
> **4.1 Trial Period and Start Date.** The Client is entitled to a 7-day trial period. **The trial period begins on the go-live date of the system, which is the date the Service Provider activates the AI voice agent, WhatsApp automation, and social media management on the Client's behalf. The trial period does NOT begin on the date of signature.**
>
> **4.2 Go-Live Confirmation.** The Service Provider will confirm the go-live date in writing to the Client at least 24 hours before activation. The Client will receive a written notification on the day of go-live confirming that Trial Day 1 has started.
>
> **4.3 During the Trial.** During the 7-day trial period:
>
> a) The Client may use all services as described in Section 2
>
> b) No monthly fee is charged
>
> c) The Client may cancel at any point during the trial by providing written notice to the Service Provider before the trial expires
>
> d) If the Client cancels during the trial, no monthly fees will be charged and the Service Provider will deactivate the system at the end of the trial period
>
> **4.4 End of Trial.** If the Client does not cancel during the trial period, monthly billing begins automatically on the day following the trial expiry. The Service Provider will issue the Month 1 invoice on that date, payable within 7 days per Section 3.2(f).

---

## Implementation

These clause revisions only take effect when applied to the contract generator script. The script for Haleh Cake is at:

`projects/agency/28-04-26/generate-haleh-cake-contract.py`

The script for Kish is at:

`projects/agency/09-05-26/generate-kish-agreement.py`

**Recommended next step:** Build a single canonical contract generator that accepts client name, package tier, and case-study flag as variables. Replace the per-client Python scripts with one master template. This removes the risk of clauses drifting across clients and makes future revisions a one-file change.

Until that refactor happens, every new client contract script must use the language from this file. Do not copy old scripts forward without updating these three clauses first.

## What is NOT changing

- Section 5 (Term and Termination): the monthly rolling, 30-day notice structure is correct and serves both parties well
- Section 6 (Intellectual Property): clear and balanced as written
- Section 8 (Data Protection and GDPR): legally required language, no change needed
- Section 9 (Liability): standard limitation, no change needed
- Schedule A overage rates: appropriate, no change needed

## Quality check before adopting

Before adopting these rewrites into the contract generator script, run them past a UK contracts solicitor for a 30-minute legal review. The plain-language rewrites are designed to read more naturally to a small business owner. We need to confirm they do not weaken our legal position. Budget: £200 to £400 for the review. Worth it before this goes onto 10 more contracts.

If a solicitor review is not possible this week, adopt as is and review retroactively. The current clauses already exist in 4 sent contracts without legal review, so we are not increasing risk by deploying these now.
