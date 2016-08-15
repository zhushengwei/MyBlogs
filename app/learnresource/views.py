from . import learnresource
from flask import render_template

@learnresource.route('/learnPhotography', methods=['GET', 'POST'])
def learnPhotography():
    return render_template("learnresource/learnPhotography.html")

@learnresource.route('/learnPython', methods=['GET', 'POST'])
def learnPython():
    return render_template("learnresource/learnPython.html")
