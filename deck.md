---
marp: true
theme: default
paginate: true
backgroundColor: #0a0a0b
color: #ece9e1
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

section {
  background: radial-gradient(1200px 700px at 62% 30%, rgba(227, 179, 65, 0.10), transparent 60%), #0a0a0b;
  color: #ece9e1;
  font-family: 'Inter', 'Hiragino Sans GB', 'PingFang SC', 'Microsoft YaHei', sans-serif;
  padding: 90px 80px;
}
section::after {
  color: #5c5a52;
  font-family: 'JetBrains Mono', monospace;
  font-size: 16px;
  right: 40px; bottom: 20px;
}
h1 {
  font-size: 76px;
  font-weight: 800;
  letter-spacing: -1.5px;
  color: #ece9e1;
  border: none;
  margin: 18px 0 6px 0;
}
h2 { color: #e3b341; font-weight: 700; border: none; margin-bottom: 10px; }
.kicker {
  font-family: 'JetBrains Mono', monospace;
  font-size: 20px;
  letter-spacing: 4px;
  text-transform: uppercase;
  color: #e3b341;
  margin-bottom: 6px;
}
.zh { font-weight: 400; font-size: 42px; color: #8b887e; display: inline-block; }
ul { list-style: none; padding-left: 0; margin-top: 34px; }
li { font-size: 30px; font-weight: 500; color: #ece9e1; margin: 20px 0; }
li::before { content: "—  "; color: #e3b341; font-weight: 700; }
li .zh { font-size: 26px; display: block; margin: 6px 0 0 48px; }
.cover-title { font-size: 96px; margin-top: 120px; }
.cover-sub { margin-top: 30px; font-size: 26px; color: #8b887e; line-height: 1.7; }
.tag {
  position: absolute; top: 44px; right: 64px;
  font-family: 'JetBrains Mono', monospace; font-size: 17px; color: #5c5a52;
}
.sitechip {
  position: absolute; top: 40px; left: 80px;
  font-family: 'JetBrains Mono', monospace; font-size: 19px;
  color: #e3b341; letter-spacing: 2px;
}
.panel {
  position: absolute; left: 80px; top: 108px;
  background: rgba(8, 8, 12, 0.62);
  border-left: 4px solid #e3b341;
  padding: 34px 44px 30px;
  border-radius: 10px;
  max-width: 640px;
}
.panel h2 { font-size: 78px; margin: 0 0 10px 0; color: #ece9e1; }
.panel p { margin: 0; font-size: 34px; color: #bbb7ab; }
.gallery_slide p { display: inline-block; margin: 26px 16px 0 0; vertical-align: bottom; }
.gallery_slide img {
  width: 190px;
  height: 338px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 18px 50px rgba(0,0,0,.55);
}
</style>

<!-- _class: cover -->
# Three Projects, One Builder
<span class="zh">三个项目 · 一位建造者</span>

<div class="cover-sub">
Zhiwei Li · @lzwjava<br>
AI research &nbsp;·&nbsp; Software studio &nbsp;·&nbsp; AI-powered blog
</div>

<!-- notes: Greeting — hi I'm Zhiwei Li, I build software, train AI models, and write about both. Today I'm announcing three projects that all build on each other: an AI research lab, a software studio, and an AI-powered blog. -->

---

<!-- _class: project -->
<div class="tag">AGENDA</div>
<div class="kicker">今天的内容 · WHAT'S INSIDE</div>

# 01 · 02 · 03
<span class="zh">三个项目 · 一条线</span>

- **Truth Lab** <span class="zh">求真实验室</span> — 从零训练小模型，二手显卡，诚实的实验
- **Truth Software** <span class="zh">求真软件</span> — 40+ 交付产品，AI 原生团队
- **lzwjava.com** <span class="zh">AI 博客 · 作品集</span> — 翻译 · 朗读 · PDF/EPUB，真实数据

<!-- notes: Three projects, one builder. The lab does the research, the studio ships the products, and the blog documents everything with evidence. -->

---

<!-- _class: project -->
<div class="tag">01 / 03</div>
<div class="kicker">PROJECT 01 · AI RESEARCH LAB</div>

# Truth Lab
<span class="zh">求真实验室</span>

- Small LLMs trained from scratch <span class="zh">从零训练小型大语言模型</span>
- 52 GB home GPU cluster from used parts <span class="zh">52GB 家用显卡集群 · 二手件</span>
- Every experiment reported honestly — failures included <span class="zh">所有实验如实公开，包括失败</span>

<!-- notes: Truth Lab is a one-person AI research lab. I pretrain GPT-2-scale models from zero on real data, I resurrect second-hand datacenter GPUs — 52 GB of VRAM at home — and I publish every result honestly, including the failures. Truth through compute. -->

---

![bg brightness:0.75](assets/sites/truthlab.png)

<div class="sitechip">TRUTHLAB.CC · LIVE SITE</div>
<div class="panel">
## One lab, run in the open
Training runs · hardware bills · honest charts
</div>

<!-- notes: This is what the lab looks like online — a single-file static site, dark and typographic, with the full experiment notebook: 13+ training runs, statuses, hardware, and honest numbers. -->

---

<!-- _class: project -->
<div class="tag">02 / 03</div>
<div class="kicker">PROJECT 02 · CONSULTING STUDIO</div>

# Truth Software
<span class="zh">求真软件</span>

- 40+ products delivered & shipped <span class="zh">交付 40+ 个产品</span>
- AI-native team · 1B+ tokens a day <span class="zh">AI 原生团队 · 每日 10亿+ tokens</span>
- AI roadmap delivered in weeks, not months <span class="zh">数周交付 AI 转型方案</span>

<!-- notes: Truth Software is the consulting studio — 40+ delivered products from WeChat Mini Programs to iOS, Android and web. Today delivery runs on an AI-native pipeline: more than a billion tokens a day, dozens of custom agents, hundreds of automation scripts. -->

---

![bg brightness:0.62](assets/sites/truthsoft.png)

<div class="sitechip">TRUTHSOFT.DEV · LIVE SITE</div>
<div class="panel">
## Software, done honestly
AI transformation · teams · portfolio of delivered work
</div>

<!-- notes: truthsoft.dev presents the studio — services, AI transformation consulting, real case studies with screenshots, and a manifesto of six principles. -->

---

<!-- _class: project -->
<div class="tag">03 / 03</div>
<div class="kicker">PROJECT 03 · AI-POWERED BLOG</div>

# lzwjava.com
<span class="zh">AI 博客 · 作品集</span>

- Every post AI-translated, narrated, PDF & EPUB <span class="zh">每篇：AI 翻译 · 朗读 · PDF 与 EPUB</span>
- AI portfolio: benchmarks, hardware, training logs <span class="zh">AI 作品集：基准、硬件、训练日志</span>
- Software portfolio: a decade of shipped work <span class="zh">软件作品集：十年的交付</span>

<!-- notes: lzwjava.com is the home base — every article is machine-translated, narrated, exported to PDF and EPUB automatically. It hosts both my AI portfolio and my software portfolio, backed by benchmarks, training logs and certifications. -->

---

![bg brightness:0.62](assets/sites/blog.png)

<div class="sitechip">LZWJAVA.COM · LIVE SITE</div>
<div class="panel">
## Evidence of daily work
AI portfolio · software portfolio · 10 万月活 · 100k monthly visits
</div>

<!-- notes: The AI portfolio post shows real evidence of daily AI work — hardware, teardowns, benchmarks, certifications. The software portfolio collects a decade of shipped products across companies and partners. -->

---

<!-- _class: gallery_slide -->
<div class="tag">PORTFOLIO</div>
<div class="kicker">SOME SHIPPED WORK · 部分交付</div>

# Real products, real users
<span class="zh">真实的产品 · 真实的用户</span>

![](assets/cases/jimiao-community.jpg)
![](assets/cases/lawshare.jpg)
![](assets/cases/togo-career.jpg)
![](assets/cases/wowo-renovation.jpg)

<!-- notes: A small slice of the product gallery — community, legal, career and home-renovation apps, mostly WeChat Mini Programs, from the 40+ delivered projects in the case book. -->

---

<!-- _class: cta -->
<div class="kicker">LET'S BUILD</div>

# Build something honest.
<span class="zh">一起来，求真的创造</span>

- AI transformation? <span class="zh">AI 转型？</span> → truthlab.cc
- Software done right? <span class="zh">产品放心做？</span> → truthsoft.dev
- Follow the journey <span class="zh">关注进展</span> → lzwjava.com

<!-- notes: Everything connects. AI transformation → Truth Lab. Software done right → Truth Software. Follow along → lzwjava.com. Collaboration is token-based: tell me what to help with, pay for what's used. Let's build something honest. -->
