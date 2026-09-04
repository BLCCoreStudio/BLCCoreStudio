<div align="center">

<img width="100%" src="./assets/banner.svg" alt="BLCCoreStudio developer profile" />

# BLCDev

**Independent developer building Android products, developer tools, Linux utilities, and open-source software under `BLCCoreStudio`.**

[![AgentContextMap](https://img.shields.io/badge/AgentContextMap-v0.2.3-24292F?style=flat-square&logo=rust&logoColor=white)](https://github.com/BLCCoreStudio/AgentContextMap)
[![RepoDoctor CI](https://img.shields.io/badge/Marketplace-RepoDoctor%20CI-24292F?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/repodoctor-ci)

</div>

## Selected work

| Project | What it does | Current status |
| --- | --- | --- |
| [AgentContextMap](https://github.com/BLCCoreStudio/AgentContextMap) | Maps which repository instructions can affect coding agents, including activation, scope, conflicts, SARIF and local HTML reports | **Stable v0.2.3** · Rust · GitHub Action |
| [RepoDoctor](https://github.com/BLCCoreStudio/RepoDoctor) | Repository health analysis with prioritized findings and optional CI quality gates | **Marketplace Action v0.1.3** · Alpha |
| [TurkishEvalKit](https://github.com/BLCCoreStudio/TurkishEvalKit) | Human-in-the-loop evaluation infrastructure for Turkish AI text/audio, review, calibration and reliability analysis | **Alpha 0.13.x** · Python |
| [BLCVoice](https://github.com/BLCCoreStudio/BLCVoice) | Local-first cross-platform voice dictation with evidence-based platform capability boundaries | **Pre-alpha** · Rust/Tauri |
| [OpenDevIndex](https://github.com/BLCCoreStudio/OpenDevIndex) | Source-backed structured technology knowledge map with validation and search tooling | **Active development** · Python |
| [TermKeys](https://github.com/BLCCoreStudio/TermKeys) | Safer terminal shortcut and configuration management for Linux | **Alpha v0.1.0** · Linux |

The public profile is intentionally selective. Older experiments and maintenance-only projects are not presented as active products.

## Android product work

Android products are being developed behind explicit engineering and release gates rather than published early for appearance's sake. Current work is focused on reproducible `./gradlew` builds, testable domain/data/UI boundaries, durable local persistence, permission and process-death behavior, accessibility, localization, device validation, installable test APKs, and evidence-backed release readiness.

Private product repositories remain private until a deliberate release/visibility decision is made. No private product is presented here as publicly available before that decision.

## Engineering standards

- **Evidence before claims.** Compile success is not treated as proof of runtime reliability, accessibility, performance, security or cross-platform compatibility.
- **Local-first where it matters.** Privacy boundaries and data ownership are explicit rather than implicit.
- **Reproducible delivery.** CI, pinned/reviewed dependencies, tests, checksums and release artifacts are part of the product surface.
- **Small maintenance surface.** Overlapping experiments are retired or moved to maintenance-only status instead of being kept artificially active.
- **No rewrite for its own sake.** Architecture changes must solve a measured product or engineering problem.
- **Transparent limitations.** Pre-alpha/alpha projects say so, and unsupported capabilities are not marketed as complete.

## Featured tools

### AgentContextMap

[AgentContextMap](https://github.com/BLCCoreStudio/AgentContextMap) is a local, read-only scanner for repository instruction systems used by Codex, Claude Code, Gemini CLI, GitHub Copilot, Cursor, Windsurf and Cline. It does not execute repository instructions or send repository content to an LLM service.

```yaml
- uses: BLCCoreStudio/AgentContextMap@v0.2.3
  with:
    path: .
```

### RepoDoctor CI

[RepoDoctor](https://github.com/BLCCoreStudio/RepoDoctor) turns repository-level engineering signals into a health score, prioritized findings and optional CI quality gates. The documented first-run configuration remains report-only so teams can inspect findings before enforcing thresholds.

```yaml
- uses: BLCCoreStudio/RepoDoctor@v0.1.3
```

## Open-source contributions

This account also carries contribution branches/forks for upstream projects. Those repositories are treated as contribution workspaces, not as BLCCoreStudio-authored products, and are intentionally excluded from the selected-product list above.

## Working areas

`Android` · `Rust` · `Python` · `Linux` · `Git/GitHub` · `GitHub Actions` · `CI/CD` · `local-first software` · `developer tooling` · `AI evaluation`

---

<div align="center">

**BLCDev · BLCCoreStudio**  
Build fewer things. Validate them properly. Maintain them well.

</div>
