from flask import Flask, render_template
from forms import AddSnackForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret"

@app.route('/snacks/new')
def add_snack():
    form  = AddSnackForm() #creates an instance for the snackform
    return render_template("add_snack_form.html", form = form) #send it to the html jinja

    #TODO: the template only shows up as an obj for the WTForm. Now you must set up a display for each idv field for it to show up. 
    



