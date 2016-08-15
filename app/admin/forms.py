# coding:utf-8
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField

class PostForm(Form):
    body = TextAreaField('')
    sumbit = SubmitField(u'提交')