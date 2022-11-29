import json
import requests
import pandas as pd

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

# Extract Bases of Department Throughout Years
def bases_department(res: dict) -> list:
   bs_d: list = []
   for i in range(len(res['records'])):
      bs_d.append([res['records'][i]['year'], res['records'][i]['deptName'], res['records'][i]['baseLast']])

   return bs_d

# Extract Bases, of Year, of Departments
def bases_departments_year(res: dict) -> list:
   bs_ds_y: list = []
   for i in range(len(res['records'])):
      bs_ds_y.append([res['records'][i]['deptName'], res['records'][i]['baseLast']])

   return bs_ds_y

# Turn to DataFrame
def to_dataFrame(modded_data: list, cols: list) -> pd.core.frame.DataFrame:
   df: pd.core.frame.DataFrame = pd.DataFrame(modded_data, columns = cols)

   return df

# GET Functions --------------------------
def get_name() -> list:
   data: dict = uni_titles(call_api())

   return data

def get_bases_department() -> list:
   data: dict = bases_department(call_api('https://vaseis.iee.ihu.gr/api/index.php/bases/department/1622?type=gel-ime-gen&details=full'))

   return data

def get_bases_departments_year() -> list:
   data: dict = bases_departments_year(call_api('https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base=15000&department=πληροφορική&year=2020&details=full&type=gel-ime-gen'))

   return data