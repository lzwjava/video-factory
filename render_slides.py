#!/usr/bin/env python3
"""Render bilingual (EN+ZH) announcement slides + caption strips from scenes.json."""

import json, os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(ROOT, "fonts")
MONO = "/System/Library/Fonts/Menlo.ttc"

def load_scenes():
    with open(os.path.join(ROOT, "scenes.json")) as f:
        return json.load(f)

def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

def cjk(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_letterspaced(draw, pos, text, f, fill, tracking):
    x, y = pos
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking
    return x

def radial_glow(base, accent, center, radius, peak_alpha=30):
    w, h = base.size
    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    steps = 64
    cx, cy = center
    for i in range(steps, 0, -1):
        r = radius * i / steps
        a = int(peak_alpha * (steps - i) / steps)
        if a <= 0:
            continue
        col = (*accent, a)
        d.ellipse([cx - r, cy - r * 0.62, cx + r, cy + r * 0.62], fill=col)
    base.alpha_composite(ov)

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def hex_to_rgb_a(h, a=255):
    return (*hex_to_rgb(h), a)

def render_slide(scene, cfg, idx, total):
    SS = cfg["supersample"]
    W, H = cfg["width"] * SS, cfg["height"] * SS
    CJK = cfg["cjk"]
    ih = lambda v: int(H * v)
    iw = lambda v: int(W * v)
    bg = hex_to_rgb(cfg["bg"])
    accent = hex_to_rgb(scene.get("accent", cfg["accent"]))

    img = Image.new("RGBA", (W, H), (*bg, 255))
    d = ImageDraw.Draw(img)

    radial_glow(img, accent, (W * 0.5, H * 0.34), W * 0.55, peak_alpha=30)
    d.rectangle([iw(0.08), ih(0.038), iw(0.92), ih(0.038) + 2], fill=(*accent, 90))

    # kicker (top-left, letterspaced mono)
    fk = font("Inter-Medium.ttf", int(28 * SS))
    draw_letterspaced(d, (iw(0.1), ih(0.105)), scene["kicker"].upper(), fk,
                      (*accent, 255), int(8 * SS))

    # scene tag (top-right)
    tag = f"{idx:02d} / {total:02d}"
    fm = ImageFont.truetype(MONO, int(26 * SS))
    d.text((iw(0.9) - d.textlength(tag, font=fm), ih(0.105)), tag, font=fm,
           fill=hex_to_rgb_a(cfg["muted"], 220))

    # urls (top-right, below tag)
    fu = ImageFont.truetype(MONO, int(34 * SS))
    uy = ih(0.158)
    for u in scene.get("urls", []):
        d.text((iw(0.9) - d.textlength(u, font=fu), uy), u, font=fu,
               fill=(*accent, 255))
        uy += int(50 * SS)

    # title EN
    lines = scene["title_en"].split("\n")
    fsize = int(140 * SS)
    while fsize > 60:
        ft = font("Inter-ExtraBold.ttf", fsize)
        if max(d.textlength(l, font=ft) for l in lines) <= iw(0.75):
            break
        fsize -= int(8 * SS)
    ft = font("Inter-ExtraBold.ttf", fsize)
    ty = ih(0.22)
    for l in lines:
        d.text((iw(0.1), ty), l, font=ft, fill=hex_to_rgb_a(cfg["text"], 255))
        ty += int(fsize * 1.02)

    # title ZH
    fz = cjk(CJK, int(58 * SS))
    d.text((iw(0.1), ty + int(12 * SS)), scene["title_zh"], font=fz,
           fill=hex_to_rgb_a(cfg["muted"], 240))
    by = ty + int(12 * SS) + int(70 * SS) + int(26 * SS)

    # bullets EN + ZH
    fe = font("Inter-Medium.ttf", int(40 * SS))
    fz2 = cjk(CJK, int(36 * SS))
    for b in scene.get("bullets", []):
        d.text((iw(0.1), by), "—", font=fe, fill=(*accent, 255))
        d.text((iw(0.12), by), b["en"], font=fe, fill=hex_to_rgb_a(cfg["text"], 245))
        by += int(50 * SS)
        d.text((iw(0.12), by), b["zh"], font=fz2, fill=hex_to_rgb_a(cfg["muted"], 235))
        by += int(48 * SS) + int(24 * SS)

    return img

def render_caption(scene, cfg, cap):
    SS = cfg["supersample"]
    W, H = cfg["width"] * SS, cfg["height"] * SS
    CJK = cfg["cjk"]
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    accent = hex_to_rgb(scene.get("accent", cfg["accent"]))

    fe = font("Inter-Medium.ttf", int(44 * SS))   # EN
    fz = cjk(CJK, int(40 * SS))                    # ZH
    max_w = int(W * 0.82)
    en_lines = wrap(d, cap["en"], fe, max_w)
    zh_lines = wrap(d, cap["zh"], fz, max_w)
    lh_en = int(58 * SS)
    lh_zh = int(50 * SS)
    th = len(en_lines) * lh_en + len(zh_lines) * lh_zh
    pad = int(24 * SS)
    box_w = max(max(d.textlength(l, font=fe) for l in en_lines),
                max(d.textlength(l, font=fz) for l in zh_lines)) + pad * 2
    box_h = th + pad * 2
    bx = (W - box_w) / 2
    by = H - box_h - int(40 * SS)
    d.rounded_rectangle([bx, by, bx + box_w, by + box_h], radius=int(20 * SS),
                        fill=(8, 8, 12, 178), outline=(*accent, 70),
                        width=max(1, int(2 * SS)))
    ty = by + pad
    for l in en_lines:
        tw = d.textlength(l, font=fe)
        d.text(((W - tw) / 2, ty), l, font=fe, fill=hex_to_rgb_a(cfg["text"], 255))
        ty += lh_en
    for l in zh_lines:
        tw = d.textlength(l, font=fz)
        d.text(((W - tw) / 2, ty), l, font=fz, fill=hex_to_rgb_a("#cfcbbf", 235))
        ty += lh_zh
    return img

def caption_times(scene):
    dur = scene["duration"]
    caps = scene["captions"]
    W = sum(c["words"] for c in caps)
    lead, tail = 0.35, 0.5
    usable = max(dur - lead - tail, 1.0)
    specs, cur = [], lead
    for c in caps:
        span = usable * c["words"] / W
        specs.append({"start": round(cur, 2), "end": round(cur + span, 2),
                      "en": c["en"], "zh": c["zh"], "words": c["words"]})
        cur += span
    specs[-1]["end"] = round(dur - tail, 2)
    return specs

def main():
    data = load_scenes()
    cfg = dict(data["settings"])
    cfg["supersample"] = int(cfg.get("supersample", 2))
    scenes = data["scenes"]
    total = len(scenes)
    os.makedirs(os.path.join(ROOT, "slides"), exist_ok=True)
    timing_out = {}
    for i, scene in enumerate(scenes, start=1):
        render_slide(scene, cfg, i, total).save(
            os.path.join(ROOT, "slides", f"scene_{scene['id']}.png"))
        times = caption_times(scene)
        timing_out[scene["id"]] = times
        for j, t in enumerate(times):
            render_caption(scene, cfg, t).save(
                os.path.join(ROOT, "slides", f"cap_{scene['id']}_{j}.png"))
        print(f"[slides] {scene['id']}: dur={scene['duration']}s captions={len(times)}")
    with open(os.path.join(ROOT, "slides", "timings.json"), "w") as f:
        json.dump(timing_out, f, indent=2)
    print("done → slides/")

if __name__ == "__main__":
    main()
