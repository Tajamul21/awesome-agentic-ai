# Contributing to Awesome Agentic AI Systems

Thank you for helping keep this list useful for researchers.

## What belongs here

A resource should be included when it is directly relevant to at least one of the following:

- agent loops: observe, reason, act, verify, update memory
- tool use, function calling, API use, browser use, computer use, code execution, robotics
- memory, planning, reflection, test-time scaling, verification, or orchestration
- multi-agent communication, coordination, or interoperability protocols
- benchmarks, datasets, evaluation methods, safety tests, or governance resources
- reproducibility practices for agentic systems

## What usually does not belong

- Generic chatbots without a closed-loop or tool-using component.
- Product pages without technical papers, documentation, or reproducible details.
- Benchmark numbers without an access date or exact model/scaffold version.
- Duplicated paper entries unless the work is foundational and fits multiple sections.

## Paper addition format

Please add a paper to `data/papers.yaml` using this format:

```yaml
- title: Paper Title
  year: 2026
  category: benchmark
  tags: [web, tools, evaluation]
  paper: https://arxiv.org/abs/XXXX.XXXXX
  code: https://github.com/org/repo
  project: https://project-page.example
  note: One sentence explaining why this is useful for agentic AI.
```

Then add a short entry to the relevant README table if the paper is important enough to be visible in the main page.

## Benchmark addition format

Please add benchmarks to `data/benchmarks.yaml`:

```yaml
- name: Benchmark Name
  year: 2026
  domain: web agents
  scale: 500 tasks across 20 websites
  feedback: task success, trajectory score, and citation checks
  paper: https://arxiv.org/abs/XXXX.XXXXX
  code: https://github.com/org/repo
  project: https://project-page.example
```

## Framework addition format

Please add frameworks to `data/frameworks.yaml`:

```yaml
- name: Framework Name
  category: orchestration framework
  best_for: stateful multi-agent workflows
  language: Python
  url: https://github.com/org/repo
  docs: https://docs.example.com
```

## Pull request checklist

Before opening a pull request:

- Check that the paper/resource is not already listed.
- Prefer official project pages, arXiv, OpenReview, ACL Anthology, PMLR, NeurIPS/ICLR/ICML pages, or official GitHub repositories.
- Avoid speculative claims. Keep notes short and descriptive.
- Run `python scripts/validate_metadata.py` from the repository root.
- Keep entries alphabetically or chronologically ordered within their section.

## Style guide

- Use ASCII punctuation for consistency.
- Use title case for paper titles only when the paper itself uses title case.
- Use short, factual notes.
- Do not add leaderboard claims unless you include access date and exact model/scaffold.
- Use consistent tags such as `web`, `coding`, `computer-use`, `multimodal`, `embodied`, `tools`, `memory`, `evaluation`, `safety`, `multi-agent`, `survey`.
