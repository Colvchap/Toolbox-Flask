"""
This is a simple profile making web app that utilises Flask. -a web development
program with an importable module for Python.
"""
from flask import Flask, request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('get_intel.html')


@app.route('/login', methods=['GET', 'POST'])
def make_profile():
    if request.method == 'POST':
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        age = request.form["age"]
        return render_template('profile.html', firstname=firstname,
                               lastname=lastname, age=age)
    else:
        return render_template('get_intel.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
