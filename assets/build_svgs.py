# Builds the README images in light and dark versions. Run: python3 assets/build_svgs.py
# Look: the aizadshafeez.com style (deep teal, Cairo, Instrument Serif italic). Both fonts are
# SIL OFL and embedded in each SVG, so GitHub shows them without any web font request.
import base64
import os
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")


def font64(name):
    with open(os.path.join(FONTS, name), "rb") as f:
        return base64.b64encode(f.read()).decode()


STYLE = (
    "<style>"
    "@font-face{font-family:'Cairo';src:url(data:font/woff2;base64,%s) format('woff2');font-weight:200 1000}"
    "@font-face{font-family:'Instrument Serif';src:url(data:font/woff2;base64,%s) format('woff2');font-style:italic}"
    "text{font-family:'Cairo','Segoe UI',Helvetica,Arial,sans-serif}"
    ".serif{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400}"
    "</style>"
) % (font64("cairo-latin-variable.woff2"), font64("instrument-serif-latin-400-italic.woff2"))

THEMES = {
    "light": dict(bg="#f6f7f5", card="#ffffff", subtle="#eef1ee", ink="#151417", muted="#5f6662", line="#dfe3df",
                  accent="#0b6b66", accent_ink="#ffffff", wash="#e3efed", withbg="#edf5f3", tie="#c6cdc8",
                  loss="#b4432f", losswash="#f6e9e6", band="#ebf2f0"),
    "dark": dict(bg="#101313", card="#181c1c", subtle="#1f2424", ink="#eef1ef", muted="#a3abaa", line="#2a3030",
                 accent="#5ccfc4", accent_ink="#062220", wash="#173533", withbg="#16292a", tie="#3a4343",
                 loss="#f08a74", losswash="#3a2420", band="#142120"),
}

# The 20 blind requests: label, the author's result for the skill, the AI judge's (won / tie / lost).
# Order matches tests/blind-20. The author's verdicts lead; the AI judge is the second opinion.
BLIND = [
    ("MC message to my boss", "won", "lost"), ("Balik kampung, to my mum", "tie", "tie"),
    ("Nudge a friend about RM200", "won", "tie"), ("Instagram caption, Cameron", "tie", "won"),
    ("Office group: meeting moved", "won", "won"), ("Shop listing translation", "tie", "tie"),
    ("Seller DM about COD", "tie", "tie"), ("Email to HR: leave balance", "tie", "tie"),
    ("Wedding invite to colleagues", "won", "won"), ("Condolence to a colleague", "won", "won"),
    ("Stuck in traffic, to my wife", "won", "won"), ("Family group: the kenduri", "won", "tie"),
    ("Home bakery Telegram post", "tie", "tie"), ("App UI strings", "tie", "tie"),
    ("Landlord: leaking pipe", "tie", "tie"), ("Reply to a recruiter", "tie", "won"),
    ("Thank-you to a teacher", "tie", "tie"), ("Cancel dinner, sick toddler", "won", "tie"),
    ("Threads: my first rendang", "tie", "won"), ("Letter to the headmaster", "tie", "won"),
]


def text(x, y, s, size, fill, weight=400, anchor="start", cls="", spacing=0):
    c = f' class="{cls}"' if cls else ""
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{ls}{c}>{escape(s)}</text>')


def marked(x, y, line, size, t, mark):
    import re
    parts = re.split(r"\[\[(.+?)\]\]", line)
    spans = []
    for i, part in enumerate(parts):
        if not part:
            continue
        if i % 2:
            spans.append(f'<tspan fill="{mark}" font-weight="700">{escape(part)}</tspan>')
        else:
            spans.append(escape(part))
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="450" fill="{t["ink"]}">{"".join(spans)}</text>'


def head(w, h, label, t):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="{escape(label)}">', STYLE, f'<rect width="{w}" height="{h}" rx="22" fill="{t["bg"]}"/>']


