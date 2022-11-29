from flask import render_template
from flask import Blueprint
import pandas as pd
from . import fetching as ftc

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cols_bs_d: list = ['year', 'department','baseLast']
    cols_bs_ds_y: list = ['departments','baseLast']
    df_bs_d: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_bases_department(), cols_bs_d)
    df_bs_ds_y: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_bases_departments_year(), cols_bs_ds_y)

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

@main.route('/profile')
def profile():
    return 'Profile'