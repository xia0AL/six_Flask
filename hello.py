from flask import Flask, request, make_response
from flask import render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/unsafe/xss1')
def unsafe_xxs1():
    first_name = request.args.get('name', '')
    return make_response("your name is " + first_name)

@app.route('/unsafe/xss2')
def unsafe_xxs2():
    first_name = request.args.get('name')
    return make_response("your name is " + first_name)


@app.route('/unsafe/xss3')
def unsafe_xxs3():
    first_name = request.args.get('name', '')
    return str(first_name)


@app.route('/unsafe/xss4')
def unsafe_xxs4():
    first_name = request.args.get('name')
    return str(first_name)

@app.route('/unsafe/pickle')
def unsafe_pickle():
    user = request.args.get('userpickled')
    user_obj = pickle.loads(user)
    return "unsafe pickle example"

if __name__ == "__main__":
    app.run(debug=True)
