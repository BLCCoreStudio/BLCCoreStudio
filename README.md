<div align="center">

<img width="100%" src="./assets/banner.svg" alt="BLCCoreStudio — Developer tools, AI evaluation, security research, and local-first software" />

[![AgentContextMap](https://img.shields.io/badge/AgentContextMap-v0.2.3-7C3AED?style=for-the-badge&logo=rust&logoColor=white)](https://github.com/BLCCoreStudio/AgentContextMap)
[![RepoDoctor CI](https://img.shields.io/badge/Marketplace-RepoDoctor%20CI-1F6FEB?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/repodoctor-ci)
![Linux](https://img.shields.io/badge/Platform-Linux-06B6D4?style=for-the-badge&logo=linux&logoColor=white)

### Developer tooling, local-first AI workflows, security research, evaluation infrastructure, and open technical knowledge.

[**Explore AgentContextMap →**](https://github.com/BLCCoreStudio/AgentContextMap) · [**Try RepoDoctor CI →**](https://github.com/marketplace/actions/repodoctor-ci)

</div>

---

## Flagship projects

| Project | Focus | Status |
| --- | --- | --- |
| 🧭 [AgentContextMap](https://github.com/BLCCoreStudio/AgentContextMap) | Maps coding-agent instruction scope, activation, conflicts, and context | **Stable v0.2.3** · Rust · GitHub Action |
| 🩺 [RepoDoctor](https://github.com/BLCCoreStudio/RepoDoctor) | Repository health analysis and configurable CI quality gates | **Marketplace Action v0.1.3** · Alpha |
| 🔬 [BLCReverseLab](https://github.com/BLCCoreStudio/BLCReverseLab) | Evidence-first authorized reverse-engineering and application analysis workspace | **1.1 analysis line** · Python · JADX/Ghidra integration |
| 🇹🇷 [TurkishEvalKit](https://github.com/BLCCoreStudio/TurkishEvalKit) | Human-in-the-loop evaluation infrastructure for Turkish AI text and audio | **Alpha 0.11.x** · Python |
| 🎙️ [BLCVoice](https://github.com/BLCCoreStudio/BLCVoice) | Private cross-platform voice dictation with local-first speech recognition | **Pre-alpha** · Rust/Tauri |
| 🗺️ [OpenDevIndex](https://github.com/BLCCoreStudio/OpenDevIndex) | Source-backed, structured technology knowledge map | **Active development** · Python |

The profile intentionally highlights a small set of projects with clear scope, verifiable behavior, and maintained development paths rather than repository count.

---

## Engineering focus

- **Rust, Python, Android, Linux, Git/GitHub, GitHub Actions and CI/CD**
- Local-first software with explicit privacy and security boundaries
- Reproducible builds, automated tests and evidence-backed release workflows
- Repository analysis, developer tooling and AI-assisted development infrastructure
- Human-in-the-loop AI evaluation and evidence-oriented security tooling
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

[Explore the project](https://github.com/BLCCoreStudio/AgentContextMap) · [Use it in GitHub Actions](https://github.com/BLCCoreStudio/AgentContextMap#github-actions) · [Download v0.2.3](https://github.com/BLCCoreStudio/AgentContextMap/releases/tag/v0.2.3)

### 🩺 RepoDoctor CI

**[RepoDoctor](https://github.com/BLCCoreStudio/RepoDoctor)** scores repository health across security, testing, documentation, CI/CD, dependencies, configuration, repository structure, and architecture, with optional quality gates.

The published **GitHub Marketplace Action v0.1.3** starts in report-only mode and can later enforce a minimum score or finding severity.

```yaml
- uses: BLCCoreStudio/RepoDoctor@v0.1.3
```

[Explore RepoDoctor](https://github.com/BLCCoreStudio/RepoDoctor) · [View on GitHub Marketplace](https://github.com/marketplace/actions/repodoctor-ci)

---

## Upstream open-source work

Recent contributions focus on small, test-backed fixes in established projects.

- **Grafana Pathfinder** — [#1738](https://github.com/grafana/grafana-pathfinder-app/pull/1738) and [#1737](https://github.com/grafana/grafana-pathfinder-app/pull/1737) — **merged upstream**.
- **Microsoft TypeSpec** — [#11791](https://github.com/microsoft/typespec/pull/11791) — generated C# model-description fix; **under review**.
- **Microsoft MsQuic** — [#6282](https://github.com/microsoft/msquic/pull/6282) — Linux `SOCK_CLOEXEC` datapath fix; **under review**.
- **rtk** — [#3778](https://github.com/rtk-ai/rtk/pull/3778) — Windows GNU linker-stack fix; **under review**.

---

## Engineering approach

- Prefer **local-first** behavior where practical.
- Keep destructive and security-sensitive operations conservative by default.
- Use CI and tests as evidence, not decoration.
- Document important limitations and trust boundaries explicitly.
- Consolidate overlapping experiments instead of presenting every prototype as a standalone flagship product.

<div align="center">

### Build useful things. Keep them clear. Make them reliable.

[![Explore AgentContextMap](https://img.shields.io/badge/Explore-AgentContextMap-7C3AED?style=for-the-badge&logo=rust&logoColor=white)](https://github.com/BLCCoreStudio/AgentContextMap)
[![Try RepoDoctor CI](https://img.shields.io/badge/Try-RepoDoctor%20CI-1F6FEB?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/repodoctor-ci)

</div>