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

# Extract Maximum Year
def max_Year(res: int) -> int:
   m_Year: int = res['maxYear']

   return m_Year

# Extract Sum of Departments
def department_sum(res: dict) -> int:
   dp_s = len(res)

   return dp_s

# Extract List of Departments
#def department_list(res: list) -> list:
#   dept_l: list = []
#   for i in res:
#      dept_l.append(i['name'])
#
#   return dept_l 

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
   for i in range(len(res['records'])):
      bs_ds_y.append([res['records'][i]['deptName'], res['records'][i]['baseLast']])

   return bs_ds_y

# Extract Positions, of Year, by ExamType
def positions_year_examType(res: dict) -> list:
   po_y_ex: list = []
   for i in range(len(res['records'])):
      po_y_ex.append([res['records'][i]['year'], res['records'][i]['positions'], res['records'][i]['specialCat']])
      
   return po_y_ex


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


#def get_depts_by_uni(theTitle) -> list:
#   data: list = []
#   theID: int = get_uni_id_by_title(theTitle)
#   myURL: str = 'https://vaseis.iee.ihu.gr/api/index.php/departments/university/'+ str(theID)
#   theDepts: list = department_list(call_api(myURL))
#   for i in range(len(theDepts)):
#      data.append(theDepts[i])
#   #print(data)
#   return data

def get_examTypes() -> str:
   data: str = exam_types(call_api('https://vaseis.iee.ihu.gr/api/index.php/bases/2022/department/1625'))
   #print(data)

   return data

def get_bases_department() -> list:
   data: dict = bases_department(call_api('https://vaseis.iee.ihu.gr/api/index.php/bases/department/1622?type=gel-ime-gen&details=full'))

   return data

def get_bases_departments_year(department) -> list:
   print(f'this is the dept: {department}')
   if department == None: link: str = 'https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base=20000&department=πληροφορική&year=2020&details=full&type=gel-ime-gen'
   else: link = f'https://vaseis.iee.ihu.gr/api/index.php/bases/search/?base=20000&department={department}&year=2020&details=full&type=gel-ime-gen'
   data: dict = bases_departments_year(call_api(link))

   return data


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

def get_preferences_top_3() -> list:
   
   link = 'https://vaseis.iee.ihu.gr/api/index.php/v1.0/statistics/department/1625'
   data: list = preferences_top_3(call_api(link))
   #print(data)
   return data

def get_successful_preferences_top_3() -> list:
   
   link = 'https://vaseis.iee.ihu.gr/api/index.php/v1.0/statistics/department/1625'
   data: list = successful_preferences_top_3(call_api(link))
   #print(data)
   return data

def get_positions_year_examType(tType) -> list:
   link = 'https://vaseis.iee.ihu.gr/api/index.php/bases/department/98?type=' + tType
   data: list = positions_year_examType(call_api(link))
   #print(data)
   return data