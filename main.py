from flask import render_template, request
from flask import Blueprint, make_response
import pandas as pd
from flask_login import login_required, current_user
from . import db_controller
from . import fetching as ftc

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@main.route('/', methods = ['GET', 'POST'])
def index():

    global persistent1
    global persistent2
    global persistent3
    global persistent4
    global persistent5

    def1 = 'Πληροφορικής'
    def2 = '4000'
    def3 = '40'
    def4 = '2022'
    def5 = 'ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ (ΤΡΙΠΟΛΗ)'

    sl_op1 = request.form.get('school_operator')
    sl_op2 = request.form.get('base_operator')
    sl_op3 = request.form.get('position_operator')
    sl_op4 = request.form.get('year_operator')
    sl_more = request.form.get('more_depts')

    secret = request.form.get('secret_operator')
    if secret == 'true':
        dashReq = request.form.get('saved_dashed')
        dashReq = dashReq.strip('[').strip(']').replace(" '","").replace("'","").split(',')
        print(f'saved dash is {dashReq}')
    print(f'secret is {secret}')
    
    cookie1 = request.cookies.get('persistent1')

    if sl_op1 == None: persistent1 = def1
    elif sl_op1 == '#': persistent1 = request.cookies.get('persistent1')
    else: persistent1 = sl_op1

    if sl_op2 == None: persistent2 = def2
    elif sl_op2 == '#': persistent2 = request.cookies.get('persistent2')
    else: persistent2 = sl_op2

    if sl_op3 == None: persistent3 = def3
    elif sl_op3 == '#': persistent3 = request.cookies.get('persistent3') 
    else: persistent3 = sl_op3

    if sl_op4 == None: persistent4 = def4
    elif sl_op4 == '#': persistent4 = request.cookies.get('persistent4') 
    else: persistent4 = sl_op4

    if sl_more == None: persistent5 = def5
    elif sl_more == '#': persistent5 = request.cookies.get('persistent5') 
    else: persistent5 = sl_more[:-1]; sl_more = sl_more[:-1]

    print(f'slop1 and cookie1 are -> {sl_op1}, {cookie1}')
    print(f'Submission operators  are: {persistent1, persistent2, persistent3, persistent4, persistent5}')
    #if current_user is not None: print(f'user now is: {current_user.username}, with id: {current_user.id}')

    cols_bs_ds_y: list = ['departments','baseLast','code']
    cols_bs_d: list = ['year','department','baseLast']
    
    if secret == 'true': df_bs_ds_y: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_bases_departments_year(dashReq[1], dashReq[4]), cols_bs_ds_y)
    else: df_bs_ds_y: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_bases_departments_year(persistent1, persistent4), cols_bs_ds_y)
    new_list = df_bs_ds_y['departments'][0];
    print(df_bs_ds_y)

    print(f'this is first PERSISTENT5-> {persistent5}\n')
    print(f'just to see the selection...-> {sl_more}\n')    
    print(f'just to see the new list...-> {new_list}\n\n')    

    if new_list != sl_more and sl_more != persistent5: persistent5 = new_list; print('fi')
    elif new_list != sl_more and sl_more == persistent5 and sl_op1 == '#': persistent5 = sl_more; print('thi')
    elif new_list != sl_more and sl_more == persistent5 and new_list != persistent5: persistent5 = new_list; print('sec')
    
    print(f'this is the FINAL persistent5-> {persistent5}')
    if secret == 'true': real_code = int(df_bs_ds_y.loc[df_bs_ds_y['departments'] == dashReq[5], 'code'])
    else: real_code = int(df_bs_ds_y.loc[df_bs_ds_y['departments'] == persistent5, 'code'])
    print(real_code)
    df_bs_d: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_bases_department(real_code), cols_bs_d)

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

    #un_dps: list = ftc.get_depts_by_uni(request.form.get('uni-sl'))

    cols_pr_t3: list = ['position', 'prefs']
    pr_t3: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_preferences_top_3(real_code), cols_pr_t3)
    pr_labels: str = pr_t3['position']
    pr_values: int = pr_t3['prefs']

    cols_suc_pr_t3: list = ['position', 'prefs']
    su_pr_t3: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_successful_preferences_top_3(real_code), cols_suc_pr_t3)
    su_pr_values: int = su_pr_t3['prefs']

    cols_ex_ty: list = ['examType', 'positions']
    if secret == 'true': ex_ty: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_examTypes(real_code, dashReq[4]), cols_ex_ty)
    else: ex_ty: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_examTypes(real_code, persistent4), cols_ex_ty)
    polar_labels: str = ex_ty['examType']
    polar_values: int = ex_ty['positions']

    cols_po_y_ex: list = ['year', 'positions', 'specialCat']
    years: list = ['2019', '2020', '2021', '2022']
    po_y_ex1: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_positions_year_examType("gel-ime-gen", real_code), cols_po_y_ex)
    #po_y_ex2: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_positions_year_examType("epal-ime-gen", real_code), cols_po_y_ex)
    po_y_ex3: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_positions_year_examType("gel-ime-ten", real_code), cols_po_y_ex)
    #po_y_ex4: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_positions_year_examType("epal-ime-ten", real_code), cols_po_y_ex)
    
    po_y_ex_title: str = po_y_ex1['specialCat']
    po_y_ex_labels: int = po_y_ex1['year']
    
    po_y_ex_values1: int = po_y_ex1['positions']
    #po_y_ex_values2: int = po_y_ex2['positions']
    po_y_ex_values3: int = po_y_ex3['positions']
    #po_y_ex_values4: int = po_y_ex4['positions']

    line_labels: int = df_bs_d['year']
    line_values: int = df_bs_d['baseLast']
    line_title: str = df_bs_d['department'][0]

    bar_labels: str = df_bs_ds_y['departments']
    bar_values: int = df_bs_ds_y['baseLast']

    tableaus = db_controller.get_preferences(current_user.id)

    if secret == 'true':
        persistent1 = dashReq[1]
        persistent2 = dashReq[2]
        persistent3 = dashReq[3]
        persistent4 = dashReq[4]
        persistent5 = dashReq[5]

    resp =  make_response(render_template('dashboard_non_auth.html',
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
                            #uni_dps = un_dps,
                            po_labels = po_y_ex_labels,
                            po_title = po_y_ex_title,
                            po_values1 = po_y_ex_values1,
                            #po_values2 = po_y_ex_values2,
                            po_values3 = po_y_ex_values3,
                            #po_values4 = po_y_ex_values4,
                            #labels5 = du_labels,
                            #values5 = du_values
                            persistent1 = persistent1,
                            persistent2 = persistent2,
                            persistent3 = persistent3,
                            persistent4 = persistent4,
                            persistent5 = persistent5,
                            saved = tableaus
                            )
            )       
    
    resp.set_cookie('persistent1', persistent1)
    resp.set_cookie('persistent2', persistent2)
    resp.set_cookie('persistent3', persistent3)
    resp.set_cookie('persistent4', persistent4)
    resp.set_cookie('persistent5', persistent5)

    return resp

