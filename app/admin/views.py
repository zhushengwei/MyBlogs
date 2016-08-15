# coding:utf-8
from . import admin
from .forms import PostForm
from flask import render_template, redirect, url_for
from flask_login import current_user
from ..models import Permission, Role, User, Post, db

@admin.route('/edit', methods=['GET', 'POST'])
def edit():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('main.index'))
    return render_template('admin/edit.html', form=form)