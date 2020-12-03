from flask import Flask

app = Flask(__name__)


@app.route('/')
def menu():
    out = """<pre>
    <input type="search" id="menu">
    <datalist id="character">
    <option value="1"></option>
    <option value="2"></option>
    <option value="3"></option>
   </datalist>
   </pre>"""
    return out


@app.route('/haba/')
def hello_world():
    s = ["Hello, Haba!",
         "Hello, Arsen!",
         "Hello, Karim!"]

    out = "<pre>{}</pre>".format("\n".join(s))
    return out


@app.route('/task1/random/')
def random():
    s = ["Hello, Haba!",
         "Hello, Arsen!",
         "Hello, Karim!"]

    out = "<pre>{}</pre>".format("\n".join(s))
    return out


@app.route('/task1/i_will_not/')
def i_will_not():
    s = ["Hello, Haba!",
         "Hello, Arsen!",
         "Hello, Karim!"]

    out = "<pre>{}</pre>".format("\n".join(s))
    return out
