from flask import Flask
from random import randint
import requests

app = Flask(__name__)


@app.route('/task2/avito/<city>/<category>/<ad>/')
def avito(city, category, ad):
    m = 'qwertyuiopasdfffghjklzxcvbnm'
    d = randint(0, len(m) - 1)
    out = """<h1>debug info</h1><p>city={} category={} ad={}</p><h1>{}</h1><p>{}</p>""".format(city, category, ad, m[d], m[d])
    return out


@app.route('/task2/cf/profile/<username>/')
def chelik(username):
    m = requests.get("https://codeforces.com/api/user.rating?handle=" + str(username)).json()
    if m["status"] != "OK":
        out = "User not found"
    else:
        print(m["result"])
        lol = str(m["result"][-1]["newRating"])
        out = """<table id=stats> <tr><th>User</th><th>Rating</th></tr>
<tr><td>{}</td><td>{}</td></tr>
</table>""".format(username, lol)
    return out


@app.route('/haba/')
def hello_world():
    s = ["Hello, Haba!",
         "Hello, Arsen!",
         "Hello, Karim!"]

    out = """<pre>{}</pre>""".format("\n".join(s))
    return out


@app.route('/task1/random/')
def random():
    out = "<pre>Haba mark is {}</pre>".format(str(randint(1, 5)))
    return out


@app.route('/task1/i_will_not/')
def i_will_not():
    s = ["<li><a>I will not waste time</a></li>" for i in range(100)]
    out = """<pre><ul id=blackboard>
 {}
</ul></pre>""".format("\n".join(s))
    return out


@app.route('/')
def menu():
    out = """<pre>
    <ul id=menu>
 <li><a href="/task1/random/">/task1/random/</a></li>
 <li><a href="/task1/i_will_not/">/task1/i_will_not/</a></li>
</ul>
   </pre>"""
    return out
