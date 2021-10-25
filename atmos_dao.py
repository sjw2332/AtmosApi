import sqlalchemy as db
import pandas as pd
from data.atmos_api import getWeatherData


engine = db.create_engine("mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")

def insert():
    weather = getWeatherData()
    weather.to_sql("weather",engine,index=False,if_exists="replace")

def select():
    weather = pd.read_sql("select * from weather",con=engine)
    print(weather)
    wt = weather.to_html()
    return wt
    
#insert()
#select()