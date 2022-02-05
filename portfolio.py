# Set up your imports and your flask app.
from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.fields.core import FieldList, FormField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'HelloWorld'

class HistoryEntryForm(FlaskForm):
    cmd = TextField()
    rsp = TextField()

class TermForm(FlaskForm):
    history = FieldList(FormField(HistoryEntryForm))
    lst_cmd = TextField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():

    form = TermForm()

    if form.lst_cmd.data:
        print('validated')
        entry = {'cmd': form.lst_cmd.data}
        entry.update({'rsp': form.lst_cmd.data})
        form.history.append_entry(entry)
        form.lst_cmd.data = ''
        return render_template('index.html', form=form)

    # This home page should have the form.
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
