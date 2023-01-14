import json
import requests
import pandas as pd
from flask import request

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

# Extract Maximum Year
def max_Year(res: int) -> int:
   m_Year: int = res['maxYear']

   return m_Year

# Extract Sum of Departments
def department_sum(res: dict) -> int:
   dp_s = len(res)

   return dp_s

# Extract List of Departments
def department_list(res: list) -> list:
   dept_l: list = []
   for d in res:
      dept_l.append(d['name'])
      #print(d['name'])

   return dept_l 

# Extract Sum of Universities
def university_sum(res: dict) -> int:
   uni_s = len(res['records'])

   return uni_s

# Extract List of Universities
def university_list(res: dict) -> list:
   uni_s: list = []
   for i in range(len(res['records'])):
      uni_s.append([res['records'][i]['id'], res['records'][i]['title']])

   return uni_s

# Extract University Full Title
def university_full_title(res: dict) -> str:
   uni_ft: str = str(res['full-title'])
   
   return uni_ft


# Extract Exam types
def exam_types(res: dict) -> list:
   ex_t: list = []
   for i in range(len(res['records'])):
      ex_t.append([res['records'][i]['examType'], res['records'][i]['positions']])
   return ex_t

# Extract Bases of Department Throughout Years
def bases_department(res: dict) -> list:
   bs_d: list = []
   for i in range(len(res['records'])):
      bs_d.append([res['records'][i]['year'], res['records'][i]['deptName'], res['records'][i]['baseLast']])

   return bs_d

# Extract Bases, of Year, of Departments
def bases_departments_year(res: dict) -> list:
   bs_ds_y: list = []
   print(f'wow -> {type(res)}')

   for i in range(len(res['records'])):
      bs_ds_y.append([res['records'][i]['deptName'], res['records'][i]['baseLast'], res['records'][i]['code']])

   return bs_ds_y

# Extract Positions, of Year, by ExamType
def positions_year_examType(res: dict) -> list:
   po_y_ex: list = []
   print(f'THIS IS RES!!!!!! {res}')

   for key, value in res.items():
    print(key, value)
    if key == 'error': po_y_ex = pd.DataFrame(); return po_y_ex

   for i in range(len(res['records'])):
      po_y_ex.append([res['records'][i]['year'], res['records'][i]['positions'], res['records'][i]['specialCat']])
      
   return po_y_ex

def preferences_top_3(res: dict) -> list:
   pr_t_3: list = []
   f= s= t = 0
   for i in range(len(res[0]['statistics'])):
      if ((res[0]['statistics'][i]['year'])==2022):
         theList = res[0]['statistics'][i]['candidatePreferences']
         f += int(theList['first'])
         s += int(theList['second'])
         t += int(theList['third'])
   theDict: dict = {'First': f, 'Second': s, 'Third' : t}
   pr_t_3 = list(theDict.items())

   return pr_t_3

def successful_preferences_top_3(res: dict) -> list:
   su_pr_t_3: list = []
   f= s= t = 0
   for i in range(len(res[0]['statistics'])):
      if ((res[0]['statistics'][i]['year'])==2022):
         theList = res[0]['statistics'][i]['successfulPreferences']
         f += int(theList['first'])
         s += int(theList['second'])
         t += int(theList['third'])
   theDict: dict = {'first': f, 'second': s, 'third' : t}
   su_pr_t_3 = list(theDict.items())

   return su_pr_t_3

# Turn to DataFrame
def to_dataFrame(modded_data: list, cols: list) -> pd.core.frame.DataFrame:
   df: pd.core.frame.DataFrame = pd.DataFrame(modded_data, columns = cols)

   return df


# GET Functions --------------------------


def get_name() -> list:
   data: dict = uni_titles(call_api())

   return data

def get_maxYear() -> int:
   data: int = max_Year(call_api('https://vaseis.iee.ihu.gr/api/index.php/bases/?year=max'))

   return data

theURL: str = "https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base=15000&department=πληροφορική&year=" + str(get_maxYear()) + "&details=full&type=gel-ime-gen"

uniIDs: list = university_list(call_api('https://vaseis.iee.ihu.gr/api/index.php/universities'))

def get_dptSum() -> int:
   data: int = department_sum(call_api('https://vaseis.iee.ihu.gr/api/index.php/departments'))

   return data

def get_uniSum() -> int:
   data: int = university_sum(call_api('https://vaseis.iee.ihu.gr/api/index.php/universities'))

   return data

def get_uniList() -> list:
   data: list = university_list(call_api('https://vaseis.iee.ihu.gr/api/index.php/universities'))
   #print(data)
   return data

# def get_uni_titles() -> list:
#    data: list = []
#    for i in range(len(uniIDs)):
#       data.append(uniIDs[i][1])
#    print(data)
#    return data

def get_uni_id_by_title(theTitle) -> int:
   data: int = 0
   theList = get_uniList()
   for i in range(len(theList)):
      if(theList[i][1]==theTitle):
         data = theList[i][0]
   #print(data)
   return data

