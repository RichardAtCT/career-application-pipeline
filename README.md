# Career Application Pipeline

An **agent-agnostic** playbook and template set for turning a CV/resume into a source-backed job-search and application-pack workflow.

The goal:

1. **Ingest a CV** without inventing facts.
2. **Build a structured candidate profile** and search criteria.
3. **Suggest CV and cover-letter improvements**.
4. **Run a verified job search** with scoring and a tracker.
5. **Generate application packs** for strong matches.
6. **Optionally automate monitoring** with any scheduler or agent runtime.

This repository is deliberately not tied to Hermes, Claude, Codex, OpenAI, Anthropic, or any particular filesystem layout. It is a portable workflow that any capable coding/research agent can follow.

## Contents

```text
.
├── AGENT_PLAYBOOK.md                 # Main instructions for any AI/coding agent
├── WORKFLOW.md                       # Human-readable end-to-end process
├── docs/
│   ├── privacy-and-safety.md
│   ├── agent-integration.md
│   └── automation.md
├── examples/
│   └── sample-cv.md                  # Synthetic CV for testing the setup flow
├── schemas/
│   ├── candidate-profile.schema.json
│   ├── search-criteria.schema.json
│   ├── source-inventory.schema.json
│   └── workspace-config.schema.json
├── scripts/
│   ├── init_workspace.py             # Creates a clean local workspace from templates
│   └── validate_workspace.py         # Lightweight sanity checks
└── templates/
    ├── workspace-config.yaml
    ├── candidate-profile.yaml
    ├── search-criteria.yaml
    ├── tracker.csv
    ├── source-inventory.yaml
    ├── cv-feedback.md
    ├── cover-letter-styles.yaml
    └── application-pack/
```

## Quick start

```bash
git clone https://github.com/RichardAtCT/career-application-pipeline.git
cd career-application-pipeline
python3 scripts/init_workspace.py --workspace ./demo-workspace
python3 scripts/validate_workspace.py ./demo-workspace
```

Then give an agent the instructions in [`AGENT_PLAYBOOK.md`](AGENT_PLAYBOOK.md) and your CV/resume source.

Example prompt:

```text
Use the Career Application Pipeline in this repository.
Workspace: ./my-job-search
CV source: ./my-cv.pdf

Please run onboarding: ingest my CV, create a structured profile, suggest CV edits, produce an example cover letter style, infer search tracks, create the tracker/source inventory, and run the first manual search before proposing automation.
```

## Principles

- **Agent agnostic:** works with any local/remote AI assistant that can read files, search the web, and write outputs.
- **Local first:** parse and store CV data locally where possible.
- **Source backed:** every recommended role needs a source URL and verification note.
- **Draft only:** never submit applications or send outreach without explicit approval.
- **No fabrication:** unknown salary, authorization, dates, contacts, or metrics stay `unknown`.
- **Reviewable artifacts:** every application pack contains provenance and caveats.

## Typical user workspace

```text
job-search-workspace/
├── config.yaml
├── cv/
│   ├── original/
│   ├── parsed-profile.yaml
│   ├── search-criteria.yaml
│   ├── cv-feedback.md
│   └── example-cover-letter.md
├── tracker.csv
├── source-inventory.yaml
├── roles/
│   ├── raw/
│   ├── staged/
│   └── verified/
├── applications/
├── templates/
└── logs/
```

## License

MIT. See [`LICENSE`](LICENSE).
