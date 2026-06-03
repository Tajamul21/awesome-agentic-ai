from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

COLORS = {
    "ink": "#0F172A",
    "muted": "#475569",
    "line": "#CBD5E1",
    "bg": "#F8FAFC",
    "card": "#FFFFFF",
    "blue": "#2563EB",
    "blue2": "#1D4ED8",
    "cyan": "#0891B2",
    "teal": "#0F766E",
    "green": "#16A34A",
    "violet": "#7C3AED",
    "purple": "#6D28D9",
    "amber": "#D97706",
    "rose": "#E11D48",
    "slate": "#334155",
    "pale_blue": "#EFF6FF",
    "pale_teal": "#ECFDF5",
    "pale_violet": "#F5F3FF",
    "pale_amber": "#FFFBEB",
    "pale_rose": "#FFF1F2",
    "pale_cyan": "#ECFEFF",
}


def wrap(text, width=22):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        if len(cur) + len(word) + (1 if cur else 0) <= width:
            cur = f"{cur} {word}".strip()
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text(x, y, content, size=16, weight="500", fill=None, anchor="start", extra=""):
    fill = fill or COLORS["ink"]
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" font-family="Inter,Segoe UI,Arial,sans-serif" {extra}>{escape(content)}</text>'


def multiline(x, y, content, size=14, fill=None, width=30, gap=18, weight="400"):
    parts = []
    for i, line in enumerate(wrap(content, width)):
        parts.append(text(x, y + i * gap, line, size=size, fill=fill, weight=weight))
    return "\n".join(parts)


def rect(x, y, w, h, fill, stroke=None, r=14, sw=1, opacity=1):
    stroke_attr = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" opacity="{opacity}"{stroke_attr}/>'


def pill(x, y, w, h, label, fill, stroke=None, txt=None, size=13):
    txt = txt or COLORS["ink"]
    return "\n".join([
        rect(x, y, w, h, fill=fill, stroke=stroke, r=h/2),
        text(x + w/2, y + h/2 + 5, label, size=size, weight="700", fill=txt, anchor="middle"),
    ])


def card(x, y, w, h, title, body, accent, pale, icon=None):
    s = [rect(x, y, w, h, COLORS["card"], stroke="#E2E8F0", r=18),
         rect(x, y, 8, h, accent, r=18),
         text(x + 22, y + 32, title, size=18, weight="800", fill=COLORS["ink"]),
         rect(x + 22, y + 48, 58, 4, accent, r=2),
         multiline(x + 22, y + 78, body, size=13, fill=COLORS["muted"], width=28, gap=17)]
    if icon:
        s.append(pill(x + w - 64, y + 18, 42, 28, icon, pale, stroke=accent, txt=accent, size=15))
    return "\n".join(s)


def header_defs():
    return """
<defs>
  <linearGradient id="bgGrad" x1="0" x2="1" y1="0" y2="1">
    <stop offset="0%" stop-color="#F8FAFC"/>
    <stop offset="52%" stop-color="#EFF6FF"/>
    <stop offset="100%" stop-color="#F5F3FF"/>
  </linearGradient>
  <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
    <path d="M0,0 L0,6 L9,3 z" fill="#64748B" />
  </marker>
</defs>
"""


