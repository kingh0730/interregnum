# FIRST DAY MIX · 《先别落地》

**AI SI - I｜普通话音乐试播片｜最终成片已导出**

[播放／下载最终MP4](../../renders/first-day-mix/first-day-mix-final.mp4) · [封面帧](../../renders/first-day-mix/first-day-mix-poster.jpg)

1920×1080，60fps，43.683秒；保留完整43.670秒原曲。22位当代AI拟人角色、1位未命名未来角色，混合生成视频、摄影、赛璐璐、纸偶、像素、版画和程序动画。最后13.333毫秒仅为帧边界的静音补齐。

最终实现、源片选段和复现入口见 [最终剪辑](production/final-cut.md)、[制作说明](production/README.md) 与 [交付记录](production/delivery.json)。以下保留前期美术阶段记录，早先“停在美术阶段”等文字描述当时的交付范围；后续最终成片以production内记录为准。

---

## 前期开发记录

也可直接阅读14页图文决策PDF：[中文版](../../output/pdf/first-day-mix-decisions-zh.pdf) / [英文版](../../output/pdf/first-day-mix-decisions.pdf)。

从 [美术提案与实图](art-review.md) 开始。九张生成测试、三种候选方向、一次白昼深化和一次夜景空间修订，选定了摄影人物 / 精密折纸机构 / 赛璐璐 / 纸偶 / 像素 / 版画的混合方向。

> 一块能站的地醒来，就多一个朋友，也少一个落脚处。大家把衣带变成共同的帆，最后接住从仅剩那块地里出生的新朋友。

## 阅读顺序

1. [原始要求](prompt.txt) — 每次上下文压缩后必须重新读。早先 First Day 尝试不作本片创作参考。
2. [故事与范围](episode.md) — 22位当代AI拟人角色，加1位未命名未来角色。
3. [美术提案](art-review.md) — 先看实图；[逐图检查](bible/test_frames.md)记录保留与淘汰理由。
4. [中文分镜](script.md) — 53个编辑单元、52个实际计划摄影镜头；[节奏图谱](development/tempo-map.md)。
5. [美术方向](bible/art_direction.md)、[造型与场景](bible/production_design.md)、[摄影](bible/cinematography.md)、[声音](bible/sound.md)。
6. [p(doom)代码研究](research/pdoom-code-study.md) — 固定源码版本、具体函数、合成与渲染机制；[梗与事实来源](research/culture-and-facts.md)。
7. [人数、地块与承重规则](continuity.md)、[技术实验](technique-plan.md)、[制作方法清单](production-methods.md)。

## 实际完成的工作

- 三个不同概念、20条可预测套路排除、独立概念评分与一轮逻辑修订。
- 研究截至2026-10-02的中文AI梗，区分有出处的梗与本片原创性格。SGI以 `SGI?` 保留歧义，不伪装成确定的技术阶段。
- 测量WAV的完整43.670秒，记录LRC的15个行锚点、信号攻击候选与节拍候选。没有声称做过听觉确认。
- 完整中文动作稿、53份单镜计划、帧时间线、23块种子片的状态账本和名字阅读区间。
- 九张通过内置image_gen完成的探索 / 修订图；最终设计参考为 `work/first-day-mix/art/c3.png` 与 `work/first-day-mix/art/c5.png`。全部提示词与文件哈希在 `build/art-prompts.json`、`build/art-assets.json`。
- 一个原创、可拖动时间的本地Canvas技术小样：[contact-study.html](build/contact-study.html)。已渲染并检查0/2/4秒静帧；它是简化机制实验，不是最终人物美术。

## 交付边界与检查

停在要求的美术阶段。没有付费视频生成、最终音乐视频、完整角色定稿或运动质量通过结论。艺术方向已选定；角色尺度、手腕接触、23槽布局、实际舞蹈和手机大小文字需要后续生产资产来验证。不能把美术测试误当作连续性放行。

图像调用消耗订阅额度；本次没有fal/API生成费用。参考仓库只作源码研究，未把它的代码、音乐或媒体移入本片。未发布、未推送；其他会话的 `.gitignore` 修改未触碰。

源数据以 `build/timeline.json`、`build/scene-state.json` 和 `build/labels.json` 为准。60fps计划2621帧，视频尾比原WAV长13.33毫秒；保留原音频，不拉伸或截短。最终镜头上的片名字是叠加，不另算一次切镜。

## 下一阶段的先后

先做核心六人的干净身份参考与23槽场景布局，再做接触变人 / 全身跳舞 / 混合媒介遮挡的代表性短测试，最后扩展成全片资产和动画。生成运动前另作当时报价；本阶段没有启动该流程。
