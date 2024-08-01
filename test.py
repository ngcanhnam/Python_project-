import requests
import json
import pandas as pd
data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
pd.DataFrame(results)
df2 = pd.json_normalize(results)
print(df2)