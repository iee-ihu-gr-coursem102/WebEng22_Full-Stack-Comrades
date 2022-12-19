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

    m_y: int = ftc.get_maxYear()
    dp_s: int = ftc.get_dptSum()
    un_s: int = ftc.get_uniSum()

    cols_dp_uni: list = ['uni', 'depts']
    dp_uni: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_depts_by_uni(), cols_dp_uni)
    du_labels: str = dp_uni['uni']
    du_values: int = dp_uni['depts']

    cols_pr_t3: list = ['position', 'prefs']
    pr_t3: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_preferences_top_3(), cols_pr_t3)
    pr_labels: str = pr_t3['position']
    pr_values: int = pr_t3['prefs']

    cols_suc_pr_t3: list = ['position', 'prefs']
    su_pr_t3: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_successful_preferences_top_3(), cols_suc_pr_t3)
    su_pr_values: int = su_pr_t3['prefs']

    cols_ex_ty: list = ['examType', 'positions']
    ex_ty: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_examTypes(), cols_ex_ty)
    polar_labels: str = ex_ty['examType']
    polar_values: int = ex_ty['positions']

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
                            max_y = m_y,
                            dept_sum = dp_s,
                            uni_sum = un_s,
                            pref_top3 = pr_values,
                            labels3 = pr_labels,
                            su_pref_top3 = su_pr_values,
                            pol_val = polar_values,
                            pol_lab = polar_labels,
                            labels5 = du_labels,
                            values5 = du_values
                            )

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username = current_user.username)