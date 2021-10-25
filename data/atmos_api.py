import requests
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


url = '''
   http://openapi.seoul.go.kr:8088/6d424f64706765743730746d476f47/json/RealtimeCityAir/1/5?END_INDEX=1 
'''

# MSRDT(날짜), MSRSTE_NM(지역 ), PM10(미세먼지), IDEX_NM(상태)


response = requests.get(url)
responseDic = response.json()
data = responseDic["RealtimeCityAir"]["row"]

date = []
for i in data:
    #print(i["MSRDT"]) #날짜
    date.append(i["MSRDT"])

loc = []
for i in data:
    #print(i["MSRSTE_NM"]) #지역
    loc.append(i["MSRSTE_NM"])

pm = []
for i in data:
    #print(i["PM10"]) #미세먼지
    pm.append(i["PM10"])

stat = []
for i in data:
    #print(i["IDEX_NM"]) #상태
    stat.append(i["IDEX_NM"])

date = np.array(date)
loc = np.array(loc)
pm = np.array(pm)
stat = np.array(stat)

def getWeatherData():
    weather = np.column_stack((date,loc,pm,stat))
    #print(weather)
    weather_dataFrame = pd.DataFrame(weather,columns=["날짜","지역","미세먼지","상태"])
    #print(weather_dataFrame)
    return weather_dataFrame


def getWeatherJson():
    pass

