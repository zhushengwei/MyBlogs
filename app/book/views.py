from . import book
from flask import render_template

@book.route('/book', methods=['GET', 'POST'])
def book():
    return render_template('book/book.html')