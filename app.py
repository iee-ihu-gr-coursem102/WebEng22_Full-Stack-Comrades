from flask import Flask, jsonify, render_template
from fetching import *
# import re, os


app = Flask(__name__)


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







   