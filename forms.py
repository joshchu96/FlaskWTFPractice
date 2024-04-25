from flask_wtf import FlaskForm 
from wtforms import StringField, FloatField

class AddSnackForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Snack Name") #string field is used for texts
    price = FloatField("Price in USD") 
    quantity = FloatField("Amount of Snacks")