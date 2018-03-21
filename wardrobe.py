from flask import Flask, render_template, redirect, session, url_for, flash
from flask_bootstrap import Bootstrap

from item_form import NormForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NormForm()
    if form.validate_on_submit():
        old_title = session.get('title')
        if old_title is not None and old_title != form.title.data:
            flash('New title')
        session['title'] = form.title.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, title=session.get('title'))

if __name__ == '__main__':
    app.run(debug=True)
