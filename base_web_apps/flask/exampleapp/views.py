from flask import render_template
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index')
def index():
    return render_template('index.html')
