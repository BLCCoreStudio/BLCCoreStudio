<div align="center">

<img width="100%" src="./assets/banner.svg" alt="BLCCoreStudio — Developer tools, local-first software, and AI evaluation" />

[![AgentContextMap](https://img.shields.io/badge/AgentContextMap-v0.2.3-7C3AED?style=for-the-badge&logo=rust&logoColor=white)](https://github.com/BLCCoreStudio/AgentContextMap)
[![RepoDoctor CI](https://img.shields.io/badge/Marketplace-RepoDoctor%20CI-1F6FEB?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/repodoctor-ci)
![Linux](https://img.shields.io/badge/Platform-Linux-06B6D4?style=for-the-badge&logo=linux&logoColor=white)

### A small set of maintained developer tools, local-first software, and technical knowledge projects.

[**Explore AgentContextMap →**](https://github.com/BLCCoreStudio/AgentContextMap) · [**Try RepoDoctor CI →**](https://github.com/marketplace/actions/repodoctor-ci)

</div>

---

## Maintained projects

| Project | Focus | Status |
| --- | --- | --- |
| 🧭 [AgentContextMap](https://github.com/BLCCoreStudio/AgentContextMap) | Maps coding-agent instruction scope, activation, conflicts, and context | **Stable v0.2.3** · Rust · GitHub Action |
| 🩺 [RepoDoctor](https://github.com/BLCCoreStudio/RepoDoctor) | Repository health analysis and configurable CI quality gates | **Marketplace Action v0.1.3** · Alpha |
| 🇹🇷 [TurkishEvalKit](https://github.com/BLCCoreStudio/TurkishEvalKit) | Human-in-the-loop evaluation infrastructure for Turkish AI text and audio | **Alpha 0.11.x** · Python |
| 🎙️ [BLCVoice](https://github.com/BLCCoreStudio/BLCVoice) | Private cross-platform voice dictation with local-first speech recognition | **Pre-alpha** · Rust/Tauri |
| ⌨️ [TermKeys](https://github.com/BLCCoreStudio/TermKeys) | Safer terminal shortcuts and configuration management for Linux | **Alpha v0.1.0** · Linux |
| 🗺️ [OpenDevIndex](https://github.com/BLCCoreStudio/OpenDevIndex) | Source-backed, structured technology knowledge map | **Active development** · Python |

BLCCoreStudio is intentionally reducing maintenance surface. Older experiments and projects outside this set are being retired rather than kept artificially active.

---

## Engineering focus

- **Rust, Python, Linux, Git/GitHub, GitHub Actions and CI/CD**
- Local-first software with explicit privacy and security boundaries
- Reproducible builds, automated tests and evidence-backed release workflows
- Repository analysis, developer tooling and AI-assisted development infrastructure
- Human-in-the-loop AI evaluation
- Structured, source-backed technical knowledge
- Clear limitations instead of unsupported product claims

---

## Featured developer tools

### 🧭 AgentContextMap

**[AgentContextMap](https://github.com/BLCCoreStudio/AgentContextMap)** maps which repository instructions can affect Codex, Claude Code, Gemini CLI, GitHub Copilot, Cursor, Windsurf, and Cline.

It is local, read-only and deterministic: no LLM calls, no repository uploads, and no execution of repository instructions. The stable **v0.2.3** release includes a GitHub Action, SARIF 2.1.0 output for Code Scanning, conflict detection, target-path analysis, GitHub Actions job summaries, checksum verification, and a self-contained HTML report.

```yaml
- uses: BLCCoreStudio/AgentContextMap@v0.2.3
  with:
    path: .
```

### 🩺 RepoDoctor CI

**[RepoDoctor](https://github.com/BLCCoreStudio/RepoDoctor)** scores repository health across security, testing, documentation, CI/CD, dependencies, configuration, repository structure, and architecture, with optional quality gates.

```yaml
- uses: BLCCoreStudio/RepoDoctor@v0.1.3
```

---

## Upstream open-source work

Recent contributions focus on small, test-backed fixes in established projects.

- **Grafana Pathfinder** — [#1738](https://github.com/grafana/grafana-pathfinder-app/pull/1738) and [#1737](https://github.com/grafana/grafana-pathfinder-app/pull/1737) — **merged upstream**.
- **Microsoft TypeSpec** — [#11791](https://github.com/microsoft/typespec/pull/11791) — **under review**.
- **Microsoft MsQuic** — [#6282](https://github.com/microsoft/msquic/pull/6282) — **under review**.
- **rtk** — [#3778](https://github.com/rtk-ai/rtk/pull/3778) — **under review**.

---

## Engineering approach

- Keep the active project set deliberately small.
- Prefer **local-first** behavior where practical.
- Keep destructive and security-sensitive operations conservative by default.
- Use CI and tests as evidence, not decoration.
- Consolidate or retire overlapping experiments instead of maintaining them indefinitely.

<div align="center">

### Build fewer things. Make them useful. Maintain them well.

</div>