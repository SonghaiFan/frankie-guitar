# Guitar intro maintenance / Guitar 介绍页维护

The intro uses the actual app's walnut, maple and instrument-panel styling. It explains current behavior separately from general CAGED theory. / 介绍页沿用应用的木质、枫木色和乐器面板风格；区分实际功能与通用 CAGED 理论。

## Content and source map / 内容与来源

- `project.json` → `content.en` / `content.zh`: independent bilingual product explanations, CAGED lesson, workflow, captions and limits. Update both when behavior changes. / 独立的双语产品说明、CAGED 解释、流程、图片说明与限制；行为变化后两种语言同步更新。
- `build.py`: standard-library renderer. Copies `site/assets/` into published `media/`, emits English `/` and Chinese `/zh/`. It no longer extracts page copy from README section positions. / 标准库构建器，不依赖 README 的段落顺序。
- `style.css`: app-derived palette and panel treatment; compare with `components/Controls.tsx`, `components/Fretboard.tsx`, `constants.ts`, `index.css`. / 应用对应的色彩与面板。
- `demo.js`: five screenshot buttons; no chord engine or audio imitation. Fret strings are stored in `build.py` and must match captures. / 五个真实截图切换按钮，不模拟和弦引擎或音频；品位数组在构建脚本中。
- `AUDIT.md`: audited behavior, source code paths, research link and inspection notes. / 行为、代码与研究记录。

## Replace assets when these screens change / 按界面变化替换素材

| Asset | Capture recipe / 采集步骤 | Source to check / 对应代码 |
| --- | --- | --- |
| `assets/caged-c.png` | C Major, Standard, capo 0, C badge: `x 3 2 0 1 0` | Controls, Fretboard, chordEngine |
| `assets/caged-a.png` | Same chord, A badge: `x 3 5 5 5 3` | Same |
| `assets/caged-g.png` | Same chord, G badge: `8 7 5 5 5 8` | Same |
| `assets/caged-e.png` | Same chord, E badge: `8 10 10 9 8 8` | Same |
| `assets/caged-d.png` | Same chord, D badge: `x x 10 12 13 12` | Same |
| `assets/scale-map.png` | Setup → Major (Ionian), Full Chord Map and Interval Labels enabled | Controls, Fretboard |
| `assets/setup.png` | Setup controls visible; no open menus | Controls |

Capture real settled UI at a consistent viewport (current five-shape captures: 1468×1247). Confirm the selected voicing and matching screenshot before saving. If engine ranking changes, select the matching badge/fret string, not a hardcoded index. / 保持相同视口采集真实、稳定界面；排名变化后按字母标记与品位数组定位，不按列表下标。

The hero uses `caged-c.png`. The CAGED demo uses all five captures. The gallery uses `scale-map.png` and `setup.png`. Older `chord.png`, `voicing.png`, `demo.gif` remain as source assets but are not shown by this introduction. / 主图、五形状演示、设置画廊分别使用上述文件；旧素材仍保留，不在新介绍页显示。

When CAGED recognition changes, review `CAGED_PATTERNS` and both standard-interval checks in `utils/chordEngine.ts`. Keep the distinction between shape and sounding chord, and between major-form recognition and alternate tuning generation. / 识别变化后审查模式与标准弦间音程判断；保留形状名、发声和弦和其他调弦的区别。

No credentials or personal data are needed for screenshots. Do not update README banner captures incidentally: they have their own provenance and build under `docs/readme/`. / 截图无需凭证或私人数据；README banner 的采集来源与构建独立维护。

## Build and review / 构建与检查

```sh
python3 site/build.py
python3 -m http.server 8080 --directory _site --bind 127.0.0.1
```

Open `/` and `/zh/`; verify all five buttons change the screenshot and fret readout, the selected button state, keyboard focus, images, app/source links and `#use` / `#start`. At 390px width check no horizontal overflow. / 检查双语、五按钮图像与品位同步、键盘焦点、链接及手机宽度无横向溢出。

Push only reviewed intro files to `main`. The existing Pages workflow builds `_site/`. Keep the app’s Vercel deployment separate and exclude unrelated working-tree changes. / 只推送审核过的介绍页文件，GitHub Pages 工作流发布 `_site/`；Vercel 应用部署独立，勿包含无关代码。


## Signature wordmark

Use the approved `docs/readme/assets/frankie.svg` for the intro header, copied to `media/signature.svg`. Keep the product name separate; do not replace Frankie with a typed font. Guitar tints the SVG via a CSS mask to match the instrument palette. The app uses the identical approved `public/frankie-signature.svg`. Refresh screenshots if the visible app header changes.
