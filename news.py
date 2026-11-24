import json,urllib.parse,urllib.request,xml.etree.ElementTree as ET,datetime,os
assets=["Air Liquide","Alibaba","Apple","Avenir Telecom","Bitcoin","S&P 500","Stoxx Europe 600","Ethereum","Fluence Energy","Hedera","LVMH","MSCI Africa","Emerging Markets ETF","Gold","Render crypto","Safran","Solana","XRP","Uranium ETF","Apollo Global"]
items=[]
for q in assets:
 try:
  url="https://news.google.com/rss/search?q=" + urllib.parse.quote(q+" finance") + "&hl=fr&gl=FR&ceid=FR:fr"
  req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 PortfolioNewsBot"})
  root=ET.fromstring(urllib.request.urlopen(req,timeout=12).read())
  for item in root.findall("./channel/item")[:3]:
   title=item.findtext("title","");link=item.findtext("link","");date=item.findtext("pubDate","")
   if title and link:items.append({"asset":q,"title":title,"url":link,"date":date})
 except Exception as e:print("RSS error",q,e)
# deduplicate, cap feed
seen=set();out=[]
for x in items:
 if x['url'] not in seen:seen.add(x['url']);out.append(x)
os.makedirs('data',exist_ok=True)
json.dump({"updated":datetime.datetime.now(datetime.timezone.utc).isoformat(),"items":out[:80]},open('data/news.json','w'),ensure_ascii=False)
print("RSS articles:",len(out))
