# video-factory

Code-built announcement assets for **Truth Lab · Truth Software · lzwjava.com** (bilingual EN+中文, 16:9). No CapCut.

## Deliverables (`output/`)

| File | What |
|------|------|
| `announcement.mp4` | 1920×1080 · 30fps · 55s · silent track, captions burned in |
| `announcement.html` | Marp deck — browser view |
| `announcement.pdf` | Marp deck — print/share |
| `announcement.pptx` | Marp deck — PowerPoint |
| `previews/` | PNG thumbnails of the 6 slides |

## Source files

| File | Purpose |
|------|---------|
| `scenes.json` | Video content & timing (EN+ZH) — edit then re-render |
| `render_slides.py` | PIL: renders slide/caption PNGs (fonts: Inter, Menlo, Hiragino Sans GB) |
| `build_video.py`  | ffmpeg: zoompan motion + caption overlays + silent audio → mp4 |
| `deck.md`         | **Marp markdown deck** (the PPT, editable in any markdown editor) |
| `transcript.md`   | English narration script + WeChat/YouTube copy |
| `deliver-transcription.md` | Bilingual transcription of `deliver.m4a` (voice memo) |

## Build

```bash
# video
python3 render_slides.py && python3 build_video.py

# deck (PPT) — --allow-local-files is required for the site screenshots
marp deck.md -o output/announcement.html --allow-local-files          # HTML
marp deck.md -o output/announcement.pdf --pdf --allow-local-files     # PDF via Chrome
marp deck.md -o output/announcement.pptx --allow-local-files         # PPTX
```