def get_depts_by_uni(theTitle) -> list:
  data: list = []
  if theTitle is not None:
   theID: int = get_uni_id_by_title(theTitle)
   myURL: str = 'https://vaseis.iee.ihu.gr/api/index.php/departments/university/'+ str(theID)
   #print(myURL)
   theDepts: list = department_list(call_api(myURL))
   #print(theDepts)
   for i in range(len(theDepts)):
      data.append(theDepts[i])
   #print(data)
  return data

def get_uni_full_title(theTitle) -> str:
   data: str = ""
   print(theTitle)
   if theTitle is not None:
      theID: int = get_uni_id_by_title(theTitle)
      link: str =  'https://vaseis.iee.ihu.gr/api/index.php/universities/'+ str(theID)
      data = university_full_title(call_api(link))

   return data
   

# def get_depts_by_uni_old() -> list:
#    data: list = []
#    for i in range(len(uniIDs)):
#       myURL: str = 'https://vaseis.iee.ihu.gr/api/index.php/departments/university/'+ str(uniIDs[i][0])
#       theSum: int = department_sum(call_api(myURL))
#       data.append([uniIDs[i][1], theSum])
#    #print(data)
#    return data

def get_examTypes(code, year) -> str:

   cook1: str = request.cookies.get('persistent5') 
   cook2: str = request.cookies.get('persistent4') 

   if code == None and year == None: data: str = exam_types(call_api('https://vaseis.iee.ihu.gr/api/index.php/bases/2022/department/1625'))
   elif code == '#' and year == '#': data: str = exam_types(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/bases/{cook2}/department/{cook1}'))
   elif code != '#' and year == '#': data: str = exam_types(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/bases/2022/department/{code}'))
   elif code == '#' and year != '#': data: str = exam_types(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/bases/{year}/department/1625'))
   else: data: str = exam_types(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/bases/{year}/department/{code}'))

   return data

def get_bases_departments_year(school, year, base) -> list:

   cook1: str = request.cookies.get('persistent1') 
   cook2: str = request.cookies.get('persistent4')
   cook3: str = request.cookies.get('persistent2')
   print(f'HMMMM: {cook1, cook2, cook3}')
   print(f'HMMMM: {school, year, base}')

   if school == None and year == None: link: str = 'https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base=20000&department=πληροφορική&year=2022&details=full&type=gel-ime-gen'
   elif school == '#' and year == '#' and base == '#': link: str = f'https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base={cook3}&department={cook1}&year={cook2}&details=full&type=gel-ime-gen'
   elif school != '#' and year == '#' and base == '#': link: str = f'https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base=20000&department={school}&year=2022&details=full&type=gel-ime-gen'
   elif school == '#' and year != '#' and base == '#': link: str = f'https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base=20000&department=πληροφορική&year={year}&details=full&type=gel-ime-gen'
   elif school == '#' and year == '#' and base != '#': link: str = f'https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base={base}&department=πληροφορική&year=2022&details=full&type=gel-ime-gen'
   else: link: str = f'https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base={base}&department={school}&year={year}&details=full&type=gel-ime-gen'
   data: dict = bases_departments_year(call_api(link))

   return data

def get_bases_department(code) -> list:

   cook1: str = request.cookies.get('persistent5')

   if code == None: data: dict = bases_department(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/bases/department/1625?type=gel-ime-gen&details=full'))
   elif code == '#': data: dict = bases_department(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/bases/department/{cook1}?type=gel-ime-gen&details=full'))
   else: data: dict = bases_department(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/bases/department/{code}?type=gel-ime-gen&details=full'))

   return data

def get_preferences_top_3(code) -> list:

   cook1: str = request.cookies.get('persistent5')
   
   if code == None: data: dict = preferences_top_3(call_api('https://vaseis.iee.ihu.gr/api/index.php/v1.0/statistics/department/1625'))
   elif code == '#': data: dict = preferences_top_3(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/v1.0/statistics/department/{cook1}'))
   else: data: dict = preferences_top_3(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/v1.0/statistics/department/{code}'))

   return data

def get_successful_preferences_top_3(code) -> list:

   cook1: str = request.cookies.get('persistent5')
   
   if code == None: data: dict = successful_preferences_top_3(call_api('https://vaseis.iee.ihu.gr/api/index.php/v1.0/statistics/department/1625'))
   elif code == '#': data: dict = successful_preferences_top_3(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/v1.0/statistics/department/{cook1}'))
   else: data: dict = successful_preferences_top_3(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/v1.0/statistics/department/{code}'))

   return data

def get_positions_year_examType(tType, code) -> list:

   if code == None and code == '#': data: list = positions_year_examType(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/bases/department/1625?type=' + tType))
   else: data: list = positions_year_examType(call_api(f'https://vaseis.iee.ihu.gr/api/index.php/bases/department/{code}?type={tType}'))

   return data