def pane(x, y, w, lines, t, *, label, chip=None, kind="without", size=19, lh=29):
    """A side of the comparison: a labelled card with a chat bubble inside."""
    pad = 22
    bub_h = 20 + lh * len(lines)
    h = pad + 26 + bub_h + pad
    if kind == "with":
        out = [f'<rect x="{x - 4}" y="{y - 4}" width="{w + 8}" height="{h + 8}" rx="22" fill="{t["wash"]}"/>',
               f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{t["card"]}" stroke="{t["accent"]}" stroke-width="2"/>']
        lab, bub, bline = t["accent"], t["withbg"], t["wash"]
    else:
        out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{t["subtle"]}" stroke="{t["line"]}" stroke-width="1.5"/>']
        lab, bub, bline = t["muted"], t["card"], t["line"]
    out.append(text(x + pad, y + pad + 12, label, 13, lab, 700, spacing=1.6))
    if chip:
        cw = 14 + 7.6 * len(chip)
        out += [f'<rect x="{x + w - pad - cw}" y="{y + pad - 4}" width="{cw}" height="22" rx="11" fill="{t["accent"]}"/>',
                text(x + w - pad - cw / 2, y + pad + 11, chip, 11.5, t["accent_ink"], 700, "middle", spacing=0.8)]
    by = y + pad + 26
    out.append(f'<rect x="{x + pad}" y="{by}" width="{w - 2 * pad}" height="{bub_h}" rx="14" fill="{bub}" stroke="{bline}"/>')
    ty = by + 10 + lh - 8
    for ln in lines:
        out.append(marked(x + pad + 14, ty, ln, size, t, t["accent"] if kind == "with" else t["loss"]))
        ty += lh
    return out, h


def banner(t):
    W, H = 1200, 346
    p = head(W, H, "bahasa-melayu: an agent skill for natural Malaysian Malay", t)
    p += [text(64, 100, "AGENT SKILL  ·  CLAUDE CODE  ·  CODEX  ·  MIT", 13, t["accent"], 700, spacing=1.8),
          text(60, 176, "bahasa-melayu", 66, t["ink"], 300, spacing=-2),
          text(64, 224, "Malay that sounds like a", 28, t["ink"], 350),
          text(64, 260, "Malaysian wrote it.", 30, t["accent"], cls="serif"),
          text(64, 298, "Baku (DBP)  ·  Basahan  ·  a Malay humanizer pass", 16, t["muted"], 500)]
    a, h1 = pane(640, 28, 500, ["Pesanan [[anda dijangka tiba]] esok.", "[[Kami memohon maaf atas kesulitan.]]"], t,
                 label="TYPICAL AI", size=17, lh=26)
    b, _ = pane(640, 28 + h1 + 18, 500, ["Maaf [[cik]], saya dah check. Parcel", "tersangkut kat hub, [[esok sampai ye.]]"], t,
                label="WITH THE SKILL", chip="SOUNDS HUMAN", kind="with", size=17, lh=26)
    p += a + b + ["</svg>"]
    return "\n".join(p)


def case(t):
    W = 1200
    left = ["Salam, maaf sangat atas kelewatan ni. Bukan", "scam ya. Saya dah semak tracking, parcel",
            "tersangkut di hub Pos Laju Shah Alam.", "[[Dijangka sampai esok.]] Kalau esok masih tak", "sampai, saya refund caj pos tu."]
    right = ["Maaf [[cik]], bukan scam ye. Saya dah check,", "parcel [[cik]] tersangkut kat hub Pos Laju",
             "Shah Alam. [[Sepatutnya esok sampai.]] Kalau", "esok tak sampai juga, saya refund kos pos."]
    a, h1 = pane(56, 168, 520, left, t, label="WITHOUT THE SKILL")
    b, h2 = pane(624, 168, 520, right, t, label="WITH THE SKILL", chip="SKILL WINS", kind="with")
    y = 168 + max(h1, h2)
    vs_y = 168 + max(h1, h2) / 2
    H = y + 150
    p = head(W, H, "Same model, same request: a customer complaint reply without and with the skill", t)
    p += [text(56, 70, "SAME MODEL  ·  SAME REQUEST", 13, t["accent"], 700, spacing=1.8),
          text(56, 112, "Customer: “Order saya 5 hari tak sampai lagi.", 28, t["ink"], 450, spacing=-0.4),
          text(56, 146, "Ni scam ke?”", 28, t["ink"], 450, spacing=-0.4),
          text(216, 146, "Two replies.", 28, t["accent"], cls="serif")]
    p += a + b
    p += [f'<circle cx="600" cy="{vs_y}" r="22" fill="{t["ink"]}" stroke="{t["bg"]}" stroke-width="6"/>',
          text(600, vs_y + 7, "vs", 20, t["bg"], cls="serif", anchor="middle")]
    p.append(f'<line x1="56" y1="{y + 40}" x2="1144" y2="{y + 40}" stroke="{t["line"]}" stroke-dasharray="4 5"/>')
    notes = [("“Dijangka sampai esok” is a notice-board passive", "It talks to the customer: “cik”"),
             ("“di hub”, “semak”: written Malay, not chat", "Chat wording: “kat”, “check”, “sepatutnya”")]
    for i, (l, r) in enumerate(notes):
        yy = y + 80 + i * 34
        p += [f'<circle cx="66" cy="{yy - 6}" r="9" fill="{t["losswash"]}"/>', text(66, yy - 1.5, "!", 12, t["loss"], 800, "middle"),
              text(84, yy, l, 18, t["loss"], 500),
              f'<circle cx="634" cy="{yy - 6}" r="9" fill="{t["accent"]}"/>', text(634, yy - 1.5, "✓", 11, t["accent_ink"], 800, "middle"),
              text(652, yy, r, 18, t["accent"], 600)]
    p.append("</svg>")
    return "\n".join(p)


def blind(t):
    W = 1200
    count = lambda col, k: sum(1 for r in BLIND if r[col] == k)
    won, tie, lost = count(1, "won"), count(1, "tie"), count(1, "lost")
    ai = (count(2, "won"), count(2, "tie"), count(2, "lost"))
    agree = sum(1 for r in BLIND if r[1] == r[2])
    rows_top = 318
    row_h = 46
    H = rows_top + row_h * 10 + 64
    p = head(W, H, f"Blind test of 20 requests. Author: skill won {won}, tied {tie}, lost {lost}. AI judge: won {ai[0]}, tied {ai[1]}, lost {ai[2]}", t)
    p += [f'<path d="M0 22A22 22 0 0 1 22 0H{W - 22}A22 22 0 0 1 {W} 22V262H0Z" fill="{t["band"]}"/>',
          text(56, 70, f"BLIND TEST  ·  {len(BLIND)} EVERYDAY REQUESTS  ·  TWO JUDGES", 13, t["accent"], 700, spacing=1.8),
          text(56, 126, "With the skill vs", 44, t["ink"], 300, spacing=-1.2),
          text(326, 126, "without it.", 46, t["accent"], cls="serif"),
          text(56, 168, "Claude Opus 5.5, the same requests twice: once plain, once with the skill.", 17, t["muted"], 500),
          text(56, 194, "Each pair shuffled into A and B. Judged blind by the author, a native", 17, t["muted"], 500),
          text(56, 220, "KL speaker, and separately by an AI judge. Outputs unedited.", 17, t["muted"], 500)]
    p.append(text(760, 40, "THE AUTHOR, BLIND", 11.5, t["muted"], 700, spacing=1.4))
    tiles = [(won, "SKILL WON", t["accent"], t["accent_ink"]), (tie, "TIED", t["subtle"], t["ink"]),
             (lost, "SKILL LOST", t["losswash"] if lost else t["subtle"], t["loss"] if lost else t["ink"])]
    for i, (n, lab, bg, ink) in enumerate(tiles):
        x = 760 + i * 132
        p += [f'<rect x="{x}" y="52" width="120" height="104" rx="16" fill="{bg}"/>',
              text(x + 16, 112, str(n), 52, ink, 250, spacing=-2), text(x + 16, 140, lab, 11.5, ink, 700, spacing=1.2)]
    seg = (384 - 19 * 3) / 20
    for i, r in enumerate(sorted(BLIND, key=lambda r: {"won": 0, "tie": 1, "lost": 2}[r[1]])):
        fill = t["accent"] if r[1] == "won" else t["loss"] if r[1] == "lost" else t["tie"]
        p.append(f'<rect x="{760 + i * (seg + 3):.1f}" y="172" width="{seg:.1f}" height="12" rx="3" fill="{fill}"/>')
    p += [text(760, 208, "Never worse" if not lost else f"Worse {lost}x", 14, t["muted"], 600),
          f'<line x1="760" y1="222" x2="1144" y2="222" stroke="{t["line"]}" stroke-dasharray="4 5"/>',
          text(760, 246, "AI JUDGE, BLIND", 11.5, t["muted"], 700, spacing=1.4),
          text(1144, 246, f"{ai[0]} won · {ai[1]} tied · {ai[2]} lost", 15, t["ink"], 600, "end")]
    look = {"won": ("Won", t["accent"], t["accent_ink"]), "tie": ("Tie", t["subtle"], t["muted"]),
            "lost": ("Lost", t["loss"], "#ffffff")}
    for col in range(2):
        x = 56 + col * 556
        p += [text(x + 532 - 128, rows_top - 30, "AUTHOR", 10.5, t["muted"], 700, "middle", spacing=1.2),
              text(x + 532 - 38, rows_top - 30, "AI", 10.5, t["muted"], 700, "middle", spacing=1.2)]
    for i, (label, mine, judge) in enumerate(BLIND):
        col, row = divmod(i, 10)
        x = 56 + col * 556
        y = rows_top + row * row_h
        if row == 0:
            p.append(f'<line x1="{x}" y1="{y - 22}" x2="{x + 532}" y2="{y - 22}" stroke="{t["line"]}"/>')
        p += [text(x, y + 6, f"{i + 1:02d}", 15, t["muted"], 600),
              text(x + 40, y + 6, label, 18.5, t["ink"], 600 if mine == "won" else 500)]
        name, bg, ink = look[mine]
        p += [f'<rect x="{x + 532 - 164}" y="{y - 12}" width="72" height="26" rx="13" fill="{bg}"/>',
              text(x + 532 - 128, y + 5.5, name, 13, ink, 700, "middle")]
        name, bg, ink = look[judge]
        edge = t["accent"] if judge == "won" else t["loss"] if judge == "lost" else t["line"]
        p += [f'<rect x="{x + 532 - 70}" y="{y - 11}" width="64" height="24" rx="12" fill="none" stroke="{edge}" stroke-width="1.5"/>',
              text(x + 532 - 38, y + 5, name, 12, edge if judge != "tie" else t["muted"], 700, "middle")]
        if mine != judge:
            p.append(f'<circle cx="{x + 532 - 186}" cy="{y + 1}" r="4" fill="{t["muted"]}"/>')
        p.append(f'<line x1="{x}" y1="{y + 24}" x2="{x + 532}" y2="{y + 24}" stroke="{t["line"]}"/>')
    p.append(text(56, H - 26, f"The judges agreed on {agree} of 20 (a dot marks the rest). Everything is in tests/blind-20/.", 15, t["muted"], 600))
    p.append("</svg>")
    return "\n".join(p)


for name, fn in [("banner", banner), ("case-study", case), ("blind-test", blind)]:
    for theme, t in THEMES.items():
        with open(os.path.join(HERE, f"{name}-{theme}.svg"), "w") as f:
            f.write(fn(t))
print("ok")
