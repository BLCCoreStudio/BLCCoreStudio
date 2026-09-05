<div align="center">

<img width="100%" src="./assets/banner.svg" alt="BLCCoreStudio developer profile" />

# BLCDev

**Independent developer building developer tools, local-first software, Android products, and open-source infrastructure under `BLCCoreStudio`.**

`Rust` · `Python` · `Android` · `Linux` · `GitHub Actions` · `CI/CD` · `AI evaluation`

</div>

## Selected work

| Project | Focus | Status |
| --- | --- | --- |
| [AgentContextMap](https://github.com/BLCCoreStudio/AgentContextMap) | Maps repository instructions that can affect coding agents; local, read-only analysis with SARIF and HTML reporting | **Stable v0.2.3** · Rust · GitHub Action |
| [RepoDoctor](https://github.com/BLCCoreStudio/RepoDoctor) | Repository health analysis, prioritized findings, and optional CI quality gates | **Alpha** · GitHub Marketplace Action |
| [TurkishEvalKit](https://github.com/BLCCoreStudio/TurkishEvalKit) | Human-in-the-loop infrastructure for Turkish AI text/audio evaluation and reliability analysis | **Alpha 0.13.x** · Python |
| [BLCVoice](https://github.com/BLCCoreStudio/BLCVoice) | Privacy-oriented, local-first cross-platform voice dictation | **Pre-alpha** · Rust / Tauri |
| [OpenDevIndex](https://github.com/BLCCoreStudio/OpenDevIndex) | Source-backed structured technology knowledge map with validation and search tooling | **Active development** · Python |
| [TermKeys](https://github.com/BLCCoreStudio/TermKeys) | Safer terminal shortcut and configuration management for Linux | **Alpha v0.1.0** · Linux |

## Engineering focus

- **Evidence before claims** — compile success is not treated as proof of runtime reliability, security, accessibility, or compatibility.
- **Local-first where it matters** — privacy boundaries and data ownership are explicit.
- **Reproducible delivery** — CI, reviewed dependencies, tests, checksums, and release artifacts are part of the product surface.
- **Conservative compatibility claims** — unsupported or unverified platforms remain clearly labeled.
- **Maintainable scope** — experiments are consolidated or retired instead of being presented as mature products.

## Featured tools

### AgentContextMap

A local, read-only scanner for repository instruction systems used by Codex, Claude Code, Gemini CLI, GitHub Copilot, Cursor, Windsurf, and Cline. It does not execute repository instructions or send repository content to an LLM service.

```yaml
- uses: BLCCoreStudio/AgentContextMap@v0.2.3
  with:
    path: .
```

### RepoDoctor CI

Repository-level engineering signals become a health score, prioritized findings, and optional quality gates. The documented first run is report-only so teams can inspect results before enforcing thresholds.

```yaml
- uses: BLCCoreStudio/RepoDoctor@v0.1.3
```

## Open-source contributions

This account also contains forks used for upstream contribution work. They are contribution workspaces, not BLCCoreStudio-authored products, and are intentionally excluded from the product list above.

## Current direction

Public work is intentionally selective. New projects are expected to earn their place through a clear product boundary, reproducible validation, and an explicit maintenance plan before they are presented as active products.

---

<div align="center">

**BLCDev · BLCCoreStudio**  
Build fewer things. Validate them properly. Maintain them well.

</div>
