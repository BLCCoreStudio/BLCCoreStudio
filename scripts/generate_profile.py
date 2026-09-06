#!/usr/bin/env python3
"""Generate dependency-free SVG assets for the BLCCoreStudio profile README."""

from __future__ import annotations

import html
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OWNER = "BLCCoreStudio"
REPOS = [
    "OpenDevIndex",
    "AgentContextMap",
    "RepoDoctor",
    "BLCVoice",
    "TurkishEvalKit",
    "TermKeys",
]
OUT = Path("assets/project-cards.svg")


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


def shorten(text: str, limit: int = 86) -> str:
    text = " ".join((text or "No description yet.").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def svg_text(value: object) -> str:
    return html.escape(str(value), quote=True)


def card(repo: dict, x: int, y: int, index: int) -> str:
    name = svg_text(repo["name"])
    description = svg_text(shorten(repo.get("description") or ""))
    language = svg_text(repo.get("language") or "Mixed")
    stars = compact(int(repo.get("stargazers_count", 0)))
    forks = compact(int(repo.get("forks_count", 0)))
    updated = svg_text((repo.get("updated_at") or "")[:10] or "unknown")
    accent = ["#67E8F9", "#A78BFA", "#60A5FA", "#34D399", "#F472B6", "#FBBF24"][index % 6]

    return f'''<g transform="translate({x} {y})">
  <rect width="570" height="152" rx="18" fill="#0B121D" stroke="#FFFFFF" stroke-opacity="0.075"/>
  <rect width="5" height="152" rx="2.5" fill="{accent}" opacity="0.9"/>
  <circle cx="32" cy="34" r="6" fill="{accent}" opacity="0.95"/>
  <text x="50" y="42" fill="#F1F5F9" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="23" font-weight="700">{name}</text>
  <text x="28" y="77" fill="#94A3B8" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="14.5">{description}</text>
  <line x1="28" y1="101" x2="542" y2="101" stroke="#FFFFFF" stroke-opacity="0.055"/>
  <circle cx="34" cy="127" r="5" fill="{accent}" opacity="0.75"/>
  <text x="47" y="132" fill="#7F8FA4" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13">{language}</text>
  <text x="214" y="132" fill="#7F8FA4" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13">★ {stars}</text>
  <text x="292" y="132" fill="#7F8FA4" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13">⑂ {forks}</text>
  <text x="390" y="132" fill="#5E6F84" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="12">updated {updated}</text>
</g>'''


def build_svg(repos: list[dict]) -> str:
    cards = []
    for i, repo in enumerate(repos):
        col = i % 2
        row = i // 2
        cards.append(card(repo, 24 + col * 586, 92 + row * 170, i))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="620" viewBox="0 0 1200 620" role="img" aria-labelledby="title desc">
  <title id="title">BLC Core Studio live project cards</title>
  <desc id="desc">Automatically refreshed repository metadata for selected public projects.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#070B12"/>
      <stop offset="1" stop-color="#101827"/>
    </linearGradient>
    <linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#67E8F9"/>
      <stop offset="0.5" stop-color="#60A5FA"/>
      <stop offset="1" stop-color="#A78BFA"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="1198" height="618" rx="24" fill="url(#bg)" stroke="#FFFFFF" stroke-opacity="0.07"/>
  <text x="28" y="42" fill="#F1F5F9" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="24" font-weight="700">Live project board</text>
  <text x="28" y="66" fill="#64748B" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="12">public repository metadata · refreshed by GitHub Actions</text>
  <rect x="932" y="32" width="238" height="30" rx="15" fill="#0B141F" stroke="#67E8F9" stroke-opacity="0.22"/>
  <circle cx="952" cy="47" r="5" fill="#34D399"><animate attributeName="opacity" values="1;.25;1" dur="1.4s" repeatCount="indefinite"/></circle>
  <text x="968" y="51" fill="#74869B" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="12">AUTO REFRESH ENABLED</text>
  <rect x="24" y="78" width="1148" height="2" fill="url(#line)" opacity="0.48"/>
  {''.join(cards)}
  <text x="28" y="607" fill="#46576C" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11">source: GitHub REST API · generated from scripts/generate_profile.py</text>
</svg>'''


def main() -> None:
    repos = [api_get(f"https://api.github.com/repos/{OWNER}/{name}") for name in REPOS]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_svg(repos) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
