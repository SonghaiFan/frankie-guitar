#!/usr/bin/env python3
"""Standalone bilingual Guitar introduction; standard library only."""
import argparse, html, json, shutil
from pathlib import Path

def esc(value): return html.escape(str(value), quote=True)

def build(repo, out):
    cfg = json.loads((repo/'site/project.json').read_text())
    out.mkdir(parents=True, exist_ok=True)
    shutil.copytree(repo/'site/assets', out/'media', dirs_exist_ok=True)
    shutil.copy(repo/'docs/readme/assets/frankie.svg', out/'media/signature.svg')
    shutil.copy(repo/'docs/readme/banner.png', out/'media/banner.png')
    for name in ('style.css', 'demo.js'): shutil.copy(repo/'site'/name, out/name)
    (out/'.nojekyll').touch()
    for lang in ('en', 'zh'):
        zh = lang == 'zh'; p = '../' if zh else './'; dest = out/'zh' if zh else out; dest.mkdir(exist_ok=True)
        c = cfg['content'][lang]
        def section(title, body, id=''): return f'<section class="section" {f"id={id}" if id else ""}><h2>{esc(title)}</h2>{body}</section>'
        features = ''.join(f'<article><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for a,b in c['features'])
        shapes = [('C','x 3 2 0 1 0'),('A','x 3 5 5 5 3'),('G','8 7 5 5 5 8'),('E','8 10 10 9 8 8'),('D','x x 10 12 13 12')]
        buttons = ''.join(f'<button type="button" class="shape" data-shape="{s.lower()}" aria-pressed="{str(i==0).lower()}" data-frets="{f}">{s}<span>{esc(c["shape_word"])}</span></button>' for i,(s,f) in enumerate(shapes))
        demo = f'''<div class="caged-copy"><p>{esc(c['caged_intro'])}</p><p>{esc(c['caged_example'])}</p></div><div class="demo-panel"><div class="demo-heading"><strong>C MAJOR</strong><span>C · E · G / 1 · 3 · 5</span></div><div class="shape-controls" aria-label="{esc(c['shape_label'])}">{buttons}</div><p id="shape-status" class="readout" aria-live="polite">C {esc(c['shape_word'])} · x 3 2 0 1 0</p><a id="shape-link" href="{p}media/caged-c.png"><img id="shape-image" src="{p}media/caged-c.png" alt="{esc(c['shape_alt'])}" loading="lazy" width="1468" height="1247"></a><p class="caption">{esc(c['demo_note'])}</p></div><p class="source-note">{esc(c['theory_source'])} <a href="https://www.daddario.com/en-eu/blogs/guitar/guitarists-guide-to-the-caged-system">D’Addario: A Guitarist’s Guide to the CAGED System ↗</a></p><aside class="note">{esc(c['caged_limit'])}</aside>'''
        steps = '<ol class="steps">'+''.join(f'<li><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for a,b in c['steps'])+'</ol>'
        gallery = '<div class="gallery">'+''.join(f'<figure><a href="{p}media/{file}"><img src="{p}media/{file}" alt="{esc(caption)}" loading="lazy"></a><figcaption>{esc(caption)}</figcaption></figure>' for file,caption in c['gallery'])+'</div>'
        runtime = f'<div class="runtime"><div><h3>{esc(c["runtime_heading"])}</h3><p>{esc(c["runtime"])}</p><pre><code>npm install\nnpm run dev</code></pre></div><div><h3>{esc(c["limits_heading"])}</h3><ul>'+''.join(f'<li>{esc(t)}</li>' for t in c['limits'])+'</ul></div></div>'
        base = f'https://github.com/{cfg["repository"]}/blob/{cfg["branch"]}/'
        page = f'''<!doctype html><html lang="{'zh-CN' if zh else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Frankie Guitar | {esc(c['title'])}</title><meta name="description" content="{esc(c['intro'])}"><meta name="theme-color" content="#120c08"><link rel="canonical" href="{cfg['pages_url']+('zh/' if zh else '')}"><link rel="alternate" hreflang="en" href="{cfg['pages_url']}"><link rel="alternate" hreflang="zh-CN" href="{cfg['pages_url']}zh/"><link rel="stylesheet" href="{p}style.css"><meta property="og:title" content="Frankie Guitar"><meta property="og:description" content="{esc(c['intro'])}"><meta property="og:type" content="website"><meta property="og:url" content="{cfg['pages_url']+('zh/' if zh else '')}"><meta property="og:image" content="{cfg['pages_url']}media/banner.png"><script src="{p}demo.js" defer></script></head><body><a class="skip" href="#main">{esc(c['skip'])}</a><header class="shell"><a class="brand" href="{p}" aria-label="Frankie Guitar"><span class="brand-signature" role="img" aria-label="Frankie"></span><span>GUITAR</span></a><nav aria-label="{esc(c['nav'])}"><a href="#caged">CAGED</a><a href="#use">{esc(c['how'])}</a><a href="https://github.com/{cfg['repository']}">GitHub</a><span class="languages"><a href="{p}" lang="en" {'aria-current="page"' if not zh else ''}>EN</a><a href="{p}zh/" lang="zh-CN" {'aria-current="page"' if zh else ''}>中文</a></span></nav></header><main id="main" class="shell"><section class="hero"><div><p class="eyebrow">{esc(c['category'])}</p><h1>{esc(c['title'])}</h1><p class="intro">{esc(c['intro'])}</p><a class="button" href="{cfg['app_url']}">{esc(c['open'])} ↗</a></div><figure class="hero-image"><img src="{p}media/caged-c.png" alt="{esc(c['hero_alt'])}" width="1468" height="1247" fetchpriority="high"><figcaption>{esc(c['hero_caption'])}</figcaption></figure></section>{section(c['features_title'], '<div class="features">'+features+'</div>')}{section(c['caged_title'],demo,'caged')}{section(c['workflow_title'],steps,'use')}{section(c['gallery_title'],gallery)}{section(c['runtime_title'],runtime,'start')}<section class="section maintenance"><h2>{esc(c['guide_title'])}</h2><p>{esc(c['guide'])}</p><a href="{base}site/GUIDE.md">{esc(c['guide_link'])} ↗</a><a href="{base}site/AUDIT.md">{esc(c['audit_link'])} ↗</a></section></main><footer class="shell"><span>Made by <a href="https://github.com/SonghaiFan">Songhai Fan</a></span><a class="signature" href="https://github.com/{cfg['repository']}"><img src="{p}media/signature.svg" width="100" height="36" alt="Frankie"></a></footer></body></html>'''
        (dest/'index.html').write_text(page)
    print(out)
if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',default='_site');args=parser.parse_args();build(Path(__file__).resolve().parents[1],Path(args.out).resolve())
