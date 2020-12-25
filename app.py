from flask import Flask, render_template, request, redirect, url_for
from random import randint
import requests
import inflect
import json
import random as rnd
import string
from collections import OrderedDict
from operator import itemgetter

app = Flask(__name__)

s = rnd.choice(string.ascii_letters) + rnd.choice(string.ascii_letters)


@app.route('/task3/cf/profile/<handle>/')
def cf_si(handle):
    return redirect(url_for('cf_single', handle=handle, page_number=1))


@app.route('/task3/cf/profile/<handle>/page/<int:page_number>/')
def cf_single(handle, page_number):
    url = f'http://codeforces.com/api/user.status?handle={handle}&from=1&count=100'
    text = requests.get(url).text
    ssilka = json.loads(text)
    popitki = ssilka["result"]

    max_page_number = (len(popitki) + 24) // 25
    return render_template("cf_single_page.html", popitki=popitki, handle=handle, max_page_number=max_page_number,
                           page_number=page_number)


@app.route('/task3/cf/top/')
def top():
    handles = sorted(request.args.get("handles").split("|"))
    orderby = request.args.get("orderby", "")
    handict = {}
    url = "https://codeforces.com/api/user.info?handles="
    for nick in handles:
        url = url + nick + ";"
    ssilka = json.loads(requests.get(url).text)
    if ssilka["status"] == "FAILED":
        return "User not found"
    else:
        for nicki in ssilka["result"]:
            handle = nicki["handle"]
            rating = nicki["rating"]
            handict[handle] = int(rating)
        if orderby == "rating":
            handict = OrderedDict(sorted(handict.items(), key=itemgetter(1), reverse=True))
    return render_template("cf_top.html", dict=handict)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error404.html"), 404


@app.route('/task2/num2words/<num>/')
def numc(num):
    if int(num) < 0 or int(num) > 999:
        return json.dumps({"status": "FAIL"})
    else:
        p = inflect.engine()
        lol = p.number_to_words(int(num))
        if 'and' in lol:
            lol = ''.join(lol.split(' and'))
        if '-' in lol:
            lol = ' '.join(lol.split('-'))
        if int(num) % 2 == 0:
            m = True
        else:
            m = False
        return json.dumps({"status": "OK", "number": int(num), "isEven": m, "words": str(lol)})


@app.route('/task2/avito/<city>/<category>/<ad>/')
def avito(city, category, ad):
    out = """<h1>debug info</h1><p>city={} category={} ad={}</p><h1>{}</h1><p>{}</p>""".format(city, category, ad, category[1], city[1])
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
