# Guitar introduction: code and UI audit

Reviewed 2026-11-06. The introduction is a separate static GitHub Pages site. App behavior was not changed.

## What was opened

- Opened https://timber-chord-finder.vercel.app in Ego and inspected the real C-major screen.
- Selected its C, A, G, E and D-badged voicings. Captured `site/assets/caged-{c,a,g,e,d}.png` directly from those states.
- Opened Setup, selected Major (Ionian), Full Chord Map and Interval Labels. Captured `site/assets/scale-map.png`.
- Confirmed the current interface uses walnut/bakelite panels, maple text, an italic display wordmark and mono instrument labels. The intro adopts that visual language rather than the earlier white generic layout.

## Code evidence

| Intro explanation | Owning source |
| --- | --- |
| Root, quality, slash bass, recomputation and reset behavior | `App.tsx` |
| Chord qualities/formulas, tuning presets, capo 0–12, scale intervals | `constants.ts` |
| Generated six-string voicings, note coverage, bass constraint, bounded search, span/finger heuristics | `utils/chordEngine.ts` → `generateChords` |
| Strict CAGED badges and standard-interval requirement | `utils/chordEngine.ts` → `CAGED_PATTERNS`, `identifyCAGEDShape`, `getCAGEDScore` |
| Synthetic strum and per-note sound | `utils/audioEngine.ts`; `components/Fretboard.tsx` |
| Setup controls, chord-tone map, scales, interval labels, lefty mode | `components/Controls.tsx`; `components/Fretboard.tsx` |
| Walnut/maple palette, italic branding, instrument panels | `constants.ts`; `components/Controls.tsx`; `components/Fretboard.tsx`; `index.css` |

The screenshot explorer reuses real rendered UI, not a separately recreated fretboard. Its C-major fret arrays match the app's selected variations. It is explicitly labeled recorded, not interactive playback. The full chord engine remains in the app.

## Concept research

Primary source read: [D’Addario, A Guitarist’s Guide to the CAGED System](https://www.daddario.com/en-eu/blogs/guitar/guitarists-guide-to-the-caged-system), sections “What is the CAGED System?” and “The CAGED Chord Shapes.” This supports the five named open major shapes and movable-form explanation. Page links to this source; copy is paraphrased, not copied.

App-specific details are verified in source, not attributed to the general theory article: strict recognition, tuning intervals, examples and candidate search limitations. No claim that all generated shapes are CAGED, that alternate tunings preserve these patterns, or that the app improves skill by a measured amount.

## Validation

- Standard-library Python build produces EN `/` and Chinese `/zh/`.
- Browser check: all five recorded shape buttons update the image, selected state and fret readout; each image finishes loading. English and Chinese pages load with expected titles and anchors.
- Chinese page rendered in a real 390px-wide iframe: scroll width equals390px, all images loaded. Desktop review has no horizontal overflow.
- Both language versions retain `#use` and `#start` anchors.
- No application package or lockfile changed; pre-existing `package-lock.json` changes remain outside this work.
