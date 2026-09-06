#!/usr/bin/env python3
"""Generate the animated featured-project board for the BLCCoreStudio profile."""

from __future__ import annotations

import html
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OWNER = "BLCCoreStudio"
REPOS = ["OpenDevIndex", "RepoDoctor", "AgentContextMap", "BLCVoice"]
OUT = Path("assets/project-cards.svg")
ACCENTS = [
    ("#22D3EE", "#2563EB"),
    ("#A78BFA", "#EC4899"),
    ("#F59E0B", "#F97316"),
    ("#34D399", "#06B6D4"),
]


def api_get(url: str) -> dict:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "BLCCoreStudio-profile-generator",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=20) as response:
            return json.load(response)
    except (HTTPError, URLError) as exc:
        raise RuntimeError(f"GitHub API request failed for {url}: {exc}") from exc


def compact(value: int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}m".replace(".0m", "m")
    if value >= 1_000:
        return f"{value / 1_000:.1f}k".replace(".0k", "k")
    return str(value)


def shorten(text: str, limit: int = 72) -> str:
    text = " ".join((text or "No description yet.").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def card(repo: dict, x: int, y: int, index: int) -> str:
    name = esc(repo["name"])
    description = esc(shorten(repo.get("description") or ""))
    language = esc(repo.get("language") or "Mixed")
    stars = compact(int(repo.get("stargazers_count", 0)))
    forks = compact(int(repo.get("forks_count", 0)))
    updated = esc((repo.get("updated_at") or "")[:10] or "unknown")
    c1, c2 = ACCENTS[index]
    gid = f"g{index}"

    return f'''<g transform="translate({x} {y})">
  <defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>
  <rect width="570" height="205" rx="24" fill="#0A1020" stroke="url(#{gid})" stroke-opacity=".66" stroke-width="2"/>
  <circle cx="506" cy="37" r="48" fill="{c1}" opacity=".07"><animate attributeName="r" values="42;58;42" dur="3s" repeatCount="indefinite"/></circle>
  <circle cx="526" cy="55" r="24" fill="{c2}" opacity=".08"><animate attributeName="cy" values="55;42;55" dur="2.5s" repeatCount="indefinite"/></circle>
  <rect x="22" y="22" width="9" height="45" rx="4.5" fill="url(#{gid})"/>
  <text x="49" y="49" fill="#F8FAFC" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="25" font-weight="750">{name}</text>
  <text x="24" y="94" fill="#A9B7CA" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15.5">{description}</text>
  <line x1="24" y1="125" x2="546" y2="125" stroke="#FFFFFF" stroke-opacity=".07"/>
  <circle cx="30" cy="158" r="5" fill="{c1}"/><text x="44" y="163" fill="#CBD5E1" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13">{language}</text>
  <text x="199" y="163" fill="#FDE68A" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13">★ {stars}</text>
  <text x="280" y="163" fill="#C4B5FD" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13">⑂ {forks}</text>
  <text x="389" y="163" fill="#64748B" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="12">{updated}</text>
  <rect x="24" y="178" width="522" height="3" rx="1.5" fill="#172033"/>
  <rect x="24" y="178" width="172" height="3" rx="1.5" fill="url(#{gid})"><animate attributeName="x" values="24;374;24" dur="4.5s" repeatCount="indefinite"/></rect>
</g>'''


def build_svg(repos: list[dict]) -> str:
    positions = [(24, 96), (606, 96), (24, 319), (606, 319)]
    cards = [card(repo, *positions[i], i) for i, repo in enumerate(repos)]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="552" viewBox="0 0 1200 552" role="img" aria-labelledby="title desc">
  <title id="title">BLC Core Studio featured projects</title>
  <desc id="desc">Four colorful animated project cards with live public GitHub metadata.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#030712"/><stop offset=".55" stop-color="#07111F"/><stop offset="1" stop-color="#10091C"/></linearGradient>
    <linearGradient id="header" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22D3EE"/><stop offset=".5" stop-color="#A78BFA"/><stop offset="1" stop-color="#F472B6"/></linearGradient>
  </defs>
  <rect x="1" y="1" width="1198" height="550" rx="28" fill="url(#bg)" stroke="#FFFFFF" stroke-opacity=".07"/>
  <text x="28" y="44" fill="#F8FAFC" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="27" font-weight="780">Featured projects</text>
  <text x="28" y="69" fill="#64748B" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="12">4 selected public repositories · live metadata · mobile-friendly board</text>
  <rect x="956" y="28" width="212" height="35" rx="17.5" fill="#07111F" stroke="#22D3EE" stroke-opacity=".35"/>
  <circle cx="978" cy="45.5" r="5" fill="#34D399"><animate attributeName="opacity" values="1;.2;1" dur="1.15s" repeatCount="indefinite"/></circle>
  <text x="994" y="50" fill="#8CA0B8" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11">AUTO REFRESH</text>
  <rect x="24" y="82" width="1148" height="2" fill="url(#header)" opacity=".62"/>
  {''.join(cards)}
  <text x="28" y="541" fill="#43536A" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10.5">source: GitHub REST API · refreshed automatically by GitHub Actions</text>
</svg>'''


def main() -> None:
    repos = [api_get(f"https://api.github.com/repos/{OWNER}/{name}") for name in REPOS]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_svg(repos) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
