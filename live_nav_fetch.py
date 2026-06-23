import requests
import pandas as pd

# response = requests.get("https://api.mfapi.in/mf/125497")
# data = response.json()
# # print(data["meta"])

# nav_data = data["data"]
# df = pd.DataFrame(nav_data)

# df.to_csv("data/raw/live_nav_mfapi.csv",index=False)
# print("Live NAV data saved as raw CSV successfully!")
# print(df.head())

scheme_codes = [119551,120503,118632,119092,120841]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    scheme_name = data["meta"]["scheme_name"]
    print("AMFI Code - ",code,"Scheme Name - ",scheme_name)
    nav_data = data["data"]
    df = pd.DataFrame(nav_data)
    print(df.head())
