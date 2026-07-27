# -*- coding: utf-8 -*-
"""
Deck do processo por tras do business case "Back at the Desk" (candidatura Clara).
Identidade visual Clara: azul #1959D2, titulos Georgia (serif), corpo sans, faixa/logo.
Saida: Clara_Case_Presentation.pptx  (16:9).
"""
import pathlib
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE / "Clara_Case_Presentation.pptx"
LOGO_WHITE = str(BASE / "assets_logo_white.png")

# ---- paleta Clara
BLUE   = RGBColor(0x19, 0x59, 0xD2)
BLUE_D = RGBColor(0x12, 0x2A, 0x66)
INK    = RGBColor(0x10, 0x15, 0x2A)
T1     = RGBColor(0x81, 0xA4, 0xE6)
T2     = RGBColor(0xBA, 0xCD, 0xF2)
T3     = RGBColor(0xE3, 0xEB, 0xFA)
PANEL  = RGBColor(0xF4, 0xF6, 0xFC)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GREEN  = RGBColor(0x1E, 0x9E, 0x5B)
RED    = RGBColor(0xD6, 0x45, 0x45)
AMBER  = RGBColor(0xC9, 0x7A, 0x12)
MUTED  = RGBColor(0x5A, 0x61, 0x72)
LIGHT  = RGBColor(0xCF, 0xDC, 0xFB)

SERIF = "Georgia"
SANS = "Calibri"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
EMU = 914400


def slide():
    return prs.slides.add_slide(BLANK)


def rect(s, x, y, w, h, fill=None, line=None, line_w=1.0, shape=MSO_SHAPE.RECTANGLE, radius=None):
    sp = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    sp.shadow.inherit = False
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = Pt(line_w)
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        try:
            sp.adjustments[0] = radius
        except Exception:
            pass
    return sp


