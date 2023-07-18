from flask import Blueprint, render_template, request, redirect, url_for
from pubgenie.controller.job import execute_gene_query

bp = Blueprint('web', __name__)

@bp.route('/')
def index():
    return redirect(url_for('web.home'))

@bp.route('/pubgenie/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        query_type = request.form.get('query_type')
        return redirect(url_for('web.' + query_type, gene=user_input))
    return render_template('index.html')

@bp.route('/pubgenie/gene/<gene>', methods=['GET', 'POST'])
def gene(gene):
    result = execute_gene_query(gene)
    return render_template('index.html', result=result, query_type='gene', user_input=gene)

@bp.route('/pubgenie/pos/<pos>', methods=['GET', 'POST'])
def pos(pos):
    result = execute_gene_query(pos)
    return render_template('index.html', result=result, query_type='pos', user_input=pos)