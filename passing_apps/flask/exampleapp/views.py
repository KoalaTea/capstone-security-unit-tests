from flask import render_template
from flask import Blueprint
from flask import request
from exampleapp.forms import AddDataForm

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index')
def index():
    return render_template('index.html')

@views.route('/reflect')
def reflect():
    return render_template('index.html')

@views.route('/add', methods=["GET", "POST"])
def add():
    form = AddDataForm()
    if request.method == 'POST':
        if form.validate():
            try:
                data = form.data.data
                if data is not None:
                    return render_template('added.html')
            except:
                pass
        return render_template('failed.html')
    return render_template('add.html', form=form)
