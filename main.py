import os
from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ.get('PI_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('PI_PASS')
app.config['MYSQL_DATABASE_DB'] = 'portfolio'
app.config['MYSQL_DATABASE_HOST'] = 'treilly.ddns.net'

mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tech')
def tech():
    cursor.callproc('top_tech')
    results = cursor.fetchall()
    return render_template('tech.html', top_tech=results)


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/exp')
def exp():
    return render_template('exp.html')


if __name__ == '__main__':
    app.run(debug=True)
