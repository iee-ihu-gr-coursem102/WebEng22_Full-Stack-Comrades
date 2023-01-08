from flask import render_template, request
from flask import Blueprint, make_response
import pandas as pd
from flask_login import login_required, current_user
from . import db_controller
from . import fetching as ftc

uni = Blueprint('uni', __name__)

@uni.route('/universities')
def unis():
    return render_template('universitypage.html')

@uni.route('/', methods = ['GET', 'POST'])
def index():

    cols_dp_uni: list = ['uni', 'depts']
    dp_uni: pd.core.frame.DataFrame  = ftc.to_dataFrame(ftc.get_depts_by_uni(), cols_dp_uni)
    du_labels: str = dp_uni['uni']
    du_values: int = dp_uni['depts']

    cols_uni: list = ['id', 'title']
    un_ti: pd.core.frame.DataFrame = ftc.to_dataFrame(ftc.get_uniList(), cols_uni)
    un_ids: int = un_ti['id']
    un_titles: str = un_ti['title']

    un_dps: list = ftc.get_depts_by_uni(request.form.get('uni-sl'))

    resp =  make_response(render_template('universitypage.html',

                            uni_tit = un_titles,
                            uni_dps = un_dps,
                            labels5 = du_labels,
                            values5 = du_values
                        )
    )

    return resp