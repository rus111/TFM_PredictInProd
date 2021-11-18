import requests
import pandas as pd

url = ' http://127.0.0.1:8000/predict?pickup_datetime=2013-07-06 17:18:00&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=1'
# params = {
# 'day_of_week': 0, # 0 for Sunday, 1 for Monday, ...
# 'time': '14:00'
# }
response = requests.get(url) #, params=params)
response = response.json()
print(response)
print(type(response))
X_pred = pd.DataFrame.from_dict(response)
print(X_pred)
