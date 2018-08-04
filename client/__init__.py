# This file defines the create_app function and allows the client directory
# to be treated as containing packages.

def create_app(configfile=None):
    """
    This function creates the application.

    Parameters:
        configfile (str) : the optional and highly recommened configuration file

    Returns
        app (Flask) : an instance of a Flask application
    """
    import datetime
    from . helpers.begin_end import begin_end
    from flask import Flask, render_template, request, flash
    from flask_bootstrap import Bootstrap
    from flask_appconfig import AppConfig
    from . models.search.SearchForm import SearchForm
    from . models.search.search_route import searchy

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
        # check whether the HTTP request sends data
        if request.method == 'POST':
            fields = ["x_pol", "y_pol", "gen_sys"]

            # format timestamps
            begin = begin_end(form, 'begin')
            end = begin_end(form, 'end')
            # if time range is more than a week, this could take a while
            begin_check = datetime.datetime.strptime(begin, "%Y-%m-%d_%H:%M")
            end_check = datetime.datetime.strptime(end, "%Y-%m-%d_%H:%M")
            delta_t = end_check - begin_check
            print(f"delta_t.days --> {delta_t.days}")
            if delta_t.days >= 7:
                flash("Time range more than 1 week. This will take minuteS.")

            plottable = False
            empty_field_counter = 0
            for i in range(3):
                # generate an HTML document with a graph of selected data
                if (form[fields[i]].raw_data[0] != ""):
                    plottable = searchy(begin, end, form[fields[i]].raw_data[0])
                else:
                    empty_field_counter += 1

            # Check whether the user left all non-date params empty
            if (empty_field_counter >= 3):
                flash("Please select an option from a dropdown, below.")
            # Notify the user if no data matches their query.
            elif not plottable:
                flash("There is no data within that time range.", 'warning')

        return render_template('index.html', form=form)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