@main.route('/save', methods = ['GET', 'POST'])
def save_selections() -> None:
    op1 = request.form.get('school')
    if op1 == '': op1 = persistent1
    op2 = request.form.get('base')
    if op2 == '': op2 = persistent2
    op3 = request.form.get('pos')
    if op3 == '': op3 = persistent3
    op4 = request.form.get('yr')
    if op4 == '': op4 = persistent4
    op5 = request.form.get('dept')
    if op5 == '': op5 = persistent5

    print(f'n1, n2, n3, n4, n5 -> {op1, op2, op3, op4, op5}')
    db_controller.insert_preference(current_user.username,
                                    current_user.id,
                                    op1,
                                    op2,
                                    op3,
                                    op4,
                                    op5
                                    )

    return ('', 204)

@main.route('/delTabls', methods = ['GET', 'POST'])
def del_tableaus() -> None:
    tableaus = request.form.to_dict()
    tableaus = list(tableaus.keys())
    print(f'tableaus are: {tableaus}')
    db_controller.del_preferences(tableaus)

    return ('', 204)

@main.route('/profile')
@login_required
def profile():
    stm = db_controller.get_preferences(current_user.id)
    return render_template('profile.html',
                           username = current_user.username,
                           stm = stm)

@main.route('/startpage', methods = ['GET'])
def start():
    return render_template('startpage.html')