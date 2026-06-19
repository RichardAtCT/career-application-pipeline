# Automation

Do not automate until a manual search has been run and the user has reviewed the criteria.

## Strong-match monitor

Purpose: frequent, quiet, high-confidence alerts.

Suggested behavior:

- run on weekdays or user-selected cadence;
- load `cv/parsed-profile.yaml`, `cv/search-criteria.yaml`, `source-inventory.yaml`, and `tracker.csv`;
- search only configured sources;
- verify direct source URLs;
- append/update tracker;
- report only new verified roles above threshold, usually `>=85`;
- generate application packs for priority matches if the user approved that behavior;
- otherwise stay silent or send a no-match line, depending on user preference.

## Weekly digest

Purpose: broader review and tracker health.

Include strong matches, strategic maybes, applications awaiting review, follow-ups due, closed/stale roles, source coverage gaps, and suggested criteria adjustments.

## Portable scheduled prompt

```text
Use the Career Application Pipeline playbook.
Workspace: <absolute-or-runtime-accessible-path>

Tasks:
1. Load candidate profile, search criteria, source inventory, and tracker.
2. Search configured sources for new roles.
3. Verify direct job/source URLs.
4. Deduplicate by canonical URL and normalized company/title.
5. Score using the configured rubric.
6. Append/update tracker without overwriting statuses such as applied, archived, rejected, or interviewing.
7. Report only roles meeting the monitor threshold.

Safety:
- Do not submit applications.
- Do not send outreach.
- Do not fabricate salary, remote policy, contacts, or posting dates.
- Mark unknowns explicitly.
```
