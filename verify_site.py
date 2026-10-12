from pathlib import Path
from html.parser import HTMLParser
import json
from urllib.parse import urlparse,unquote

ROOT=Path(__file__).parent
class Check(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.h1=0; self.script=False; self.json_text=''; self.schemas=[]; self.form=None; self.names=set(); self.title=False; self.description=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='title':self.title=True
        if tag=='meta' and a.get('name')=='description':self.description=bool(a.get('content'))
        if tag in ('a','img','link','script'):
            link=a.get('href') or a.get('src')
            if link:self.links.append(link)
        if tag=='script' and a.get('type')=='application/ld+json':self.script=True;self.json_text=''
        if tag=='form':self.form=a
        if tag in ('input','select','textarea') and a.get('name'):self.names.add(a['name'])
    def handle_data(self,data):
        if self.script:self.json_text+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.script:self.schemas.append(json.loads(self.json_text));self.script=False
for p in ROOT.glob('*.html'):
    c=Check();c.feed(p.read_text());assert c.h1==1 and c.title,p
    if p.name!='404.html':assert c.description and c.schemas,p
    for link in c.links:
        u=urlparse(link)
        if not u.scheme and not u.netloc and u.path:assert (p.parent/unquote(u.path)).exists(),(p,link)
    if p.name=='contact.html':
        assert c.form['action']=='https://formsubmit.co/themansigoel@gmail.com' and c.form['method']=='POST'
        assert {'name','email','message','topic','privacy_consent','_honey'}<=c.names
cfg=json.loads((ROOT/'site-config.json').read_text())
if cfg['status']=='local_only':assert cfg['base_url'] is None
print('Passed: five pages, headings, metadata, JSON-LD, local links/assets and FormSubmit fields. No messages sent.')
