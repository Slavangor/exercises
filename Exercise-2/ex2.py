import requests
import pandas as pd

url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/01017099999.csv"

response = requests.get(url)
response.status_code
file_name = "01017099999.csv"
with open (file_name,"wb") as f:
    f.write(response.content)



df = pd.read_csv(file_name)

print("Highest HourlyDryBulbTemperature is = " ,df["HourlyDryBulbTemperature"].max() )







#print(df)







