from flask import render_template, request
from flask import Blueprint
import pandas as pd
from flask_login import login_required, current_user
from . import db_controller
from . import fetching as ftc

main = Blueprint('main', __name__)

@main.route('/', methods = ['GET', 'POST'])
def index():
    sl_op1 = request.form.get('department_operator')
    sl_op2 = request.form.get('base_operator')
    sl_op3 = request.form.get('position_operator')
    sl_op4 = request.form.get('year_operator')
    print(f'Submission operators  are: {sl_op1, sl_op2, sl_op3, sl_op4}')
    print(f'user now is: {current_user.username}, with id: {current_user.id}')

    cols_bs_d: list = ['year','department','baseLast']
    cols_bs_ds_y: list = ['departments','baseLast']
    df_bs_d: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_bases_department(), cols_bs_d)
    df_bs_ds_y: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_bases_departments_year(request.form.get('department_operator')), cols_bs_ds_y)

    m_y: int = ftc.get_maxYear()
    dp_s: int = ftc.get_dptSum()
    un_s: int = ftc.get_uniSum()

    #cols_dp_uni: list = ['uni', 'depts']
    #dp_uni: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_depts_by_uni(), cols_dp_uni)
    #du_labels: str = dp_uni['uni']
    #du_values: int = dp_uni['depts']

    cols_uni: list = ['id', 'title']
    un_ti: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_uniList(), cols_uni)
    un_ids: int = un_ti['id']
    un_titles: str = un_ti['title']

    un_dps: list = ftc.get_depts_by_uni(request.form.get('uni-sl'))

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
                            uni_tit = un_titles,
                            uni_dps = un_dps
                            #labels5 = du_labels,
                            #values5 = du_values
                            )

@main.route('/save', methods = ['GET', 'POST'])
def save_selections() -> None:
    print('ohGod...')
    op1 = request.form.get('pos')
    op2 = request.form.get('dept')
    op3 = request.form.get('yr')
    op4 = request.form.get('base')
    print(f'n1, n2, n3, n4 -> {op1, op2, op3, op4}')
    db_controller.insert_preference(current_user.username,
                                    current_user.id,
                                    op1,
                                    op2,
                                    op3,
                                    op4
                                    )

    return ('', 204)

@main.route('/profile')
@login_required
def profile():

    return render_template('profile.html', username = current_user.username)