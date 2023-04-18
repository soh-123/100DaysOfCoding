from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapped_function():
        return '<b>' + function() + '</b>'
    return wrapped_function

def make_emphasis(function):
    def wrapped_function():
        return '<em>' + function() + '</em>'
    return wrapped_function

def make_underlined(function):
    def wrapped_function():
        return '<u>' + function() + '</u>'
    return wrapped_function

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!<h1>'\

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'bye'

@app.route('/username/<name>')
def greet(name):
    return f'Hello {name}!'

if __name__ == "__main__":
    app.run(debug=True)