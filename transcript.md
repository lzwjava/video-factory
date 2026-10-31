# Announcement Video — Transcript (English)

**Presenter:** Zhiwei Li (lzwjava)
**Projects announced:** [Truth Lab](https://truthlab.cc) · [Truth Software](https://truthsoft.dev) · [Blog / Portfolio](https://lzwjava.com)
**Format:** 16:9 · 1920×1080 (YouTube-ready; also accepted by WeChat Channels)
**Length:** ~0:55 · **Slides: bilingual EN + 中文** · Silent track, captions burned in

---

## Full narration script

**[SCENE 1 — INTRO · 0:00–0:14]**

> Hi, I'm Zhiwei Li — I build software, train AI models, and write about both.
> Three projects I want to show you today: an AI research lab, a software studio, and an AI-powered blog.

**[SCENE 2 — TRUTH LAB · 0:14–0:42]**

> First — Truth Lab, my one-person AI research lab.
> I pretrain small language models from scratch, on billions of tokens from the open web and SEC filings.
> I serve open models, resurrect second-hand GPUs, and publish every experiment honestly — failures included.
> Total home GPU memory: fifty-two gigabytes. Come see the numbers — truthlab.cc.

**[SCENE 3 — TRUTH SOFTWARE · 0:42–1:08]**

> Second — Truth Software, the studio behind forty-plus delivered products.
> WeChat mini programs, iOS and Android apps, and web platforms.
> Today the team runs AI-native — a billion tokens a day, dozens of custom agents, hundreds of automation scripts.
> Need a product built, or an AI roadmap in weeks, not months? Head to truthsoft.dev.

**[SCENE 4 — BLOG & PORTFOLIO · 1:08–1:26]**

> Third — my home base, lzwjava.com.
> An AI-powered blog: every article machine-translated, narrated, and published as audio, PDF, and EPUB.
> It also hosts my AI portfolio and my software portfolio — benchmarks, training logs, certifications.

**[SCENE 5 — CTA · 1:26–1:44]**

> Everything connects. AI transformation? Truth Lab. Software done right? Truth Software.
> Follow the journey on the blog — links in the description. Let's build something honest.

---

## Publication copy

### WeChat Channels 视频号 (short description)

> 做了三个项目，一起告诉你。AI 研究实验室 Truth Lab、软件咨询 Truth Software、AI 博客 lzwjava.com。求真的工程师，正在路上。🔥
> #AI #LLM #软件开发 #技术博客 #独立开发者

### YouTube description

> Three projects, one builder — Truth Lab, Truth Software, and an AI-powered blog.
> 
> 🔬 **Truth Lab** — one-person AI research lab: https://truthlab.cc
> 🛠️ **Truth Software** — consulting studio: https://truthsoft.dev
> 📝 **Blog & Portfolios**: https://lzwjava.com · https://lzwjava.com/ai-portfolio-en · https://lzwjava.com/portfolio-en
> 
> 0:00 Intro
> 0:14 Truth Lab
> 0:42 Truth Software
> 1:08 Blog & Portfolio
> 1:26 Build something honest
> 
> Tags: AI, LLM, GPT-2 pretraining, software consulting, indie developer, WeChat mini program, AI transformation

---

## Video build notes

- Video is **silent** (no TTS) — add your own voiceover if needed.
- The shipped video is a **short bilingual version (~0:55)** — every slide and caption shows English + 中文, so it also works muted (WeChat auto-mute).
- The full narration above is the extended script (also transcribed from your voice memo: see `deliver-transcription.md`).
- Scene data & timings live in `scenes.json`; content is fully data-driven, edit & rebuild anytime.
- Build: `python3 render_slides.py && python3 build_video.py`
- Output: `output/announcement.mp4` (1920×1080, 30fps, h264+aac).
