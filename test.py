# This file is the C in MVC. This is the middleman between the front and
# back ends.  Information comes here to decide where to go, next.

from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from search_route import *

app = Flask(__name__)
# Bootstrap(app)
title = "YTLA Data"
headig = "YTLA Data"

def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')

@app.route("/")
@app.route("/uncompleted")
def tasks ():
    a2="active"
    return render_template('index.html',a2=a2,butes=attributes,t=title,h=headig)

@app.route("/search", methods=['GET'])
def search():
    searchy()
    return redirect('/')

if __name__ == "__main__":
    # app.run(debug=True) # Careful with the debug mode..
    app.run(host='0.0.0.0', debug=True, port=5000)
