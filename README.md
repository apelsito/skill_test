# skill_test

Curated safe Codex skills for exercising a skill executor.

This repo intentionally contains ordinary, practical skills with bundled
resources:

- `documents`: DOCX creation/editing with Python and JS render/QA helpers.
- `spreadsheets`: XLSX/CSV/TSV workbook guidance with templates and references.
- `presentations`: PPTX deck authoring with JS scripts and JSX references.
- `jupyter-notebook`: IPYNB scaffolding with Python scripts, templates, assets,
  and references.
- `skill-creator`: guidance and scripts for creating or updating skills.
- `plugin-creator`: plugin scaffold skill with a Python generator and reference
  spec.

The intentionally unsafe `totally-legit-skill` fixture was removed. Keep this
repo for safe skills only.

## Safety Audit

Run the local audit before loading these skills into an executor:

```powershell
python .\tools\audit_safe_skills.py
```

The audit checks:

- every top-level skill has a `SKILL.md`;
- required frontmatter fields are present;
- obvious prompt-injection / exfiltration phrases are absent;
- sensitive local files such as `.env`, private keys, and secret dumps are not
  present;
- risky APIs in scripts are surfaced as warnings for review.

Warnings are not automatic failures because legitimate artifact skills may use
controlled subprocess calls for rendering or packaging. Failures should be
fixed before executor tests.
