from flask import Blueprint, render_template, request, redirect, url_for
from pubgenie.controller.job import execute_query

bp = Blueprint('web', __name__)#, template_folder='templates', static_folder='static')

@bp.route('/')
def index():
    return redirect(url_for('web.home'))

@bp.route('/pubgenie/gene/<gene>', methods=['GET', 'POST'])
def gene(gene):
    result = execute_query(gene)
    return render_template('index.html', result=result)

@bp.route('/pubgenie/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        result = execute_query(user_input)
        return render_template('index.html', result=result)
    return render_template('index.html')

@bp.route('/pubgenie/pos/<pos>', methods=['GET', 'POST'])
def pos(pos):
    # Your code here
    pass