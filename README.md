# Agentic AI Systems: A Comprehensive Survey of LLM-based, Multimodal, Computer-Using, and Embodied Agents

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-coming_soon-b31b1b.svg)](#)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](#)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-welcome-blue.svg)](#)

<p align="center">
    <img src="./assets/teaser.png" alt="Agentic AI Survey Teaser" width="80%">
</p>

Welcome to the **Awesome-Agentic-AI-Systems** repository. This repository accompanies our survey on **Agentic AI Systems**, with a focus on **LLM-based agents, multimodal agents, computer-use agents, web agents, embodied agents, multi-agent systems, evaluation, safety, and open research challenges**.

This repository serves as a curated collection of:
- influential survey papers
- foundational agent papers
- benchmarks and datasets
- agent frameworks and libraries
- safety and alignment resources
- planning, memory, tool use, and multi-agent coordination works

Our work is based on the survey:

📄 **Agentic AI Systems: A Comprehensive Survey of LLM-based, Multimodal, Computer-Using, and Embodied Agents**

---

## Authors

**Tajamul Ashraf**, et al.  
<!-- Add co-authors here -->

- **Corresponding author:** [Tajamul Ashraf](https://www.tajamulashraf.com/)

Feel free to ⭐ star this repository and contribute relevant papers, libraries, benchmarks, and resources.

---

<p align="center">
  <img src="./assets/taxonomy.png" width="85%" />
</p>

**Figure:** A taxonomy of agentic AI systems organized by architecture, cognition loop, environment interaction, learning paradigm, coordination, evaluation, and safety.

---

## 📌 Contents

| Section | Subsection |
| ------- | ---------- |
| [📖 Survey Papers](#-survey-papers) | General Surveys, Agent Surveys, Multimodal Surveys |
| [🧠 Foundations of Agentic AI](#-foundations-of-agentic-ai) | Definitions, Agent Loop, Planning, Memory, Tool Use |
| [🤖 LLM-based Agents](#-llm-based-agents) | Single-Agent Systems, Tool-Augmented Agents, Reasoning Agents |
| [🌐 Web and Computer-Use Agents](#-web-and-computer-use-agents) | Browser Agents, GUI Agents, OS Agents |
| [🖼️ Multimodal Agents](#-multimodal-agents) | Vision-Language Agents, Grounded Agents, GUI Perception |
| [🦾 Embodied Agents](#-embodied-agents) | Robotics, Navigation, Manipulation, World Models |
| [🤝 Multi-Agent Systems](#-multi-agent-systems) | Coordination, Communication, Debate, Role Specialization |
| [🏆 Benchmarks and Evaluation](#-benchmarks-and-evaluation) | Task Success, Planning, Safety, Reliability |
| [🛡️ Safety, Alignment, and Security](#-safety-alignment-and-security) | Misuse, Robustness, Oversight, Agent Risks |
| [🛠️ Frameworks and Libraries](#-frameworks-and-libraries) | Open-Source Agent Stacks |
| [📚 Tutorials and Courses](#-tutorials-and-courses) | Lectures, Workshops, Reading Lists |
| [🔗 Other Resources](#-other-resources) | Blogs, Leaderboards, Community Lists |

---

# 📖 Survey Papers

## General Surveys

| Title | Date | Link |
|------|------|------|
| Agentic AI Systems: A Comprehensive Survey of LLM-based, Multimodal, Computer-Using, and Embodied Agents | 2026 | Coming soon |
| A Survey on Post-training of Large Language Models | 2025 | [arXiv](https://arxiv.org/abs/2503.06072) |
| LLM Post-Training: A Deep Dive into Reasoning Large Language Models | 2025 | [arXiv](https://arxiv.org/abs/2502.21321) |
| From System 1 to System 2: A Survey of Reasoning Large Language Models | 2025 | [arXiv](https://arxiv.org/abs/2502.17419) |
| Empowering LLMs with Logical Reasoning: A Comprehensive Survey | 2025 | [arXiv](https://arxiv.org/abs/2502.15652) |
| Reasoning with Large Language Models: A Survey | 2024 | [arXiv](https://arxiv.org/abs/2407.11511) |

## Vision / Multimodal / Foundation Model Surveys

| Title | Date | Link |
|------|------|------|
| Foundational Models Defining a New Era in Vision: A Survey and Outlook | 2023 | [arXiv](https://arxiv.org/abs/2307.13721) |
| A Survey on Multimodal Large Language Models | 2025 | [Link](#) |
| Reasoning VLMs and Recent Transformers in Perception | 2025 | Internal draft |

## Agent-focused Surveys

| Title | Date | Link |
|------|------|------|
| Survey of LLM Agents | 2024/2025 | Add links |
| Survey of Autonomous Agents | 2024/2025 | Add links |
| Survey of Embodied AI Agents | 2024/2025 | Add links |
| Survey of Web Agents / GUI Agents | 2024/2025 | Add links |

---

# 🧠 Foundations of Agentic AI

Agentic AI systems are typically built around a recurrent control loop:

**Perceive → Interpret → Plan → Act → Reflect → Update Memory**

Core components include:
- **Reasoning / Planning:** chain-of-thought, self-reflection, decomposition, search
- **Memory:** short-term context, episodic memory, retrieval memory, long-term memory
- **Tool Use:** calculators, APIs, code execution, web browsing, external software
- **Grounding:** vision, audio, GUI, physical sensors, environment state
- **Feedback / Learning:** post-training, reinforcement learning, verifiers, self-improvement

---

# 🤖 LLM-based Agents

## Representative Works
- ReAct
- Reflexion
- Toolformer
- AutoGPT
- BabyAGI
- Voyager
- SWE-agent
- Devin-style engineering agents
- Deep research assistants
- Reasoning + tool-use agents

## Themes
- task decomposition
- tool invocation
- self-correction
- planning under uncertainty
- long-horizon execution
- program synthesis and debugging

---

# 🌐 Web and Computer-Use Agents

Web and computer-use agents operate over:
- browsers
- search engines
- desktop interfaces
- operating systems
- enterprise software tools

## Representative Directions
- web navigation agents
- browser action agents
- computer-use foundation models
- GUI grounding and action prediction
- workflow automation agents

## Key Challenges
- partial observability
- fragile interfaces
- latency and tool reliability
- long-horizon failures
- safety in real-world automation

---

# 🖼️ Multimodal Agents

Multimodal agents extend language-only agents by incorporating:
- images
- video
- documents
- screenshots
- diagrams
- GUI states
- audio and speech
- spatial and embodied context

## Representative Capabilities
- image-grounded reasoning
- chart/table interpretation
- visual tool use
- screen understanding
- multimodal planning
- grounded instruction following

---

# 🦾 Embodied Agents

Embodied agents interact with physical or simulated environments.

## Core Areas
- navigation
- manipulation
- mobile robotics
- embodied QA
- human-robot collaboration
- world-model-based planning

## Important Properties
- closed-loop control
- action grounding
- safety constraints
- sensorimotor feedback
- real-time adaptation

---

# 🤝 Multi-Agent Systems

Multi-agent systems study coordination among multiple agents with specialized roles.

## Topics
- cooperation
- competition
- debate
- negotiation
- planner-executor architectures
- reviewer-critic setups
- distributed tool use
- communication protocols

## Emerging Trends
- role-specialized agents
- hierarchical agent organizations
- collaborative software engineering
- agent societies and market-based allocation
- protocol-level interoperability

---

# 🏆 Benchmarks and Evaluation

A major challenge in agentic AI is robust evaluation.

## Benchmark Categories
- **General task-solving:** GAIA, AgentBench
- **Web agents:** WebArena
- **Computer-use / OS agents:** OSWorld
- **Software engineering agents:** SWE-bench, SWE-agent evaluations
- **Embodied agents:** ALFWorld, Habitat, robotics benchmarks
- **Safety benchmarks:** OS-Harm and related red-team suites

## Evaluation Axes
- task success rate
- sample efficiency
- step efficiency
- robustness to environment shifts
- planning quality
- recovery from errors
- calibration and uncertainty
- safety and policy compliance
- human oversight burden

---

# 🛡️ Safety, Alignment, and Security

Agentic systems introduce new risks beyond standard LLMs.

## Key Risk Areas
- unsafe autonomous tool use
- prompt injection
- malicious websites / environments
- data exfiltration
- over-delegation
- hallucinated actions
- reward hacking
- deceptive alignment
- unsafe persistence and memory corruption

## Research Directions
- permissioned action spaces
- verifier-based execution
- human-in-the-loop oversight
- constitutional / rule-based control
- red teaming for agents
- audit trails and interpretability
- sandboxing and environment isolation

---

# 🛠️ Frameworks and Libraries

## Agent Frameworks
- LangChain
- LangGraph
- AutoGen
- CrewAI
- OpenAI Agents SDK
- Semantic Kernel
- Haystack Agents
- LlamaIndex agent tools

## Useful Infrastructure
- vector databases
- memory stores
- browser automation stacks
- code execution sandboxes
- tool registries
- environment simulators

---

# 📚 Tutorials and Courses

## Recommended Resources
- tutorials on LLM agents
- workshops on autonomous systems
- embodied AI lectures
- reasoning and planning tutorials
- alignment and safety courses

_Add curated links here._

---

# 🔗 Other Resources

- leaderboards
- curated benchmark pages
- open-source repos
- reproducibility checklists
- agent safety resources
- reading groups and community collections

---

## 🚀 Contribution Guidelines

We welcome contributions from the community.

You can contribute by:
- adding new papers
- fixing broken links
- improving taxonomy and categorization
- suggesting new benchmark sections
- adding libraries and codebases
- improving README organization

Please open a pull request or create an issue.

---

## Citation

If you find this repository useful, please cite our survey:

```bibtex
@article{ashraf2026agentic,
  title={Agentic AI Systems: A Comprehensive Survey of LLM-based, Multimodal, Computer-Using, and Embodied Agents},
  author={Ashraf, Tajamul and others},
  journal={arXiv preprint arXiv:XXXX.XXXXX},
  year={2026}
}
