from flask import render_template
from . import self

@self.route('/selfIntrduction', methods=['GET', 'POST'])
def selfIntrduction():
    return render_template("self/selfIntrduction.html")