from pathlib import Path
from urllib.parse import urlparse
import json,re,sys,html
root=Path(__file__).parent
base=sys.argv[1].rstrip('/')+'/' if len(sys.argv)==2 else ''
u=urlparse(base)
if u.scheme!='https' or not u.hostname or u.hostname in ('localhost','127.0.0.1'):raise SystemExit('Supply the agreed public HTTPS base URL')
config=json.loads((root/'site-config.json').read_text());config['base_url']=base;config['status']='prepared_for_publication';(root/'site-config.json').write_text(json.dumps(config,indent=2)+'\n')
for name in ('index.html','support.html','privacy.html','contact.html'):
 p=root/name;s=p.read_text();s=re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:(?:url|image)"[^>]*>','',s)
 url=base+('' if name=='index.html' else name)
 tags=f'<link rel="canonical" href="{html.escape(url)}"><meta property="og:url" content="{html.escape(url)}"><meta property="og:image" content="{html.escape(base)}assets/traffic-icon.png">'
 p.write_text(s.replace('</head>',tags+'</head>'))
urls=[base,base+'support.html',base+'privacy.html',base+'contact.html']
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+html.escape(v)+'</loc></url>' for v in urls)+'</urlset>\n')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'sitemap.xml\n')
print('Public URL metadata prepared. This does not deploy the website or verify public availability.')