def agentic_landscape():
    w, h = 1280, 720
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
             '<title id="title">Agentic AI systems landscape</title>',
             '<desc id="desc">A systems map for agentic AI showing the loop, methods, domains, evaluation, safety, and infrastructure.</desc>',
             header_defs(),
             rect(0, 0, w, h, 'url(#bgGrad)', r=0),
             '<circle cx="1020" cy="110" r="150" fill="#DBEAFE" opacity="0.45"/>',
             '<circle cx="250" cy="640" r="220" fill="#CCFBF1" opacity="0.38"/>',
             text(640, 62, "Awesome Agentic AI Systems", size=34, weight="900", fill=COLORS["ink"], anchor="middle"),
             text(640, 94, "Papers, benchmarks, frameworks, safety resources, and metadata for closed-loop AI agents", size=16, weight="500", fill=COLORS["muted"], anchor="middle"),
             pill(330, 120, 150, 34, "50+ papers", COLORS["pale_blue"], stroke=COLORS["blue"], txt=COLORS["blue"]),
             pill(500, 120, 160, 34, "24 benchmarks", COLORS["pale_teal"], stroke=COLORS["teal"], txt=COLORS["teal"]),
             pill(680, 120, 160, 34, "12 frameworks", COLORS["pale_violet"], stroke=COLORS["violet"], txt=COLORS["violet"]),
             pill(860, 120, 170, 34, "living metadata", COLORS["pale_amber"], stroke=COLORS["amber"], txt=COLORS["amber"]),
             '<g>']

    # Central loop
    parts.append(rect(400, 192, 480, 310, COLORS["card"], stroke="#E2E8F0", r=28))
    parts.append(text(640, 232, "Agentic system loop", size=24, weight="900", anchor="middle"))
    cx, cy = 640, 355
    nodes = [
        (640, 280, "Observe", COLORS["blue"], COLORS["pale_blue"]),
        (760, 355, "Reason", COLORS["violet"], COLORS["pale_violet"]),
        (640, 430, "Act", COLORS["teal"], COLORS["pale_teal"]),
        (520, 355, "Verify", COLORS["amber"], COLORS["pale_amber"]),
    ]
    # curved loop path
    parts.append('<path d="M640 300 C735 300 785 330 785 355 C785 398 735 420 660 420" fill="none" stroke="#64748B" stroke-width="2.4" stroke-dasharray="6 5" marker-end="url(#arrow)"/>')
    parts.append('<path d="M620 420 C535 420 493 397 493 355 C493 313 535 300 620 300" fill="none" stroke="#64748B" stroke-width="2.4" stroke-dasharray="6 5" marker-end="url(#arrow)"/>')
    for x, y, label, accent, pale in nodes:
        parts.append(rect(x-72, y-28, 144, 56, pale, stroke=accent, r=20, sw=2))
        parts.append(text(x, y+6, label, size=17, weight="800", fill=accent, anchor="middle"))
    parts.append(rect(557, 337, 166, 46, "#F8FAFC", stroke="#CBD5E1", r=22))
    parts.append(text(640, 366, "Memory + State", size=15, weight="800", fill=COLORS["slate"], anchor="middle"))
    parts.append(text(640, 470, "Feedback updates future decisions", size=13, weight="600", fill=COLORS["muted"], anchor="middle"))

    # surrounding cards
    parts.append(card(70, 205, 285, 128, "Foundations", "LLMs, VLMs, tool-use priors, instruction tuning, reasoning traces.", COLORS["blue"], COLORS["pale_blue"], "01"))
    parts.append(card(70, 370, 285, 128, "Optimization", "SFT, preference optimization, RL, process rewards, verifiers, test-time scaling.", COLORS["teal"], COLORS["pale_teal"], "02"))
    parts.append(card(925, 205, 285, 128, "Domains", "Web, code, desktop, mobile, multimodal, embodied, scientific, and enterprise agents.", COLORS["violet"], COLORS["pale_violet"], "03"))
    parts.append(card(925, 370, 285, 128, "Deployment safety", "Benchmarks, cost, reproducibility, prompt-injection defense, governance, oversight.", COLORS["rose"], COLORS["pale_rose"], "04"))
    parts.append('</g>')

    # design tuple
    parts.append(rect(125, 552, 1030, 96, COLORS["card"], stroke="#E2E8F0", r=22))
    parts.append(text(160, 586, "Reusable comparison tuple", size=20, weight="900"))
    tuple_items = [("Observation", COLORS["blue"]), ("Memory", COLORS["teal"]), ("Planning", COLORS["violet"]), ("Action", COLORS["amber"]), ("Verifier", COLORS["rose"]), ("Oversight", COLORS["slate"])]
    x = 160
    for label, color in tuple_items:
        parts.append(pill(x, 606, 140, 32, label, "#F8FAFC", stroke=color, txt=color, size=13))
        x += 160

    parts.append('</svg>')
    (ASSETS / "agentic-landscape.svg").write_text("\n".join(parts), encoding="utf-8")


