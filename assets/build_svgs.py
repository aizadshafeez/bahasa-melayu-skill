# Builds the README images in light and dark versions. Run: python3 assets/build_svgs.py
import os
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
THEMES = {
    "light": dict(bg="#f6f7f5", card="#ffffff", ink="#16201f", muted="#5f6b68", line="#dfe4e2",
                  accent="#0b6b66", good="#e3f2f0", bad="#f3eeee", badmark="#a8322a"),
    "dark":  dict(bg="#0e1413", card="#161f1e", ink="#e6ecea", muted="#97a4a1", line="#25302e",
                  accent="#5ccfc4", good="#13302d", bad="#2a1f1f", badmark="#ff8f85"),
}

def text(x, y, s, size, fill, weight=400, anchor="start", italic=False):
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}>{escape(s)}</text>')

def bubble(x, y, w, lines, fill, ink, size=21, lh=31, pad=22, label=None, labelfill=None, mark=None):
    h = pad * 2 + lh * len(lines) - (lh - size) + (30 if label else 0)
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}"/>']
    ty = y + pad + size - 3
    if label:
        out.append(text(x + pad, ty, label, 15, labelfill, 700))
        if mark:
            out.append(text(x + w - pad, ty, mark, 15, labelfill, 700, "end"))
        ty += 30
    for ln in lines:
        out.append(text(x + pad, ty, ln, size, ink))
        ty += lh
    return "\n".join(out), h

def banner(t):
    W, H = 1200, 320
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="bahasa-melayu: an agent skill for natural Malaysian Malay">',
         f'<rect width="{W}" height="{H}" rx="20" fill="{t["bg"]}"/>',
         text(64, 96, "AGENT SKILL  ·  MIT", 14, t["accent"], 700),
         text(64, 160, "bahasa-melayu", 58, t["ink"], 750),
         text(64, 206, "Malay that sounds like a Malaysian wrote it.", 22, t["ink"]),
         text(64, 244, "Baku (DBP)  ·  Pasar  ·  Malay humanizer", 16, t["muted"])]
    b1, h1 = bubble(640, 48, 496, ["Kami memohon maaf atas sebarang kesulitan", "yang dialami. Pesanan anda dijangka tiba esok."],
                    t["bad"], t["muted"], size=18, lh=27, label="TYPICAL AI", labelfill=t["badmark"], mark="✕")
    b2, _ = bubble(640, 48 + h1 + 16, 496, ["Maaf cik, saya dah check. Parcel tersangkut", "kat hub, esok sampai ye."],
                   t["good"], t["ink"], size=18, lh=27, label="WITH THE SKILL", labelfill=t["accent"], mark="✓")
    p += [b1, b2, "</svg>"]
    return "\n".join(p)

def case(t):
    W, H = 1200, 0
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="Same model, same request: a customer complaint reply without and with the skill">',
         f'<rect width="{W}" height="{H}" rx="20" fill="{t["bg"]}"/>',
         text(56, 64, "SAME MODEL, SAME REQUEST", 14, t["accent"], 700),
         text(56, 108, "Customer: “Order saya 5 hari tak sampai lagi. Ni scam ke?”", 28, t["ink"], 650)]
    left = ["Salam, maaf sangat atas kelewatan ni. Bukan", "scam ya. Saya dah semak tracking, parcel",
            "tersangkut di hub Pos Laju Shah Alam.", "Dijangka sampai esok. Kalau esok masih tak", "sampai, saya refund caj pos tu."]
    right = ["Maaf cik, bukan scam ye. Saya dah check,", "parcel cik tersangkut kat hub Pos Laju",
             "Shah Alam. Sepatutnya esok sampai. Kalau", "esok tak sampai juga, saya refund kos pos."]
    b1, h1 = bubble(56, 140, 532, left, t["card"], t["ink"], label="WITHOUT THE SKILL", labelfill=t["muted"])
    b2, h2 = bubble(612, 140, 532, right, t["card"], t["ink"], label="WITH THE SKILL", labelfill=t["accent"])
    p += [f'<rect x="56" y="140" width="532" height="{h1}" rx="16" fill="none" stroke="{t["line"]}"/>', b1,
          f'<rect x="612" y="140" width="532" height="{h2}" rx="16" fill="none" stroke="{t["accent"]}" stroke-width="2"/>', b2]
    y = 140 + max(h1, h2) + 44
    notes_l = ["“Dijangka sampai esok”: notice-board passive", "“di hub”, “semak”: written Malay, not chat"]
    notes_r = ["Talks to the customer: “cik”", "Chat wording: “kat”, “check”, “sepatutnya”"]
    for i, (a, b) in enumerate(zip(notes_l, notes_r)):
        p.append(text(56, y + i * 34, "✕  " + a, 19, t["badmark"]))
        p.append(text(612, y + i * 34, "✓  " + b, 19, t["accent"]))
    H = y + 34 + 36
    p[0] = p[0].replace('height="0" viewBox="0 0 1200 0"', f'height="{H}" viewBox="0 0 1200 {H}"')
    p[1] = p[1].replace('height="0"', f'height="{H}"')
    p.append("</svg>")
    return "\n".join(p)

for name, fn in [("banner", banner), ("case-study", case)]:
    for theme, t in THEMES.items():
        with open(os.path.join(HERE, f"{name}-{theme}.svg"), "w") as f:
            f.write(fn(t))
print("ok")
