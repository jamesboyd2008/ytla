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
        # pprint(vars(form.x_pol))
        # print("form: ", form.x_pol.raw_data)
        # refer = form.x_pol.raw_data[0]
        # refer = form.y_pol.raw_data[0]
        # refer = form.gen_sys.raw_data[0]

        # the above is problematic, yes?
        # pickup here: make the user chose only one attribute

        # begin = form.begin.raw_data[0] # e.g. --> 01/23/2019 12:27 PM
        # end = form.end.raw_data[0]

        # Address AM/PM confusion
        # begin = timerator(begin)
        # end = timerator(end)

        # searchy(begin, end, refer)

        return render_template('index.html', form=form)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
