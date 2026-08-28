<div align="center">

<img width="100%" src="./assets/banner.svg" alt="BLC Core Studio — Developer Tools, Linux Utilities, Repository Intelligence" />

[![GitHub](https://img.shields.io/badge/GitHub-BLCCoreStudio-181717?style=for-the-badge&logo=github)](https://github.com/BLCCoreStudio)
[![RepoDoctor CI](https://img.shields.io/badge/Marketplace-RepoDoctor%20CI-1F6FEB?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/repodoctor-ci)
![Linux](https://img.shields.io/badge/Platform-Linux-06B6D4?style=for-the-badge&logo=linux&logoColor=white)
![Rust](https://img.shields.io/badge/Primary%20CLI-Rust-7C3AED?style=for-the-badge&logo=rust&logoColor=white)

### Practical developer tools for repositories, Linux workflows, and safer AI-assisted development.

</div>

---

## About

**BLC Core Studio** builds focused developer tools around repository diagnostics, Linux workflows, terminal productivity, local-first automation, and software safety.

The portfolio has two main tracks: released developer utilities and early-stage trust tooling for AI-assisted development. Projects are kept intentionally scoped, with explicit limitations and conservative behavior where safety matters.

---

## Featured Projects

### 🩺 [RepoDoctor CI](https://github.com/BLCCoreStudio/RepoDoctor)

Repository health scoring and CI quality gates across security, testing, documentation, CI/CD, dependencies, configuration, repository structure, and architecture.

**Marketplace Action:** [v0.1.3](https://github.com/BLCCoreStudio/RepoDoctor/releases/tag/v0.1.3) · **Engine:** [v0.1.1](https://github.com/BLCCoreStudio/RepoDoctor/releases/tag/v0.1.1) · **Alpha** · Linux x86_64

[![View on GitHub Marketplace](https://img.shields.io/badge/View%20on-GitHub%20Marketplace-1F6FEB?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/repodoctor-ci)

Use it in GitHub Actions with `BLCCoreStudio/RepoDoctor@v0.1.3`. The documented workflow uses read-only repository permissions and requires no RepoDoctor account or API key.

> RepoDoctor's complete analysis engine is proprietary. The public repository provides the Marketplace Action wrapper, documentation, verified releases, checksums, and product preview material.

### ⌨️ [TermKeys](https://github.com/BLCCoreStudio/TermKeys)

A lightweight Linux utility for installing useful terminal-editor shortcuts with backups, conflict detection, diagnostics, restore, and uninstall support.

**Current release:** [v0.1.0](https://github.com/BLCCoreStudio/TermKeys/releases/tag/v0.1.0) · **Alpha / pre-release** · Linux x86_64

> TermKeys is proprietary software. Its public repository contains intentionally published documentation, configuration examples, contribution resources, and release material.

---

## AI Agent Trust Tooling

Primary active development targets for safer, more reviewable AI-assisted development:

| Project | Focus |
| --- | --- |
| 🛡️ [AgentGuard](https://github.com/BLCCoreStudio/AgentGuard) | Deterministic command policy, local prompt-risk scanning, and optional Linux execution isolation |
| 🧾 [AgentTrail](https://github.com/BLCCoreStudio/AgentTrail) | Wrapped command evidence, integrity-verifiable receipts, and read-only working-tree review hints |
| 🩻 [MCPDoctor](https://github.com/BLCCoreStudio/MCPDoctor) | Local MCP configuration review, executable diagnostics, and baseline drift checks |
| 🧼 [ContextGuard](https://github.com/BLCCoreStudio/ContextGuard) | Local redaction of secrets and sensitive project context before sharing content with AI tools |

Focused companion repositories such as [SafeWorkspace](https://github.com/BLCCoreStudio/SafeWorkspace), [PromptShield](https://github.com/BLCCoreStudio/PromptShield), [AgentDiff](https://github.com/BLCCoreStudio/AgentDiff), [MCPWatch](https://github.com/BLCCoreStudio/MCPWatch), [ReleaseSeal](https://github.com/BLCCoreStudio/ReleaseSeal), and [DepGuard](https://github.com/BLCCoreStudio/DepGuard) preserve narrower experiments and implementation history.

---

## Published CLI Utilities

Open-source, MIT-licensed Rust utilities for everyday developer and Linux workflows.

| Project | What it does | Release |
| --- | --- | --- |
| 🔐 [EnvGuard](https://github.com/BLCCoreStudio/EnvGuard) | Detects secrets and sensitive files before they reach Git | [v0.1.0](https://github.com/BLCCoreStudio/EnvGuard/releases/tag/v0.1.0) |
| 🔌 [PortPeek](https://github.com/BLCCoreStudio/PortPeek) | Finds the process using a TCP or UDP port on Linux | [v0.1.0](https://github.com/BLCCoreStudio/PortPeek/releases/tag/v0.1.0) |
| 💾 [DiskHog](https://github.com/BLCCoreStudio/DiskHog) | Finds files and directories consuming the most disk space | [v0.1.0](https://github.com/BLCCoreStudio/DiskHog/releases/tag/v0.1.0) |
| #️⃣ [HashCheck](https://github.com/BLCCoreStudio/HashCheck) | Calculates and verifies SHA-256/SHA-512 checksums and release manifests | [v0.1.0](https://github.com/BLCCoreStudio/HashCheck/releases/tag/v0.1.0) |
| ⏱️ [BuildTimer](https://github.com/BLCCoreStudio/BuildTimer) | Measures command durations and keeps local timing history | [v0.1.0](https://github.com/BLCCoreStudio/BuildTimer/releases/tag/v0.1.0) |
| 🧹 [GitClean](https://github.com/BLCCoreStudio/GitClean) | Finds generated build/cache directories with dry-run and Git-aware safeguards | [v0.1.0](https://github.com/BLCCoreStudio/GitClean/releases/tag/v0.1.0) |
| 🔔 [TaskBell](https://github.com/BLCCoreStudio/TaskBell) | Notifies you when long-running terminal commands finish | [v0.1.0](https://github.com/BLCCoreStudio/TaskBell/releases/tag/v0.1.0) |

---

## Engineering Priorities

- **Conservative defaults** for destructive or security-sensitive actions.
- **Clear failure behavior** with actionable errors and documented limitations.
- **Local-first where practical** to avoid unnecessary uploads, accounts, or telemetry.
- **Verifiable releases** with versioned artifacts and checksum material where applicable.
- **Linux-first usability** with predictable CLI behavior and straightforward installation.

---

## Technology

<div align="center">

![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Cargo](https://img.shields.io/badge/Cargo-000000?style=flat-square&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

</div>

---

## Explore

- [RepoDoctor CI on GitHub Marketplace](https://github.com/marketplace/actions/repodoctor-ci)
- [All public repositories](https://github.com/BLCCoreStudio?tab=repositories)
- Use each repository's **Issues** page for bug reports and focused feature requests.
- Follow the repository's `SECURITY.md` for vulnerability reporting when available.

---

<div align="center">

### Build useful things. Keep them clear. Make them reliable.

[![Try RepoDoctor CI](https://img.shields.io/badge/Try-RepoDoctor%20CI-1F6FEB?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/repodoctor-ci)
[![View Repositories](https://img.shields.io/badge/View%20Repositories-2563EB?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BLCCoreStudio?tab=repositories)

</div>
