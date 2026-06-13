import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("ECOS_API_KEY")

url = (
    f"https://ecos.bok.or.kr/api/StatisticSearch/"
    f"{api_key}/json/kr/1/100/"
    f"731Y001/D/20150101/20251231/0000001"
)

response = requests.get(url)
data =response.json()

rows = data["StatisticSearch"]["row"]

df = pd.DataFrame(rows)
#print(df[["TIME", "DATA_VALUE"]].tail())


fx = df["DATA_VALUE"].astype(float)
print("평균환울:", fx.mean())
print("최고환율:", fx.max())
print("최저환율:", fx.min())

df.to_excel("data/usdkrw_daily.xlsx")