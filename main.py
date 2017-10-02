from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tech')
def tech():
    return render_template('tech.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/exp')
def exp():
    return render_template('exp.html')


if __name__ == '__main__':
    app.run()
