# coding:utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from ..models import User


# 登录表单
class LoginForm(Form):
    email = StringField(u'电子邮件', validators=[Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')


# 注册表单
class RegistrationForm(Form):
    email = StringField(u'电子邮件', validators=[Length(1, 64), Email()])
    username = StringField(u'用户名', validators=[Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, u'用户名必须只有字母、数字、点或下划线')])
    password = PasswordField(u'密码', validators=[EqualTo('password2', message=u'两次输入密码比相同')])
    password2 = PasswordField(u'再次输入密码', validators=[])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'此电子邮件已被注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'此用户名已被注册')


# 修改密码
class ChangePasswordForm(Form):
    old_password = PasswordField(u'旧密码', validators=[])
    password = PasswordField(u'新密码', validators=[EqualTo('password2', message=u'两次输入密码比相同')])
    password2 = PasswordField(u'再次输入密码', validators=[])
    submit = SubmitField(u'更改密码')