def tb(s, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    b = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = b.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0; tf.margin_right = 0
    tf.margin_top = 0; tf.margin_bottom = 0
    return tf


def para(tf, parts, size=14, color=INK, font=SANS, bold=False, align=PP_ALIGN.LEFT,
         before=0, after=6, line=1.05, first=False):
    """parts: str OR list of (text, {overrides})."""
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(before); p.space_after = Pt(after)
    try:
        p.line_spacing = line
    except Exception:
        pass
    if isinstance(parts, str):
        parts = [(parts, {})]
    for text, ov in parts:
        r = p.add_run(); r.text = text
        f = r.font
        f.size = Pt(ov.get("size", size))
        f.bold = ov.get("bold", bold)
        f.name = ov.get("font", font)
        f.color.rgb = ov.get("color", color)
    return p


def title(s, text, kicker=None):
    if kicker:
        para(tb(s, 0.75, 0.42, 11.8, 0.3), kicker.upper(), size=11, color=BLUE, bold=True,
             font=SANS, after=0, first=True)
        ty = 0.66
    else:
        ty = 0.5
    para(tb(s, 0.75, ty, 11.8, 0.75), text, size=29, color=INK, bold=True, font=SERIF,
         after=0, first=True)
    rect(s, 0.78, ty + 0.78, 0.85, 0.055, fill=BLUE)
    return ty + 1.05


def footer(s, n):
    para(tb(s, 0.75, 7.06, 4, 0.3), "CLARA", size=9.5, color=BLUE, bold=True, font=SERIF,
         after=0, first=True)
    para(tb(s, 11.4, 7.06, 1.2, 0.3), str(n), size=9.5, color=MUTED, font=SANS,
         align=PP_ALIGN.RIGHT, after=0, first=True)


def check(s, x, y, color=GREEN, mark="✓", size=15):
    para(tb(s, x, y, 0.32, 0.32), mark, size=size, color=color, bold=True, font=SANS,
         after=0, first=True)


def pill(s, x, y, w, text, fill, txt=WHITE, h=0.34, size=10.5):
    r = rect(s, x, y, w, h, fill=fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
    tf = r.text_frame; tf.word_wrap = True
    tf.margin_top = 0; tf.margin_bottom = 0; tf.margin_left = Pt(4); tf.margin_right = Pt(4)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    para(tf, text, size=size, color=txt, bold=True, font=SANS, align=PP_ALIGN.CENTER,
         after=0, first=True)
    return r


# =====================================================================
# SLIDE 1 - CAPA
# =====================================================================
s = slide()
rect(s, -0.1, -0.1, 13.6, 7.7, fill=BLUE)
rect(s, 0, 0, 13.333, 0.28, fill=BLUE_D)
rect(s, 0, 7.22, 13.333, 0.28, fill=BLUE_D)
s.shapes.add_picture(LOGO_WHITE, Inches(0.85), Inches(0.7), height=Inches(0.5))
para(tb(s, 0.9, 2.55, 11, 0.4), "DATA STORYTELLING & BRAND INSIGHTS", size=13, color=LIGHT,
     bold=True, font=SANS, after=0, first=True)
para(tb(s, 0.85, 3.05, 11.5, 1.4), "Back at the Desk", size=58, color=WHITE, bold=True,
     font=SERIF, after=0, first=True)
para(tb(s, 0.9, 4.35, 10.5, 0.6), "The process behind the business case", size=22,
     color=T3, font=SERIF, after=0, first=True)
rect(s, 0.92, 5.15, 2.3, 0.05, fill=WHITE)
para(tb(s, 0.9, 5.45, 10, 0.4), "Gabriel Croquer  ·  July 2026", size=13, color=LIGHT,
     font=SANS, after=0, first=True)

# =====================================================================
# SLIDE 2 - INITIAL CHALLENGES
# =====================================================================
s = slide()
cy = title(s, "Initial challenges: scope and creativity")
# coluna esquerda: dois desafios
lx, lw = 0.75, 6.3
b1 = tb(s, lx, cy + 0.1, lw, 1.6)
para(b1, "Narrow the scope", size=18, color=BLUE, bold=True, font=SERIF, after=3, first=True)
para(b1, "The report can't be too broad. With a base as rich as Clara's, too many strong "
        "themes compete for a single study.", size=14, color=INK, after=0, line=1.15)
b2 = tb(s, lx, cy + 1.85, lw, 1.6)
para(b2, "Avoid repeating past reports", size=18, color=BLUE, bold=True, font=SERIF,
     after=3, first=True)
para(b2, "To show creativity, the study had to open a new subject, not re-run a theme "
        "Clara already published.", size=14, color=INK, after=0, line=1.15)
# coluna direita: reports existentes
px, pw = 7.5, 5.1
rect(s, px, cy, pw, 4.35, fill=PANEL, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)
pt = tb(s, px + 0.35, cy + 0.28, pw - 0.7, 3.9)
para(pt, "Clara's published reports", size=13, color=BLUE, bold=True, font=SANS, after=8, first=True)
para(pt, [("AI theme  ", {"color": MUTED, "size": 11}),
          ("already done four times", {"color": AMBER, "bold": True, "size": 11})], after=2)
for r in ["Clara AI Report  ·  Quando a IA entra no Caixa  ·  AI Monitor"]:
    para(pt, "  " + r, size=11.5, color=INK, after=8)
para(pt, [("Strong themes still open", {"color": MUTED, "size": 11})], after=2)
for r in ["O Custo Invisível do Pré-pago",
          "El tanque que se vacía dos veces  (fleet fuel, MX)",
          "El punto ciego de los viajes corporativos  (travel, MX)",
          "Clara Radar de marcas  (2023, 1.6M transactions)"]:
    para(pt, [("•  ", {"color": BLUE, "bold": True}), (r, {})], size=11.5, color=INK, after=4)
cap = tb(s, px + 0.35, cy + 3.55, pw - 0.7, 0.7)
para(cap, "Great themes that deserve a rebranded re-edition: more proprietary data, "
         "launched in Brazil.", size=11, color=BLUE, bold=True, font=SANS, after=0, first=True, line=1.1)
footer(s, 2)

# =====================================================================
# SLIDE 3 - ON-SITE VS REMOTE
# =====================================================================
s = slide()
cy = title(s, "On-site vs remote work: the ongoing debate")
para(tb(s, 0.75, cy - 0.02, 11.8, 0.6),
     "Chosen over spend policy, which folds into the study as H5 (Ramp already owns the "
     "generic policy angle).", size=13, color=MUTED, font=SANS, after=0, first=True, line=1.15)
yy = cy + 0.85
para(tb(s, 0.75, yy, 8, 0.4), "Criteria", size=16, color=INK, bold=True, font=SERIF,
     after=0, first=True)
yy += 0.6
crit = [
    "Generates press coverage",
    "Sparks conversations on social media",
    "Positions Clara as the leading authority on corporate spending in Latin America",
]
for c in crit:
    check(s, 0.8, yy - 0.02, GREEN)
    para(tb(s, 1.25, yy, 10.8, 0.5), c, size=15, color=INK, font=SANS, after=0, first=True, line=1.1)
    yy += 0.72
footer(s, 3)

# =====================================================================
# SLIDE 4 - WHAT PERSPECTIVE
# =====================================================================
s = slide()
cy = title(s, "What perspective?")
# linha 1 - descartado
check(s, 0.8, cy + 0.05, RED, mark="✕")
r1 = tb(s, 1.25, cy, 8.3, 1.0)
para(r1, [("First angle. ", {"bold": True, "color": INK}),
          ("Use Clara's data to measure on-site work activity and attendance.", {"color": INK})],
     size=15, after=3, first=True, line=1.1)
para(r1, "Flawed, risky, complicated: Clara has no headcount, and the VR blind spot breaks "
        "the presence proxy.", size=12.5, color=MUTED, after=0, line=1.1)
pill(s, 9.75, cy + 0.02, 1.7, "DISCARDED", RED, size=11)
# linha 2 - pivo
yy = cy + 1.55
check(s, 0.8, yy + 0.05, GREEN)
r2 = tb(s, 1.25, yy, 10.6, 0.9)
para(r2, [("Pivoted back to basics. ", {"bold": True, "color": INK}),
          ("Use Clara's data to measure how much companies spend on on-site work.", {"color": INK})],
     size=15, after=0, first=True, line=1.1)
# box Clara Workplace Index
by = yy + 1.3
rect(s, 0.75, by, 11.85, 1.75, fill=PANEL, line=BLUE, line_w=1.5,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
bt = tb(s, 1.15, by + 0.28, 11, 1.3)
para(bt, "Clara Workplace Index", size=22, color=BLUE, bold=True, font=SERIF, after=6, first=True)
para(bt, [("Recurring", {"bold": True, "color": INK}),
          ("      Recurrence builds authority", {"color": MUTED})], size=14, after=0)
footer(s, 4)

# =====================================================================
# SLIDE 5 - AI WORKFLOW
# =====================================================================
s = slide()
cy = title(s, "The AI workflow")
para(tb(s, 0.75, cy - 0.02, 11.8, 0.4), "AI agent teams swarmed to deep research.",
     size=15, color=INK, font=SERIF, after=0, first=True)
# stat tiles
stats = [("10+", "agents in parallel"), ("250+", "searches & page reads"),
         ("2,849", "URLs mapped from Clara's sitemap")]
sx, sw, gap = 0.75, 3.75, 0.28
ty = cy + 0.6
for i, (num, lab) in enumerate(stats):
    x = sx + i * (sw + gap)
    rect(s, x, ty, sw, 1.15, fill=BLUE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
    tfp = tb(s, x + 0.25, ty + 0.14, sw - 0.5, 0.95, anchor=MSO_ANCHOR.MIDDLE)
    para(tfp, num, size=30, color=WHITE, bold=True, font=SERIF, after=0, first=True)
    para(tfp, lab, size=11.5, color=LIGHT, font=SANS, after=0, line=1.0)
# bullets
yy = ty + 1.5
for c in ["Locate old reports among archived pages (many were taken down; the sitemap "
          "revealed what was still live).",
          "Benchmark reports on on-site vs remote work."]:
    check(s, 0.8, yy + 0.02, BLUE)
    para(tb(s, 1.25, yy, 11.0, 0.6), c, size=13.5, color=INK, font=SANS, after=0, first=True, line=1.1)
    yy += 0.62
# caveat
cby = yy + 0.15
rect(s, 0.75, cby, 11.85, 1.15, fill=RGBColor(0xFB, 0xF3, 0xE4), line=AMBER, line_w=1.25,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
ct = tb(s, 1.15, cby + 0.18, 11.1, 0.85, anchor=MSO_ANCHOR.MIDDLE)
para(ct, [("Although AI can do it faster, it can't do it smarter. ", {"bold": True, "color": INK, "size": 14}),
          ("It reads snippets of archived pages and reports them as if seen. Rule adopted: a "
           "number counts only when opened at its primary source. A snippet is a lead, not a source.",
           {"color": INK, "size": 12.5})], after=0, first=True, line=1.12)
footer(s, 5)

# =====================================================================
# SLIDE 6 - HYPOTHESES (lista)
# =====================================================================
s = slide()
cy = title(s, "Defining and sharpening the hypotheses")
para(tb(s, 0.75, cy - 0.02, 11.8, 0.4),
     "Conservative by instinct: 4 of 5 provable on Clara's data alone. External sources "
     "reinforce, they don't prove.", size=13, color=MUTED, font=SANS, after=0, first=True, line=1.1)
hyps = [
    ("H1", "The office is going on-demand", True),
    ("H2", "What it costs to run an office now", True),
    ("H3", "The office runs three days", True),
    ("H4", "Companies pay for more office than they use", False),
    ("H5", "A spend policy is the lever that works on office cost", True),
]
yy = cy + 0.65
for code, name, internal in hyps:
    rect(s, 0.75, yy, 11.85, 0.82, fill=PANEL, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
    cbox = rect(s, 0.95, yy + 0.16, 0.75, 0.5, fill=BLUE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.2)
    ctf = cbox.text_frame; ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
    para(ctf, code, size=15, color=WHITE, bold=True, font=SERIF, align=PP_ALIGN.CENTER, after=0, first=True)
    para(tb(s, 1.95, yy + 0.16, 7.4, 0.55, anchor=MSO_ANCHOR.MIDDLE), name, size=15, color=INK,
         bold=True, font=SANS, after=0, first=True)
    if internal:
        pill(s, 9.7, yy + 0.22, 2.7, "PROVABLE ON INTERNAL DATA", GREEN, size=9.5, h=0.38)
    else:
        pill(s, 9.7, yy + 0.22, 2.7, "NEEDS EXTERNAL SUPPORT", AMBER, size=9.5, h=0.38)
    yy += 0.94
footer(s, 6)

# =====================================================================
# SLIDE 7 - HYPOTHESES (venn)
# =====================================================================
s = slide()
cy = title(s, "Defining and sharpening the hypotheses")
para(tb(s, 0.75, cy - 0.02, 11.8, 0.55),
     "Journalist's instinct: chase the controversy, but never expose a client, and hand "
     "CFOs something usable.", size=13, color=MUTED, font=SANS, after=0, first=True, line=1.1)
# dois circulos que de fato se cruzam (Venn real)
cyv = cy + 0.45
R = 3.75
rect(s, 2.85, cyv, R, R, fill=T3, line=BLUE, line_w=2.25, shape=MSO_SHAPE.OVAL)
rect(s, 5.15, cyv, R, R, fill=None, line=GREEN, line_w=2.25, shape=MSO_SHAPE.OVAL)
# labels nas partes que nao se cruzam
para(tb(s, 2.95, cyv + 1.05, 2.0, 1.65, anchor=MSO_ANCHOR.MIDDLE),
     "Serving, helping & prospecting clients", size=13, color=BLUE_D, bold=True, font=SANS,
     align=PP_ALIGN.CENTER, after=0, first=True, line=1.1)
para(tb(s, 6.75, cyv + 1.05, 2.0, 1.65, anchor=MSO_ANCHOR.MIDDLE),
     "Sparking conversation, public interest", size=13, color=GREEN, bold=True, font=SANS,
     align=PP_ALIGN.CENTER, after=0, first=True, line=1.1)
# lente verde na interseccao
lens = rect(s, 5.1, cyv + 0.6, 1.55, 2.55, fill=GREEN, shape=MSO_SHAPE.OVAL)
ltf = lens.text_frame; ltf.vertical_anchor = MSO_ANCHOR.MIDDLE; ltf.word_wrap = True
ltf.margin_left = Pt(2); ltf.margin_right = Pt(2)
para(ltf, "The 5 hypotheses live here", size=11, color=WHITE, bold=True, font=SANS,
     align=PP_ALIGN.CENTER, after=0, first=True, line=1.05)
footer(s, 7)

# =====================================================================
# SLIDE 8 - CHOSEN HEADLINE + CHANNELS
# =====================================================================
s = slide()
cy = title(s, "Chosen headline")
# manchete centralizada
rect(s, 0.75, cy, 11.85, 1.15, fill=BLUE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
htf = tb(s, 1.1, cy + 0.12, 11.15, 0.95, anchor=MSO_ANCHOR.MIDDLE)
para(htf, "“The five-day office is losing its lease: X% of LatAm companies' workplace "
          "spend is now flexible”", size=17, color=WHITE, bold=True, font=SERIF,
     align=PP_ALIGN.CENTER, after=0, first=True, line=1.1)
# coluna esquerda: por que
colY = cy + 1.45
para(tb(s, 0.75, colY, 5.4, 0.35), "Why this headline", size=14, color=BLUE, bold=True,
     font=SANS, after=0, first=True)
yy = colY + 0.5
for c in ["Provable on internal data", "Sparks conversation",
          "Positions Clara as an authority",
          "Converges with H4 (companies pay for more office than they use)"]:
    check(s, 0.8, yy - 0.02, GREEN, size=13)
    para(tb(s, 1.2, yy, 5.0, 0.6), c, size=12.5, color=INK, font=SANS, after=0, first=True, line=1.05)
    yy += 0.56
# coluna direita: canais
para(tb(s, 6.7, colY, 5.9, 0.35), "Adapting to each channel", size=14, color=BLUE, bold=True,
     font=SANS, after=0, first=True)
ch = tb(s, 6.7, colY + 0.5, 5.9, 3.2)
para(ch, [("Tier-1 media story. ", {"bold": True, "color": INK}),
          ("Reporters' WhatsApp is flooded with pitches; lead with a short lede and research "
           "what they actually cover.", {"color": INK})], size=12.5, after=8, first=True, line=1.1)
para(ch, [("LinkedIn. ", {"bold": True, "color": INK}),
          ("The visualization does the communicating.", {"color": INK})], size=12.5, after=8, line=1.1)
para(ch, [("Clara's owned channels. ", {"bold": True, "color": INK}),
          ("Readers want detail and numbers; fewer limits, they arrive with time to read.",
           {"color": INK})], size=12.5, after=0, line=1.1)
footer(s, 8)

# =====================================================================
# SLIDE 9 - METHODS AND LIMITS
# =====================================================================
s = slide()
cy = title(s, "Methods and limits")
items = [
    ("Proxy, not attendance", "Spending is a trace of office activity, not a count of people."),
    ("Fixed cohort", "Every time series runs on a fixed cohort of companies."),
    ("External data labeled", "Vacancy, rent and utilization are always labeled by source."),
    ("Privacy", "Minimum cell size, no cut below 30 companies. We never expose a client."),
]
yy = cy + 0.15
for lab, body in items:
    rect(s, 0.78, yy + 0.05, 0.14, 0.62, fill=BLUE)
    it = tb(s, 1.2, yy, 11.2, 0.9)
    para(it, [(lab + ". ", {"bold": True, "color": BLUE, "size": 15}),
              (body, {"color": INK, "size": 14})], after=0, first=True, line=1.1)
    yy += 1.02
footer(s, 9)

prs.save(str(OUT))
print("OK ->", OUT)
print("slides:", len(prs.slides._sldIdLst))
