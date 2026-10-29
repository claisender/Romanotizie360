import json, urllib.request, urllib.parse, xml.etree.ElementTree as ET, datetime, re, html, pathlib
ROOT=pathlib.Path(__file__).parent
queries={'Cronaca':'Roma cronaca','Politica':'Roma Campidoglio politica','Trasporti':'Roma metro autobus ATAC','Eventi':'Roma eventi mostre','Cultura':'Roma cultura musei','Sport':'Roma Lazio sport'}
items=[]
for category,query in queries.items():
    url='https://news.google.com/rss/search?'+urllib.parse.urlencode({'q':query,'hl':'it','gl':'IT','ceid':'IT:it'})
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 RomaNotizie360/1.0'})
        with urllib.request.urlopen(req,timeout=20) as r: root=ET.fromstring(r.read())
        for x in root.findall('./channel/item')[:12]:
            title=html.unescape(x.findtext('title','')).strip()
            link=x.findtext('link','').strip()
            if not title or not link.startswith('https://'): continue
            source=x.find('source')
            publisher=source.text if source is not None else 'Google News'
            desc=re.sub('<[^>]+>',' ',x.findtext('description',''))
            desc=html.unescape(re.sub(r'\s+',' ',desc)).strip()[:240]
            items.append({'id':len(items)+1,'cat':category,'title':title,'desc':desc or 'Leggi la notizia dalla fonte originale.','url':link,'source':publisher,'published':x.findtext('pubDate',''),'img':None})
    except Exception as e: print(category,repr(e))
if not items: raise SystemExit('Nessuna notizia recuperata: mantenuto il file precedente')
payload={'updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'articles':items}
(ROOT/'news.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
print('Saved',len(items),'articles')
