from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, session, url_for, flash

from item_form import NormForm
import os
from models import Item
from index import app, db

bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NormForm()
    if form.validate_on_submit():
        old_title = session.get('title')
        item = Item.query.filter_by(name=form.title.data).first()

        if item is None:
            item = Item(name=form.title.data)
            db.session.add(item)
        return redirect(url_for('index'))
    items = Item.query.all()
    return render_template('index.html', form=form, items=items)

if __name__ == '__main__':
    manager.run()
