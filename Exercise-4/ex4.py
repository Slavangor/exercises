import os
import pandas as pd
import json

folder_path = "C:\exercises\data"


for root,dirs,files in os.walk(folder_path):
    for file in files:
        if file.endswith(".json"):
            json_path = os.path.join(root,file)





for paths in json_path:
    with open (json_path,"r") as f:
        data = json.load(f)
        df = pd.json_normalize(data)
        
    csv_path = json_path.replace(".json",".csv")
    df.to_csv(csv_path,index=False)








            
            

    