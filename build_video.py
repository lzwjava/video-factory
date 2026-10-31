#!/usr/bin/env python3
"""Assemble announcement.mp4 (1920x1080, 30fps) from rendered slides + captions.

Per scene: zoompan motion on the slide, alpha-faded caption overlays, silent
AAC track, fade in/out. Segments are then concatenated with the demuxer.
"""

import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "output")
TMP = os.path.join(ROOT, "output", "_segments")

W, H = 1920, 1080
FPS = 30
CRF = 18

def run(cmd):
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)

def scene_command(scene, captions, seg, fade_secs=0.4):
    dur = scene["duration"]
    sid = scene["id"]
    N = round(dur * FPS)
    zoom = scene.get("zoom", "in")
    if zoom == "in":
        zexpr = f"min(1.0+0.10*on/{N},1.10)"
    else:
        zexpr = f"max(1.10-0.10*on/{N},1.0)"
    zoompan = (
        f"zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
        f"d=1:s={W}x{H}:fps={FPS}"
    )
    vf = [f"[0:v]{zoompan},"
          f"fade=t=in:st=0:d={fade_secs}:color=0x0a0a0b,"
          f"fade=t=out:st={dur-fade_secs:.2f}:d={fade_secs}:color=0x0a0a0b[v0]"]

    # caption inputs start at index 1
    caption_chain = vf
    prev = "v0"
    for i, cap in enumerate(captions):
        s, e = cap["start"], cap["end"]
        fin = f"[{prev}][cw{i}]overlay=0:0:enable='between(t,{s:.2f},{e:.2f})'[c{i}]"
        chain = f"[{i+1}:v]scale={W}:{H}:flags=lanczos,format=rgba," \
                f"fade=t=in:st={s:.2f}:d=0.22:alpha=1," \
                f"fade=t=out:st={e-0.22:.2f}:d=0.22:alpha=1[cw{i}]"
        caption_chain.append(chain)
        caption_chain.append(fin)
        prev = f"c{i}"

    inputs = ["-y", "-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.2f}",
              "-i", f"slides/scene_{sid}.png"]
    for i in range(len(captions)):
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.2f}",
                   "-i", f"slides/cap_{sid}_{i}.png"]

    # video-only segments; audio is attached once after concatenation
    cmd = ["ffmpeg"] + inputs + [
        "-filter_complex", ";".join(caption_chain),
        "-map", f"[{prev}]",
        "-c:v", "libx264", "-preset", "fast", "-crf", str(CRF),
        "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0",
        "-t", f"{dur:.2f}", seg,
    ]
    run(cmd)

def main():
    with open(os.path.join(ROOT, "scenes.json")) as f:
        data = json.load(f)
    with open(os.path.join(ROOT, "slides", "timings.json")) as f:
        timings = json.load(f)

    os.makedirs(TMP, exist_ok=True)
    segments = []
    for i, scene in enumerate(data["scenes"]):
        sid = scene["id"]
        seg = os.path.join(TMP, f"seg_{i:02d}_{sid}.mp4")
        scene_command(scene, timings[sid], seg)
        segments.append(seg)

    listf = os.path.join(TMP, "list.txt")
    with open(listf, "w") as f:
        f.writelines(f"file '{os.path.abspath(s)}'\n" for s in segments)

    out = os.path.join(OUT, "announcement.mp4")
    total = sum(s["duration"] for s in data["scenes"])
    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(TMP, "video_only.mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listf,
         "-c", "copy", tmp])
    # attach one continuous silent track (swap in your own narration later)
    run(["ffmpeg", "-y", "-i", tmp,
         "-f", "lavfi", "-t", f"{total:.2f}", "-i", "anullsrc=r=48000:cl=stereo",
         "-map", "0:v", "-map", "1:a", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-shortest",
         "-movflags", "+faststart", out])
    print(f"\nDONE → {out}  ({total:.1f}s)")

if __name__ == "__main__":
    main()
