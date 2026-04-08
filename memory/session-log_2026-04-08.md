# Session Log — 8 April 2026

## Workflow 2 (Opener Generation) — Fixes Applied

### Problems identified and fixed

**401 error on Generate Opener node**
- Cause: Claude API credential had expired
- Fix: Re-entered API key in N8N credentials
- Status: Resolved

**Opener writing to wrong column**
- Cause (two-part): opener and generated_at columns did not exist in the sheet when workflow first ran, so Map Automatically appended data positionally
- Fix 1: Added opener and generated_at as explicit column headers in the Outreach Tracker
- Fix 2: Set Header Row to 3 and First Data Row to 4 in Update Lead Row node to match Read Lead Sheet node

**Same 20 leads processed every run**
- Cause: Status was not being written back to the sheet — Filter New Leads kept picking up the same rows
- Fix: Added `status: 'Opener Generated'` to the output.push object in Generate Opener node

**Filter New Leads returning no output**
- Cause: Filter was checking both `Status === 'New Lead'` AND `Message Sent === ''` — too strict
- Fix: Simplified to status check only. Also updated field reference to handle both `status` and `Status` casing

**Email to Zizi missing business names**
- Cause: business_name was removed from output object during debugging
- Fix: Added back. Does not affect sheet mapping (no matching column header) but required for email summary

### Current output.push object (Generate Opener node)

```javascript
output.push({
  json: {
    row_number: lead['row_number'],
    business_name: businessName,
    status: 'Opener Generated',
    opener: opener,
    generated_at: new Date().toISOString().split('T')[0]
  }
});
```

### Workflow status
LIVE and working correctly as of 8 April 2026.
