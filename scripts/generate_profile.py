#!/usr/bin/env python3
"""Generate the red-accented BLCCoreStudio project board from live GitHub metadata."""

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
    "RepoDoctor",
    "AgentContextMap",
    "BLCVoice",
    "TurkishEvalKit",
    "TermKeys",
]
OUT = Path("assets/project-cards.svg")

LANG_COLORS = {
    "Python": "#3572A5",
    "Shell": "#89E051",
    "Rust": "#DEA584",
    "Kotlin": "#A97BFF",
    "Java": "#B07219",
    "TypeScript": "#3178C6",
    "JavaScript": "#F1E05A",
}

ICONS = {
    "OpenDevIndex": """<g transform=\"translate(52 45)\" stroke=\"#ff416c\" stroke-width=\"9\" fill=\"none\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"34\" cy=\"34\" r=\"27\"/><path d=\"M34 7v13M34 48v13M7 34h13M48 34h13M15 15l9 9M44 44l9 9M53 15l-9 9M24 44l-9 9\"/></g>""",
    "RepoDoctor": """<g transform=\"translate(51 43)\" stroke=\"#60a5fa\" stroke-width=\"8\" fill=\"none\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 26h18l8-14 10 42 9-19h17\"/><rect x=\"7\" y=\"7\" width=\"68\" height=\"56\" rx=\"16\" opacity=\".35\"/></g>""",
    "AgentContextMap": """<g transform=\"translate(49 41)\" fill=\"none\" stroke=\"#ff416c\" stroke-width=\"7\" stroke-linejoin=\"round\"><path d=\"M38 8L8 24l30 16 30-16L38 8Z\"/><path d=\"M8 37l30 16 30-16\"/><path d=\"M8 50l30 16 30-16\"/></g>""",
    "BLCVoice": """<g transform=\"translate(52 37)\" fill=\"none\" stroke=\"#a855f7\" stroke-width=\"8\" stroke-linecap=\"round\"><rect x=\"20\" y=\"4\" width=\"34\" height=\"51\" rx=\"17\"/><path d=\"M10 40c0 25 54 25 54 0M37 66v16M23 82h28\"/></g>""",
    "TurkishEvalKit": """<g transform=\"translate(53 37)\" fill=\"none\" stroke=\"#ff416c\" stroke-width=\"7\" stroke-linejoin=\"round\"><path d=\"M10 5h43l17 17v57H10Z\"/><path d=\"M53 5v19h17\"/><path d=\"M24 37h32M24 50h32M24 63h19\"/><text x=\"36\" y=\"78\" font-family=\"ui-monospace,monospace\" font-size=\"13\" fill=\"#ff416c\" stroke=\"none\">TR</text></g>""",
    "TermKeys": """<g transform=\"translate(49 42)\" fill=\"none\" stroke=\"#35e06f\" stroke-width=\"9\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 14l23 23-23 23M44 60h24\"/></g>""",
}


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


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def shorten(text: str, limit: int = 92) -> str:
    text = " ".join((text or "No description yet.").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def card(repo: dict, y: int, index: int) -> str:
    name = esc(repo["name"])
    description = esc(shorten(repo.get("description") or ""))
    language = esc(repo.get("language") or "Mixed")
    lang_color = LANG_COLORS.get(repo.get("language") or "", "#94A3B8")
    stars = compact(int(repo.get("stargazers_count", 0)))
    forks = compact(int(repo.get("forks_count", 0)))
    icon = ICONS.get(repo["name"], "")
    accent = "#22c55e" if repo["name"] == "TermKeys" else "#ff416c"
    return f"""
  <g transform=\"translate(44 {y})\">
    <rect width=\"1112\" height=\"160\" rx=\"28\" fill=\"#151b2a\" stroke=\"#ffffff\" stroke-opacity=\".075\"/>
    <rect width=\"1112\" height=\"160\" rx=\"28\" fill=\"url(#cardGlow{index})\" opacity=\".10\"/>
    <rect x=\"24\" y=\"22\" width=\"112\" height=\"116\" rx=\"24\" fill=\"#0b111d\" stroke=\"{accent}\" stroke-opacity=\".55\" stroke-width=\"2\"/>
    <rect x=\"25\" y=\"23\" width=\"110\" height=\"114\" rx=\"23\" fill=\"{accent}\" opacity=\".06\">
      <animate attributeName=\"opacity\" values=\".04;.14;.04\" dur=\"{2.3 + index * .22:.2f}s\" repeatCount=\"indefinite\"/>
    </rect>
    {icon}
    <text x=\"168\" y=\"56\" fill=\"#ff4f79\" font-family=\"Inter,Segoe UI,Arial,sans-serif\" font-size=\"34\" font-weight=\"780\">{name}</text>
    <text x=\"168\" y=\"92\" fill=\"#c8d2e3\" font-family=\"Inter,Segoe UI,Arial,sans-serif\" font-size=\"20\">{description}</text>
    <circle cx=\"179\" cy=\"126\" r=\"9\" fill=\"{lang_color}\"/>
    <text x=\"197\" y=\"133\" fill=\"#e2e8f0\" font-family=\"Inter,Segoe UI,Arial,sans-serif\" font-size=\"20\">{language}</text>
    <text x=\"360\" y=\"133\" fill=\"#facc15\" font-family=\"Inter,Segoe UI Symbol,Arial,sans-serif\" font-size=\"24\">☆</text>
    <text x=\"393\" y=\"133\" fill=\"#e2e8f0\" font-family=\"ui-monospace,SFMono-Regular,Consolas,monospace\" font-size=\"19\">{stars}</text>
    <text x=\"475\" y=\"133\" fill=\"#facc15\" font-family=\"Inter,Segoe UI Symbol,Arial,sans-serif\" font-size=\"24\">⑂</text>
    <text x=\"510\" y=\"133\" fill=\"#e2e8f0\" font-family=\"ui-monospace,SFMono-Regular,Consolas,monospace\" font-size=\"19\">{forks}</text>
    <circle cx=\"1057\" cy=\"80\" r=\"31\" fill=\"#281d2c\"/>
    <path d=\"M1049 66l15 14-15 14\" fill=\"none\" stroke=\"#ff416c\" stroke-width=\"7\" stroke-linecap=\"round\" stroke-linejoin=\"round\">
      <animate attributeName=\"stroke-opacity\" values=\".55;1;.55\" dur=\"1.6s\" repeatCount=\"indefinite\"/>
    </path>
    <rect x=\"0\" y=\"158\" width=\"1112\" height=\"2\" fill=\"url(#accentLine)\" opacity=\".16\"/>
  </g>"""


def build_svg(repos: list[dict]) -> str:
    cards = "".join(card(repo, 300 + i * 185, i) for i, repo in enumerate(repos))
    gradients = "".join(
        f'<linearGradient id="cardGlow{i}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff416c"/><stop offset=".55" stop-color="#ff416c" stop-opacity=".15"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient>'
        for i in range(len(repos))
    )
    return f"""<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1200\" height=\"1500\" viewBox=\"0 0 1200 1500\" role=\"img\" aria-labelledby=\"title desc\">
<title id=\"title\">BLCCoreStudio Top Open Source Projects</title>
<desc id=\"desc\">Six large red-accented project cards with automatically refreshed repository metadata.</desc>
<defs>
  <linearGradient id=\"bg\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\"><stop offset=\"0\" stop-color=\"#060912\"/><stop offset=\".55\" stop-color=\"#0b101c\"/><stop offset=\"1\" stop-color=\"#110914\"/></linearGradient>
  <linearGradient id=\"titleGrad\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"0\"><stop offset=\"0\" stop-color=\"#ffffff\"/><stop offset=\".42\" stop-color=\"#ff416c\"/><stop offset=\".72\" stop-color=\"#ff5f84\"/><stop offset=\"1\" stop-color=\"#ffffff\"/></linearGradient>
  <linearGradient id=\"accentLine\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"0\"><stop offset=\"0\" stop-color=\"#ff416c\"/><stop offset=\".5\" stop-color=\"#ff5f84\"/><stop offset=\"1\" stop-color=\"#8b5cf6\"/></linearGradient>
  {gradients}
  <filter id=\"pinkGlow\" x=\"-50%\" y=\"-50%\" width=\"200%\" height=\"200%\"><feGaussianBlur stdDeviation=\"7\" result=\"b\"/><feMerge><feMergeNode in=\"b\"/><feMergeNode in=\"SourceGraphic\"/></feMerge></filter>
  <pattern id=\"stars\" width=\"77\" height=\"77\" patternUnits=\"userSpaceOnUse\"><circle cx=\"13\" cy=\"12\" r=\"1\" fill=\"#ff416c\" opacity=\".22\"/><circle cx=\"55\" cy=\"41\" r=\"1.3\" fill=\"#ffffff\" opacity=\".08\"/></pattern>
</defs>
<rect x=\"1\" y=\"1\" width=\"1198\" height=\"1498\" rx=\"34\" fill=\"url(#bg)\" stroke=\"#ffffff\" stroke-opacity=\".06\"/>
<rect x=\"1\" y=\"1\" width=\"1198\" height=\"1498\" rx=\"34\" fill=\"url(#stars)\"/>
<text x=\"56\" y=\"64\" fill=\"#ff4f79\" font-family=\"ui-monospace,SFMono-Regular,Consolas,monospace\" font-size=\"24\" font-weight=\"700\">&gt; BLCCoreStudio</text>
<text x=\"56\" y=\"96\" fill=\"#6d7b92\" font-family=\"ui-monospace,SFMono-Regular,Consolas,monospace\" font-size=\"13\" letter-spacing=\"5\">CODE  BUILD  SHARE  REPEAT</text>
<rect x=\"46\" y=\"135\" width=\"8\" height=\"100\" rx=\"4\" fill=\"#ff416c\" filter=\"url(#pinkGlow)\"><animate attributeName=\"opacity\" values=\".55;1;.55\" dur=\"2s\" repeatCount=\"indefinite\"/></rect>
<text x=\"78\" y=\"192\" fill=\"url(#titleGrad)\" font-family=\"Inter,Segoe UI,Arial,sans-serif\" font-size=\"58\" font-weight=\"850\">Top Open Source Projects</text>
<text x=\"82\" y=\"233\" fill=\"#a7b0c1\" font-family=\"ui-monospace,SFMono-Regular,Consolas,monospace\" font-size=\"18\" letter-spacing=\"9\">BY BLCCORESTUDIO</text>
<rect x=\"720\" y=\"220\" width=\"425\" height=\"42\" rx=\"21\" fill=\"#190b15\" stroke=\"#ff416c\" stroke-opacity=\".68\"/>
<circle cx=\"748\" cy=\"241\" r=\"6\" fill=\"#34d399\"><animate attributeName=\"opacity\" values=\"1;.25;1\" dur=\"1.2s\" repeatCount=\"indefinite\"/></circle>
<text x=\"766\" y=\"247\" fill=\"#ff6c91\" font-family=\"ui-monospace,SFMono-Regular,Consolas,monospace\" font-size=\"15\">LIVE METADATA · AUTO REFRESH</text>
{cards}
<g opacity=\".72\">
  <path d=\"M0 1444L80 1398L128 1420L181 1375L255 1428L324 1407L397 1440L463 1384L530 1420L619 1400L710 1446L802 1408L885 1429L965 1380L1046 1419L1112 1397L1200 1440V1500H0Z\" fill=\"#150b19\"/>
  <path d=\"M0 1453L81 1418L130 1431L184 1394L255 1445L322 1423L398 1453L468 1400L529 1437L620 1418L710 1461L805 1425L886 1446L964 1400L1046 1438L1112 1416L1200 1456\" fill=\"none\" stroke=\"#ff416c\" stroke-width=\"5\" stroke-linejoin=\"round\"><animate attributeName=\"stroke-opacity\" values=\".35;1;.35\" dur=\"3s\" repeatCount=\"indefinite\"/></path>
  <circle cx=\"1080\" cy=\"1395\" r=\"47\" fill=\"#ff416c\" opacity=\".18\"/>
</g>
<text x=\"345\" y=\"1470\" fill=\"#667085\" font-family=\"ui-monospace,SFMono-Regular,Consolas,monospace\" font-size=\"12\" letter-spacing=\"6\">SMALL PROJECTS · BIGGER POSSIBILITIES</text>
</svg>"""


def main() -> None:
    repos = [api_get(f"https://api.github.com/repos/{OWNER}/{name}") for name in REPOS]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_svg(repos) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
