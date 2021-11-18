# Set up your imports and your flask app.
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template('index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.
    has_low = False
    has_upp = False
    num_end = False

    username = request.args.get('username')

    has_low = any(c.islower() for c in username)
    has_upp = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    report = has_low and has_upp and num_end

    return render_template('report.html',report=report,has_low=has_low,has_upp=has_upp,num_end=num_end)

    # Return the information to the report page html.
    pass

if __name__ == '__main__':
    app.run(debug=True)
