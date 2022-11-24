from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np
import json
import requests
# import re, os

app = Flask(__name__)


# Utility Functions --------------------------

# Make the API Call
def call_api() -> None:
   url: str = "https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base=15000&department=πληροφορική&year=2020&details=full&type=gel-ime-gen"
   response: requests.models.Response  = requests.get(url)
   res: dict = json.loads(response.content.decode('utf-8'))
   
   return res

# Extract Uni Names
def get_uni_titles(res: dict) -> list:
   uni_titles: list = []
   for i in range(len(res['records'])):
      uni_titles.append(res['records'][i]['title'])

   return uni_titles

# Extract Bases, of Year, of Department
def bases_department_year(res: dict) -> list:
   b_s_y: list = []
   for i in range(len(res['records'])):
      b_s_y.append([res['records'][i]['year'], res['records'][i]['deptName'] , res['records'][i]['baseLast']])

   return b_s_y

# Turn to DataFrame
def to_dataFrame(modded_data: list, cols: list) -> pd.core.frame.DataFrame:
   df: pd.core.frame.DataFrame = pd.DataFrame(modded_data, columns = cols)

   return df
      
def get_name() -> list:
   data: dict = get_uni_titles(call_api())

   return data

def get_bases_department_year() -> list:
   data: dict = bases_department_year(call_api())

   return data
# Routes --------------------------
   
@app.route('/')
def index():
   cols = ['year','department','baseLast']
   df = to_dataFrame(get_bases_department_year(), cols)
   bar_labels = df['department']
   bar_values = df['baseLast']
   return render_template('index.html', labels = bar_labels, values = bar_values)



if __name__ == '__main__':
   app.run(debug=True)







   