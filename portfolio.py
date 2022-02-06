# Set up your imports and your flask app.
from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.fields.core import FieldList, FormField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'HelloWorld'

class HistoryEntryForm(FlaskForm):
    cmd = TextField('(base) matthew %')
    rsp = TextField()

class TermForm(FlaskForm):
    history = FieldList(FormField(HistoryEntryForm))
    lst_cmd = TextField('(base) matthew %', render_kw={'autofocus': True})

@app.route('/', methods=['GET', 'POST'])
def index():

    form = TermForm()

    if form.validate_on_submit():
      history_form = HistoryEntryForm()
      history_form.cmd = form.lst_cmd.data
      history_form.rsp = '0'
      form.history.append_entry(history_form)
      form.lst_cmd.data = ''

    # This home page should have the form.
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
