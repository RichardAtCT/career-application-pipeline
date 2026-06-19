# Roadmap

This roadmap is intentionally practical. The project should remain useful as a plain repository of files before it becomes a package or SaaS.

## Near-term polish

- [ ] Add more synthetic example CVs:
  - early-career data analyst;
  - senior engineering manager;
  - nonprofit/public-sector leader;
  - career switcher;
  - returning-to-work profile.
- [ ] Add sample completed workspaces generated from synthetic CVs.
- [ ] Add richer JSON schemas for tracker rows, role records, and application-pack provenance.
- [ ] Add Markdown examples of good vs weak CV bullet rewrites.
- [ ] Add example prompts for common agents while keeping the core playbook agent-agnostic.
- [ ] Add source-inventory examples for common ATS platforms and job boards.

## Workflow improvements

- [ ] Add a role record schema for staged/verified roles.
- [ ] Add a deterministic role ID helper script.
- [ ] Add a tracker migration/normalization script.
- [ ] Add optional application-pack generation script from a tracker row.
- [ ] Add validation for application-pack completeness.
- [ ] Add example scoring breakdowns.

## Agent integration examples

- [ ] Claude Code prompt example.
- [ ] OpenAI Codex prompt example.
- [ ] Cursor prompt example.
- [ ] ChatGPT Projects prompt example.
- [ ] Local LLM / OpenHands / Goose examples.

These should live in docs/examples and must not become core runtime dependencies.

## v1 goals

- [ ] End-to-end synthetic demo: sample CV → parsed profile → search criteria → tracker → application pack.
- [ ] Robust validation command covering schemas, workspace structure, and tracker headers.
- [ ] Clear privacy model and threat notes.
- [ ] Contribution-ready docs and issue templates.
- [ ] At least three fully synthetic example workflows.

## Maybe later

- [ ] Optional Python package / CLI wrapper.
- [ ] Optional PDF rendering helpers.
- [ ] Optional integrations with Google Drive, Notion, Airtable, or Sheets.
- [ ] Optional browser-assisted job-source adapters.
- [ ] Hosted documentation site.

## Non-goals

- Auto-submitting applications by default.
- Scraping private LinkedIn data.
- Optimizing for spammy high-volume applications.
- Requiring a specific LLM provider or agent platform.
