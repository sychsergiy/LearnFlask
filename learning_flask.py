from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
