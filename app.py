from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np
import json
import requests
# import re, os

app = Flask(__name__)


# Utility Functions --------------------------

# Make the API Call
def call_api(uri: str) -> None:
   url: str = uri
   response: requests.models.Response  = requests.get(url)
   res: dict = json.loads(response.content.decode('utf-8'))
   
   return res

# Extract Uni Names
def uni_titles(res: dict) -> list:
   uni_titles: list = []
   for i in range(len(res['records'])):
      uni_titles.append(res['records'][i]['title'])

   return uni_titles

def bases_department(res: dict) -> list:
   bs_d: list = []
   for i in range(len(res['records'])):
      bs_d.append([res['records'][i]['year'], res['records'][i]['deptName'], res['records'][i]['baseLast']])

   return bs_d

# Extract Bases, of Year, of Department
def bases_departments_year(res: dict) -> list:
   bs_ds_y: list = []
   for i in range(len(res['records'])):
      bs_ds_y.append([res['records'][i]['deptName'], res['records'][i]['baseLast']])

   return bs_ds_y

# Turn to DataFrame
def to_dataFrame(modded_data: list, cols: list) -> pd.core.frame.DataFrame:
   df: pd.core.frame.DataFrame = pd.DataFrame(modded_data, columns = cols)

   return df

# GET Functions
def get_name() -> list:
   data: dict = uni_titles(call_api())

   return data

def get_bases_department() -> list:
   data: dict = bases_department(call_api('https://vaseis.iee.ihu.gr/api/index.php/bases/department/1622?type=gel-ime-gen&details=full'))

   return data

def get_bases_departments_year() -> list:
   data: dict = bases_departments_year(call_api('https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base=15000&department=πληροφορική&year=2020&details=full&type=gel-ime-gen'))

   return data


# Routes --------------------------
   
@app.route('/')
def index():
   cols_bs_d: list = ['year', 'department','baseLast']
   cols_bs_ds_y: list = ['departments','baseLast']
   df_bs_d: pd.core.frame.DataFrame  = to_dataFrame(get_bases_department(), cols_bs_d)
   df_bs_ds_y: pd.core.frame.DataFrame = to_dataFrame(get_bases_departments_year(), cols_bs_ds_y)

   line_labels: int = df_bs_d['year']
   line_values: int = df_bs_d['baseLast']
   line_title: str = df_bs_d['department'][0]

   bar_labels: str = df_bs_ds_y['departments']
   bar_values: int = df_bs_ds_y['baseLast']
   return render_template('index.html',
                           labels = bar_labels,
                           values = bar_values,
                           department_name = line_title,
                           labels2 = line_labels,
                           values2 = line_values,
                           )



if __name__ == '__main__':
   app.run(debug=True)







   