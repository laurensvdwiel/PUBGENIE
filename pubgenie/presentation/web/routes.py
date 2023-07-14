from flask import Blueprint, render_template, request
from pubgenie.controller.job import execute_query

bp = Blueprint('web', __name__, template_folder='templates')

@bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@bp.route('/query', methods=['POST'])
def query():
    user_input = request.form.get('user_input')
    result = execute_query(user_input)
    return result
