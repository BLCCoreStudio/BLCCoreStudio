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

The current project family has two clear tracks:

- **released developer utilities** — small tools with versioned public releases
- **active trust tooling for AI-assisted development** — early-stage Rust projects with conservative, explainable behavior and explicit limitations

Focused companion repositories preserve smaller experiments and implementation history. When an experiment becomes part of a broader product, active integration moves into the primary project instead of deleting or republishing the original repository.

---

## Featured Projects

### 🩺 [RepoDoctor CI](https://github.com/BLCCoreStudio/RepoDoctor)

Repository health scoring and CI quality gates across security, testing, documentation, CI/CD, dependencies, configuration, repository structure, and architecture.

**Marketplace Action:** [v0.1.3](https://github.com/BLCCoreStudio/RepoDoctor/releases/tag/v0.1.3) · **Engine:** [v0.1.1](https://github.com/BLCCoreStudio/RepoDoctor/releases/tag/v0.1.1) · **Alpha** · Linux x86_64

[![View on GitHub Marketplace](https://img.shields.io/badge/View%20on-GitHub%20Marketplace-1F6FEB?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/repodoctor-ci)

Use it in GitHub Actions with `BLCCoreStudio/RepoDoctor@v0.1.3`. The documented workflow works with read-only repository permissions and does not require a RepoDoctor account or API key.

> RepoDoctor's complete analysis engine is proprietary and maintained privately. The public repository provides the Marketplace Action wrapper, documentation, verified releases, checksums, and product preview material.

### ⌨️ [TermKeys](https://github.com/BLCCoreStudio/TermKeys)

A lightweight Linux utility for installing useful terminal-editor shortcuts with backups, conflict detection, diagnostics, restore, and uninstall support.

**Current release:** [v0.1.0](https://github.com/BLCCoreStudio/TermKeys/releases/tag/v0.1.0) · **Alpha / pre-release** · Linux x86_64

> TermKeys is proprietary software. The public repository contains intentionally published documentation, configuration examples, contribution resources, and release material; public visibility does not make the complete implementation open source.

---

## AI Agent Trust Tooling

These are the primary active development targets for safer, more reviewable AI-assisted development. They contain working implementations but **do not have stable public releases yet**.

| Primary project | Current development direction |
| --- | --- |
| 🛡️ [AgentGuard](https://github.com/BLCCoreStudio/AgentGuard) | Deterministic command policy, local prompt-risk scanning, and an optional Linux bubblewrap execution boundary |
| 🧾 [AgentTrail](https://github.com/BLCCoreStudio/AgentTrail) | Wrapped command evidence, integrity-verifiable receipts, and read-only working-tree review hints |
| 🩻 [MCPDoctor](https://github.com/BLCCoreStudio/MCPDoctor) | Local MCP configuration review, safe executable diagnostics, and configuration-baseline drift checks |
| 🧼 [ContextGuard](https://github.com/BLCCoreStudio/ContextGuard) | Local redaction of secrets and sensitive project context before sharing content with AI tools |

The goal is not to label AI-generated work as universally “safe.” These tools are designed to make risky actions easier to constrain, changes easier to review, and local configuration/evidence easier to inspect.

---

## Companion Research

These repositories remain public intentionally. They are narrower experiments or review layers that feed primary projects while preserving their own history, links, tests, and focused implementation scope.

| Companion | Role | Primary integration target |
| --- | --- | --- |
| 🧰 [SafeWorkspace](https://github.com/BLCCoreStudio/SafeWorkspace) | Linux bubblewrap isolation research | [AgentGuard](https://github.com/BLCCoreStudio/AgentGuard) |
| 🧱 [PromptShield](https://github.com/BLCCoreStudio/PromptShield) | Deterministic prompt-risk scanning research | [AgentGuard](https://github.com/BLCCoreStudio/AgentGuard) |
| 🔍 [AgentDiff](https://github.com/BLCCoreStudio/AgentDiff) | Read-only diff-review experiments | [AgentTrail](https://github.com/BLCCoreStudio/AgentTrail) |
| 👁️ [MCPWatch](https://github.com/BLCCoreStudio/MCPWatch) | Local MCP configuration-baseline research | [MCPDoctor](https://github.com/BLCCoreStudio/MCPDoctor) |
| 🔏 [ReleaseSeal](https://github.com/BLCCoreStudio/ReleaseSeal) | Deterministic SHA-256 release-manifest research | [HashCheck](https://github.com/BLCCoreStudio/HashCheck) |

---

## Other Development Preview

### 📦 [DepGuard](https://github.com/BLCCoreStudio/DepGuard)

Local dependency-manifest review for risky version and source patterns. Its overlap with RepoDoctor dependency intelligence is being evaluated before any integration so duplicate findings are not introduced blindly.

Development-preview repositories should be evaluated from source, and their documented limitations should be treated as part of the product behavior.

---

## Incubation

New ideas are not automatically turned into public repositories. They graduate only after the product boundary, fixtures, and minimum implementation are strong enough to justify a standalone project.

- 🐤 **AgentCanary** — proposed security-contract test harness for coding agents. The design is currently being developed in [`incubator/AGENTCANARY.md`](./incubator/AGENTCANARY.md) before any standalone repository is created.

---

## Published CLI Utilities

Open-source, MIT-licensed Rust utilities for everyday developer and Linux workflows.

| Project | What it does | Release |
| --- | --- | --- |
| 🔐 [EnvGuard](https://github.com/BLCCoreStudio/EnvGuard) | Detects secrets and sensitive files before they reach Git | [v0.1.0](https://github.com/BLCCoreStudio/EnvGuard/releases/tag/v0.1.0) |
| 🔌 [PortPeek](https://github.com/BLCCoreStudio/PortPeek) | Finds the process using a TCP or UDP port on Linux | [v0.1.0](https://github.com/BLCCoreStudio/PortPeek/releases/tag/v0.1.0) |
| 💾 [DiskHog](https://github.com/BLCCoreStudio/DiskHog) | Finds files and directories consuming the most disk space | [v0.1.0](https://github.com/BLCCoreStudio/DiskHog/releases/tag/v0.1.0) |
| #️⃣ [HashCheck](https://github.com/BLCCoreStudio/HashCheck) | Calculates/verifies SHA-256/SHA-512 checksums; current development also adds deterministic SHA-256 release manifests | [v0.1.0](https://github.com/BLCCoreStudio/HashCheck/releases/tag/v0.1.0) |
| ⏱️ [BuildTimer](https://github.com/BLCCoreStudio/BuildTimer) | Measures command durations and keeps local timing history | [v0.1.0](https://github.com/BLCCoreStudio/BuildTimer/releases/tag/v0.1.0) |
| 🧹 [GitClean](https://github.com/BLCCoreStudio/GitClean) | Finds generated build/cache directories with dry-run and Git-aware safeguards | [v0.1.0](https://github.com/BLCCoreStudio/GitClean/releases/tag/v0.1.0) |
| 🔔 [TaskBell](https://github.com/BLCCoreStudio/TaskBell) | Notifies you when long-running terminal commands finish | [v0.1.0](https://github.com/BLCCoreStudio/TaskBell/releases/tag/v0.1.0) |

---

## Engineering Priorities

- **Clear failure behavior** — errors should explain what happened and what to do next.
- **Conservative defaults** — destructive or security-sensitive actions should be explicit.
- **Local-first where practical** — avoid unnecessary uploads, accounts, and telemetry.
- **Explainable safety controls** — findings should be review signals with documented scope, not unsupported guarantees.
- **Small tools, defined scope** — solve one workflow problem well, then integrate only where the product boundary becomes clearer.
- **Verifiable releases** — publish versioned artifacts and checksum material where applicable.
- **Linux-first usability** — predictable CLI behavior and straightforward installation.

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
- Download binaries and verification files from the relevant **Releases** page.

---

<div align="center">

### Build useful things. Keep them clear. Make them reliable.

[![Try RepoDoctor CI](https://img.shields.io/badge/Try-RepoDoctor%20CI-1F6FEB?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/repodoctor-ci)
[![View Repositories](https://img.shields.io/badge/View%20Repositories-2563EB?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BLCCoreStudio?tab=repositories)

</div>