def benchmark_map():
    w, h = 1280, 760
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
             '<title id="title">Benchmark map for agentic AI systems</title>',
             '<desc id="desc">A domain by feedback-strength map of major agentic AI benchmarks.</desc>',
             header_defs(), rect(0, 0, w, h, 'url(#bgGrad)', r=0),
             text(640, 56, "Agent Benchmark Map", size=32, weight="900", anchor="middle"),
             text(640, 86, "Use this map to choose evaluations by domain, verifier strength, and deployment realism.", size=16, fill=COLORS["muted"], anchor="middle")]
    # axes
    left, top, grid_w, grid_h = 110, 140, 1060, 500
    parts.append(rect(left, top, grid_w, grid_h, COLORS["card"], stroke="#E2E8F0", r=22))
    parts.append(text(left - 42, top + grid_h/2, "Verifier strength", size=17, weight="800", fill=COLORS["slate"], anchor="middle", extra='transform="rotate(-90 68 390)"'))
    parts.append(text(left + grid_w/2, top + grid_h + 58, "Environment and action realism", size=17, weight="800", fill=COLORS["slate"], anchor="middle"))
    # grid lines
    for i in range(1, 4):
        y = top + i * grid_h / 4
        parts.append(f'<line x1="{left}" y1="{y}" x2="{left+grid_w}" y2="{y}" stroke="#E2E8F0" stroke-width="1"/>')
    for i in range(1, 6):
        x = left + i * grid_w / 6
        parts.append(f'<line x1="{x}" y1="{top}" x2="{x}" y2="{top+grid_h}" stroke="#E2E8F0" stroke-width="1"/>')
    # labels
    cols = ["Text / QA", "Web", "Code", "GUI / Mobile", "Tool APIs", "Embodied"]
    for i, c in enumerate(cols):
        x = left + (i + 0.5) * grid_w / 6
        parts.append(text(x, top + grid_h + 28, c, size=14, weight="800", fill=COLORS["muted"], anchor="middle"))
    rows = ["Strong executable feedback", "State checks / judges", "Human or rubric review", "Open-world uncertain"]
    for i, r in enumerate(rows):
        y = top + (i + 0.5) * grid_h / 4
        parts.append(text(left + 18, y + 5, r, size=12, weight="700", fill=COLORS["muted"]))

    benchmarks = [
        (210, 230, "GAIA", COLORS["blue"]),
        (365, 250, "Mind2Web", COLORS["cyan"]),
        (385, 355, "WebArena", COLORS["cyan"]),
        (405, 470, "BrowseComp", COLORS["cyan"]),
        (425, 520, "BEARCUBS", COLORS["cyan"]),
        (545, 205, "SWE-bench", COLORS["teal"]),
        (570, 270, "MLAgentBench", COLORS["teal"]),
        (590, 330, "MLE-bench", COLORS["teal"]),
        (720, 260, "OSWorld", COLORS["violet"]),
        (760, 330, "AndroidWorld", COLORS["violet"]),
        (780, 410, "WorkArena", COLORS["violet"]),
        (900, 240, "tau-bench", COLORS["amber"]),
        (920, 310, "AppWorld", COLORS["amber"]),
        (945, 390, "GTA", COLORS["amber"]),
        (1080, 240, "BEHAVIOR-1K", COLORS["rose"]),
        (1035, 380, "Agent-X", COLORS["rose"]),
        (890, 520, "AgentDojo", COLORS["rose"]),
        (985, 535, "WASP", COLORS["rose"]),
        (770, 545, "AgentHarm", COLORS["rose"]),
    ]
    for x, y, label, color in benchmarks:
        tw = max(82, len(label) * 8 + 22)
        parts.append(pill(x - tw/2, y - 17, tw, 34, label, "#FFFFFF", stroke=color, txt=color, size=12))

    # legend
    parts.append(rect(210, 670, 860, 52, COLORS["card"], stroke="#E2E8F0", r=18))
    legend = [("web/search", COLORS["cyan"]), ("software", COLORS["teal"]), ("GUI/mobile", COLORS["violet"]), ("tool/API", COLORS["amber"]), ("safety/embodied", COLORS["rose"])]
    x = 240
    for lab, col in legend:
        parts.append(f'<circle cx="{x}" cy="696" r="7" fill="{col}"/>')
        parts.append(text(x + 15, 701, lab, size=13, weight="700", fill=COLORS["muted"]))
        x += 155
    parts.append('</svg>')
    (ASSETS / "benchmark-map.svg").write_text("\n".join(parts), encoding="utf-8")


