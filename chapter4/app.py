from flask import Flask, render_template, session, url_for, redirect, flash
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("submit")


@app.route('/', methods=['POST', 'GET'])
def index():
    forms = NameForm()
    if forms.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != forms.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = forms.name.data
        return redirect(url_for('index'))
    return render_template("index.html", form=forms, name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    bootstrap.run()
