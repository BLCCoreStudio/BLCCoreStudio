<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:7C3AED,45:2563EB,100:06B6D4&text=BLC%20Core%20Studio&fontColor=FFFFFF&fontSize=46&fontAlignY=38&desc=Developer%20Tools%20%E2%80%A2%20Linux%20Utilities%20%E2%80%A2%20Repository%20Intelligence&descAlignY=58&descSize=16&animation=fadeIn" alt="BLC Core Studio" />

[![GitHub](https://img.shields.io/badge/GitHub-BLCCoreStudio-181717?style=for-the-badge&logo=github)](https://github.com/BLCCoreStudio)
![Linux](https://img.shields.io/badge/Platform-Linux-06B6D4?style=for-the-badge&logo=linux&logoColor=white)
![Rust](https://img.shields.io/badge/Primary%20CLI-Rust-7C3AED?style=for-the-badge&logo=rust&logoColor=white)

### Practical developer tools for repositories, terminals, and safer automation.

</div>

---

## About

**BLC Core Studio** builds focused developer tools around repository diagnostics, Linux workflows, terminal productivity, automation, and software safety.

The projects here are intentionally narrow in scope: each tool is designed to solve a specific workflow problem clearly and predictably rather than becoming a large all-in-one suite.

Published releases and development previews are separated below so project maturity is clear at a glance.

---

## Featured Projects

### 🩺 [RepoDoctor](https://github.com/BLCCoreStudio/RepoDoctor)

Repository diagnostics for security, testing, documentation, CI/CD, dependencies, configuration, structure, and architecture.

**Current release:** [v0.1.1](https://github.com/BLCCoreStudio/RepoDoctor/releases/tag/v0.1.1) · **Alpha / pre-release** · Linux x86_64

> RepoDoctor's complete implementation is proprietary and maintained privately. The public repository provides documentation and verified release artifacts.

### ⌨️ [TermKeys](https://github.com/BLCCoreStudio/TermKeys)

A lightweight Linux utility for installing useful terminal-editor shortcuts with backups, conflict detection, diagnostics, restore, and uninstall support.

**Current release:** [v0.1.0](https://github.com/BLCCoreStudio/TermKeys/releases/tag/v0.1.0) · **Alpha / pre-release** · Linux x86_64

> TermKeys is proprietary software. The public repository contains intentionally published documentation, configuration examples, contribution resources, and release material; public visibility does not make the complete implementation open source.

---

## Published CLI Utilities

Open-source, MIT-licensed Rust utilities for everyday developer and Linux workflows.

| Project | What it does | Release |
| --- | --- | --- |
| 🔐 [EnvGuard](https://github.com/BLCCoreStudio/EnvGuard) | Detects secrets and sensitive files before they reach Git | [v0.1.0](https://github.com/BLCCoreStudio/EnvGuard/releases/tag/v0.1.0) |
| 🔌 [PortPeek](https://github.com/BLCCoreStudio/PortPeek) | Finds the process using a TCP or UDP port on Linux | [v0.1.0](https://github.com/BLCCoreStudio/PortPeek/releases/tag/v0.1.0) |
| 💾 [DiskHog](https://github.com/BLCCoreStudio/DiskHog) | Finds files and directories consuming the most disk space | [v0.1.0](https://github.com/BLCCoreStudio/DiskHog/releases/tag/v0.1.0) |
| #️⃣ [HashCheck](https://github.com/BLCCoreStudio/HashCheck) | Calculates and verifies SHA-256 and SHA-512 checksums | [v0.1.0](https://github.com/BLCCoreStudio/HashCheck/releases/tag/v0.1.0) |
| ⏱️ [BuildTimer](https://github.com/BLCCoreStudio/BuildTimer) | Measures command durations and keeps local timing history | [v0.1.0](https://github.com/BLCCoreStudio/BuildTimer/releases/tag/v0.1.0) |
| 🧹 [GitClean](https://github.com/BLCCoreStudio/GitClean) | Finds generated build/cache directories with dry-run and Git-aware safeguards | [v0.1.0](https://github.com/BLCCoreStudio/GitClean/releases/tag/v0.1.0) |
| 🔔 [TaskBell](https://github.com/BLCCoreStudio/TaskBell) | Notifies you when long-running terminal commands finish | [v0.1.0](https://github.com/BLCCoreStudio/TaskBell/releases/tag/v0.1.0) |

---

## Development Previews

These repositories contain working early-stage implementations, but **do not have stable public releases yet**.

| Project | Current direction |
| --- | --- |
| 🛡️ [AgentGuard](https://github.com/BLCCoreStudio/AgentGuard) | Deterministic checks for risky shell commands before execution |
| 🩻 [MCPDoctor](https://github.com/BLCCoreStudio/MCPDoctor) | Local security-oriented review of MCP configuration files |
| 📦 [DepGuard](https://github.com/BLCCoreStudio/DepGuard) | Local dependency-manifest review for risky version/source patterns |
| 🧱 [PromptShield](https://github.com/BLCCoreStudio/PromptShield) | Local prompt-injection signal scanning for text files |
| 🧾 [AgentTrail](https://github.com/BLCCoreStudio/AgentTrail) | Local audit history for explicitly wrapped development commands |
| 🧰 [SafeWorkspace](https://github.com/BLCCoreStudio/SafeWorkspace) | Linux bubblewrap-based restricted workspaces for commands |
| 🔏 [ReleaseSeal](https://github.com/BLCCoreStudio/ReleaseSeal) | Deterministic SHA-256 release manifest creation and verification |
| 🔍 [AgentDiff](https://github.com/BLCCoreStudio/AgentDiff) | Read-only review of working-tree changes after AI-assisted work |
| 👁️ [MCPWatch](https://github.com/BLCCoreStudio/MCPWatch) | Local baseline monitoring for MCP configuration changes |
| 🧼 [ContextGuard](https://github.com/BLCCoreStudio/ContextGuard) | Local redaction of secrets and sensitive context before sharing |

Development-preview repositories should be evaluated from source and their documented limitations should be treated as part of the product behavior.

---

## Engineering Priorities

- **Clear failure behavior** — errors should explain what happened and what to do next.
- **Conservative defaults** — destructive or security-sensitive actions should be explicit.
- **Small tools, defined scope** — solve one workflow problem well.
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

- [All public repositories](https://github.com/BLCCoreStudio?tab=repositories)
- Use each repository's **Issues** page for bug reports and focused feature requests.
- Follow the repository's `SECURITY.md` for vulnerability reporting when available.
- Download binaries and verification files from the relevant **Releases** page.

---

<div align="center">

### Build useful things. Keep them clear. Make them reliable.

[![View Repositories](https://img.shields.io/badge/View%20Repositories-2563EB?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BLCCoreStudio?tab=repositories)

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=110&section=footer&color=0:06B6D4,50:2563EB,100:7C3AED" alt="footer" />

</div>
