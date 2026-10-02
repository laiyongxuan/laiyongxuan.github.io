"""Generate both static pages from bilingual templates and shared bibliography (stdlib only)."""
from pathlib import Path
from html import escape
import json

ROOT=Path(__file__).resolve().parents[1]
papers=json.loads((ROOT/'publications.json').read_text(encoding='utf-8'))
assert sorted(p['cv_number'] for p in papers if 'cv_number' in p)==list(range(1,22)), 'All 21 CV publications must be present exactly once'
assert len({p['title'].casefold() for p in papers})==len(papers), 'Duplicate publication'

def card(p,lang,index):
    title=escape(p.get('title_'+lang,p['title']))
    if p.get('url'):title=f'<a href="{escape(p["url"],quote=True)}">{title} ↗</a>'
    authors=escape(p['authors']).replace('Yongxuan Lai','<strong>Yongxuan Lai</strong>')
    note=escape(p.get('note_'+lang,''))
    links=''.join(f'<a class="paper-link" href="{escape(url,quote=True)}">{escape(({"Project":"项目主页","Code":"代码","Author PDF":"作者公开版本"}.get(label,label)) if lang=="zh" else label)} ↗</a>' for label,url in p.get('links',[]))
    return f'<article class="paper" data-status="{p["status"]}"><div class="paper-index">{index:02d}</div><div><h4>{title}</h4><p>{authors}</p><p class="venue">{escape(p["venue"])}</p>'+ (f'<p class="paper-note">{note}</p>' if note else '')+links+'</div></article>'

def bibliography(lang):
    zh=lang=='zh'
    published=[p for p in papers if p['status'] in ('published','accepted')]
    years=sorted({p['year'] for p in published},reverse=True)
    s='<section id="publications"><div class="section-heading"><div><p class="eyebrow">PUBLICATIONS BY YEAR</p><h2>'+('学术论文' if zh else 'Selected Publications')+'</h2></div><p>'+('按年度整理 · 更新于 2026.10.02' if zh else 'By year · Updated October 2, 2026')+'</p></div>'
    s+='<nav class="year-nav" aria-label="'+('论文年份' if zh else 'Publication years')+'">'+''.join(f'<a href="#papers-{y}">{y}</a>' for y in years)+'</nav>'
    s+='<p class="section-note">'+('包含所提供简历中逐条列出的全部 21 篇论文，并保留新增成果。按出版年份归档；会议年份与出版年份不同时另作说明。' if zh else 'Includes all 21 papers individually listed in the supplied CV, together with additional work. Grouped by publication year; conference years are noted where different.')+'</p>'
    for y in years:
        s+=f'<div class="publication-year" id="papers-{y}"><h3>{y}</h3><div class="paper-list">'
        s+=''.join(card(p,lang,i+1) for i,p in enumerate(p for p in published if p['year']==y))+'</div></div>'
    pending=[p for p in papers if p['status'] not in ('published','accepted')]
    if pending:
        s+='<div class="publication-year submissions"><h3>'+('投稿论文 · 2026' if zh else 'Submitted manuscripts · 2026')+'</h3>'
        s+=''.join(card(p,lang,i+1) for i,p in enumerate(pending))+'</div>'
    s+='</section>'
    return s

for lang,name in [('en','index.html'),('zh','zh.html')]:
    template=(ROOT/'templates'/f'{lang}.html').read_text(encoding='utf-8')
    assert template.count('{{PUBLICATIONS}}')==1
    (ROOT/name).write_text(template.replace('{{PUBLICATIONS}}',bibliography(lang)),encoding='utf-8')
print(f'Generated index.html and zh.html: {len(papers)} records, all 21 CV entries accounted for.')
