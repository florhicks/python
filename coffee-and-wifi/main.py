from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, InputRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
Bootstrap(app)

coffee_rating_choices = ['☕️' * i for i in range(6)]
coffee_rating_choices[0]= "✘"
wifi_rating_choices = ['💪' * i for i in range(6)]
wifi_rating_choices[0]= "✘"
power_socket_choices = ['🔌' * i for i in range(6)]
power_socket_choices[0]= "✘"

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location on Google Maps (URL)', validators=[DataRequired(),URL()])
    opening_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=coffee_rating_choices,
                                validators=[InputRequired()])
    wifi_rating = SelectField('Wifi Rating',choices=wifi_rating_choices ,
                              validators=[InputRequired()])
    power_socket = SelectField('Power Outlet Rating',choices=power_socket_choices,
                               validators=[InputRequired()])
    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        new_coffe =[form.cafe.data, form.location.data, form.opening_time.data,
                    form.closing_time.data, form.coffee_rating.data, form.wifi_rating.data
            ,form.power_socket.data]
        with open("cafe-data.csv", 'a', newline='\n', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(new_coffe)
    return render_template('add.html', form=form, success="Cafe added!")


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
