# Workflow 1 Update Log — 9 April 2026

## Status
LIVE. Running daily Mon-Fri at 8am.
Expected output: 70-100 qualified leads per day across Restaurant/Cafe, Beauty/Aesthetics, and Dental.

---

## Changes Made

### Bug Fixes
- **Get Existing Leads node**: header row corrected from 1 to 3. Root cause of duplicate leads appearing 3-4 times in the tracker.
- **Wait 1 Minutes node** (between Start Profile Scraper and Fetch Profile Results): was disabled, re-enabled so Apify has time to complete before results are fetched.
- **Append to Lead Sheet matching column**: switched from Map Each Column Manually to Map Automatically. Resolves schema sync error caused by new columns (Second Message, business_name) added by Workflow 2.

### New Node
- **Filter by Follower Count**: inserted between Merge Profile Data and Get Existing Leads. Filters out any account outside the target follower range before writing to the tracker.

### Hashtags Expanded
- From 5 to 28 hashtags across three industries:
  - Restaurants: 11 hashtags
  - Aesthetics: 9 hashtags
  - Dental: 8 hashtags
- resultsLimit increased from 30 to 100 per hashtag
- Fetch limit increased from 200 to 3,000

### Profile Scraper
- slice increased from 20 to 100. Now enriches up to 100 accounts per run instead of 20.

### Industry Detection
- Dental added as new industry type
- Keywords: dentist, dental, teeth, orthodont, invisalign, tooth

### Follower Range
- Updated from 500-5,000 to 1,000-20,000
