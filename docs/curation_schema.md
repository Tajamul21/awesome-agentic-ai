# Curation schema

This repository keeps the main README readable while storing structured metadata in YAML files.

## `data/papers.yaml`

Required fields:

- `title`: paper title
- `year`: publication or arXiv year
- `category`: one of `foundations`, `benchmark`, `survey`, `safety`, `multi-agent`, `multimodal`, `embodied`, `coding`, `orchestration`, or a similarly clear label
- `tags`: compact topical tags
- `paper`: canonical paper link when available

Optional fields:

- `code`: official repository
- `project`: official project page
- `note`: one sentence explaining why the work matters

## `data/benchmarks.yaml`

Required fields:

- `name`
- `year`
- `domain`
- `scale`
- `feedback`

Recommended fields:

- `paper`
- `code`
- `project`

## `data/frameworks.yaml`

Required fields:

- `name`
- `category`
- `best_for`
- `url`

Recommended fields:

- `docs`
- `language`

## Curation rules

1. Prefer official paper, project, code, and documentation links.
2. Keep notes descriptive rather than promotional.
3. Do not add leaderboard claims without access date and exact scaffold details.
4. Keep safety, reproducibility, and benchmark realism visible.
5. Run `python scripts/validate_metadata.py` before opening a pull request.
