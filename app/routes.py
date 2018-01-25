from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Flex'}
    return render_template('cal.html', title='Home', user=user)
