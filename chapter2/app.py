from flask import Flask
from flask_script import Manager
from flask import request
from flask import redirect,make_response
from flask import abort

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


# @app.route('/')
# def hello_world():
#     return 'Hello World!', 404


@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s</h1>' % name


@app.route('/redirect')
def redirect():
    # response=make_response('<h1>hello</h1>')
    # return response

    # return redirect("https://www.baidu.com")
    abort(404)


if __name__ == '__main__':
    # app.run(Debug=True)
    manager.run()
