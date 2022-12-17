from flask import render_template, request
from flask import Blueprint
import pandas as pd
from flask_login import login_required, current_user
from . import db_controller
from . import fetching as ftc

main = Blueprint('main', __name__)

@main.route('/', methods = ['GET', 'POST'])
def index():
    print(f'user now is: {current_user.username}')
    db_controller.insert_preference(current_user.username)
    cols_bs_d: list = ['year','department','baseLast']
    cols_bs_ds_y: list = ['departments','baseLast']
    df_bs_d: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_bases_department(), cols_bs_d)
    df_bs_ds_y: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_bases_departments_year(request.form.get('operator')), cols_bs_ds_y)

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
                            values2 = line_values
                            )

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username = current_user.username)