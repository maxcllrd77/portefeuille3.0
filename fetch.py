import yfinance as yf, json, datetime, os
# Publicly listed assets with Yahoo Finance symbols. Private/unlisted SpaceX has no reliable public quote.
T={"SAF":"SAF.PA","SPX":"SXR8.DE","EM":"IS3N.DE","SXXP":"EXSA.DE","GOLD":"GOLD.PA","BTC":"BTC-EUR","ETH":"ETH-EUR","XRP":"XRP-EUR","SOL":"SOL-EUR","RNDR":"RENDER-EUR","HBAR":"HBAR-EUR","BABA":"BABA","AI":"AI.PA","LVMH":"MC.PA","AAPL":"AAPL","FLNC":"FLNC","ATEL":"ATEL.PA","AFR":"AFR.PA","URA":"URA.PA","APO":"APO"}
USD={"BABA","AAPL","FLNC","APO"}
def get_close(t):
    x=yf.download(t,period="400d",progress=False,auto_adjust=True)
    if x.empty:return None
    col=x["Close"]
    return col.squeeze().dropna()
fx=get_close("EURUSD=X");px={};hist={};failed=[]
for k,t in T.items():
 try:
  c=get_close(t)
  if c is None or c.empty: raise ValueError("empty series")
  if k in USD and fx is not None:c=c/fx.reindex(c.index).ffill().bfill()
  px[k]=round(float(c.iloc[-1]),6)
  for d,v in (c.pct_change().dropna()*100).items():hist.setdefault(str(d.date()),{})[k]=round(float(v),2)
 except Exception as e:failed.append({"asset":k,"symbol":t,"error":str(e)})
# No public market price for SpaceX private shares; intentionally exclude it.
failed.append({"asset":"SPCX","symbol":"SpaceX (private/unlisted)","error":"No reliable public market quote; manual valuation only"})
os.makedirs("data",exist_ok=True)
json.dump({"updated":datetime.datetime.now(datetime.timezone.utc).isoformat(),"px":px,"hist":hist,"failed":failed,"source":"Yahoo Finance via yfinance; EUR-normalized where conversion applies"},open("data/prices.json","w"),ensure_ascii=False)
print(f"Updated {len(px)} quotes; unavailable: {failed}")
