from pprint import pprint
from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField
from SearchForm import SearchForm
from search_route import searchy
from timerator import timerator
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, DateField,\
    SelectField
from wtforms.validators import Required

def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # This should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'

    @app.route('/', methods=('GET', 'POST'))
    def index():
        form = SearchForm(request.form)
        if request.method == 'POST': # check whether the HTTP request sends data
            fields = ["x_pol", "y_pol", "gen_sys"]
            # Add validation. What if they don't include a timestamp?
            # Add validation. What if they don't include a key?
            # Add validation. They must chose data that exists.

            # format the timestamp
            begin = timerator(form.begin.raw_data[0])
            # format the timestamp
            end = timerator(form.end.raw_data[0])

            for i in range(3):
                # generate an HTML document with a graph of selected data
                if (form[fields[i]].raw_data[0] != ""):
                    searchy(begin, end, form[fields[i]].raw_data[0])

        return render_template('index.html', form=form)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