def evaluation_stack():
    w, h = 1280, 760
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
             '<title id="title">Agent evaluation stack</title>',
             '<desc id="desc">A layered evaluation stack for agentic AI systems.</desc>',
             header_defs(), rect(0, 0, w, h, 'url(#bgGrad)', r=0),
             text(640, 58, "Evaluation Stack for Agentic AI", size=32, weight="900", anchor="middle"),
             text(640, 88, "Report agent results as a multi-objective profile, not only a success rate.", size=16, fill=COLORS["muted"], anchor="middle")]
    # stack cards
    layers = [
        ("Task success", "Did the agent complete the goal under the stated conditions?", COLORS["blue"], COLORS["pale_blue"]),
        ("Trajectory quality", "Were plans, tool calls, citations, and intermediate states grounded?", COLORS["teal"], COLORS["pale_teal"]),
        ("Cost and latency", "How many tokens, tool calls, retries, seconds, and dollars were used?", COLORS["violet"], COLORS["pale_violet"]),
        ("Robustness", "Does behavior survive interface drift, distractors, retries, and perturbations?", COLORS["amber"], COLORS["pale_amber"]),
        ("Safety", "Are tools least-privilege, memory governed, and untrusted inputs isolated?", COLORS["rose"], COLORS["pale_rose"]),
        ("Reproducibility", "Are prompts, model versions, scaffolds, budgets, seeds, and logs reported?", COLORS["slate"], "#F1F5F9"),
    ]
    x0, y0, width = 230, 138, 820
    heights = [60, 65, 70, 75, 80, 85]
    for i, (title, body, accent, pale) in enumerate(layers):
        y = y0 + sum(heights[:i]) + i * 10
        w_layer = width - i * 46
        x = x0 + i * 23
        parts.append(rect(x, y, w_layer, heights[i], pale, stroke=accent, r=18, sw=1.6))
        parts.append(text(x + 28, y + 36, f"{i+1}. {title}", size=18, weight="900", fill=accent))
        parts.append(text(x + 250, y + 36, body, size=13, weight="600", fill=COLORS["muted"]))
    # side checklists
    parts.append(rect(70, 176, 120, 330, COLORS["card"], stroke="#E2E8F0", r=20))
    parts.append(text(130, 214, "Inputs", size=18, weight="900", anchor="middle"))
    for j, item in enumerate(["Model", "Prompt", "Tools", "Budget", "Data", "Policy"]):
        parts.append(pill(92, 240 + j * 42, 76, 28, item, "#F8FAFC", stroke=COLORS["line"], txt=COLORS["slate"], size=12))
    parts.append(rect(1090, 176, 120, 330, COLORS["card"], stroke="#E2E8F0", r=20))
    parts.append(text(1150, 214, "Outputs", size=18, weight="900", anchor="middle"))
    for j, item in enumerate(["Score", "Cost", "Trace", "Risk", "Errors", "Logs"]):
        parts.append(pill(1112, 240 + j * 42, 76, 28, item, "#F8FAFC", stroke=COLORS["line"], txt=COLORS["slate"], size=12))
    parts.append('<path d="M190 340 L230 340" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)"/>')
    parts.append('<path d="M1050 340 L1090 340" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)"/>')
    # bottom message
    parts.append(rect(250, 665, 780, 54, COLORS["card"], stroke="#E2E8F0", r=18))
    parts.append(text(640, 700, "Recommended reporting: success + process + cost + robustness + safety + reproducibility", size=16, weight="900", fill=COLORS["ink"], anchor="middle"))
    parts.append('</svg>')
    (ASSETS / "evaluation-stack.svg").write_text("\n".join(parts), encoding="utf-8")


if __name__ == "__main__":
    agentic_landscape()
    benchmark_map()
    evaluation_stack()
    print("Wrote SVG assets to", ASSETS)
