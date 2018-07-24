# This file contains the definition of the SearchForm class.

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField, validators, DateField,  SelectField
from wtforms.validators import Required

class SearchForm(FlaskForm):
    """
    This class defines a search form with 3 dropdowns and a datepicker.
    """

    # 3 Dropdowns
    x_pol = SelectField(
        label='X Pol Parameters',
        choices=[
            ('', ''),
            ('sel1X', 'sel1X'),
            ('sel2X', 'sel2X'),
            ('intswX', 'intswX'),
            ('hybrid_selValX', 'hybrid_selValX'),
            ('intLenX', 'intLenX'),
            ('lfI_X', 'lfI_X'),
            ('lfQ_X', 'lfQ_X'),
            ('iflo_x', 'iflo_x'),
        ]
    )
    y_pol = SelectField(
        label='Y Pol Parameters',
        choices=[
            ('', ''),
            ('sel1Y', 'sel1Y'),
            ('sel2Y', 'sel2Y'),
            ('intswY', 'intswY'),
            ('hybrid_selValY', 'hybrid_selValY'),
            ('intLenY', 'intLenY'),
            ('lfI_Y', 'lfI_Y'),
            ('lfQ_Y', 'lfQ_Y'),
            ('iflo_y', 'iflo_y'),
        ]
    )
    gen_sys = SelectField(
        label='General System Parameters',
        choices=[
            ('', ''),
            ('nt_state', 'nt_state'),
            ('nt_select', 'nt_select'),
            ('lo_freq', 'lo_freq'),
            ('lo_power', 'lo_power'),
        ]
    )

    # datetimepicker http://eonasdan.github.io/bootstrap-datetimepicker/
    begin = DateField(id='begin_dtpicker', label='From:')
    end = DateField(id='end_dtpicker', label='Until:')

    # Search button
    submit_button = SubmitField('Search')
