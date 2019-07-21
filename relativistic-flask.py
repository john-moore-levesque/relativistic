from flask import Flask, render_template, flash, request
from simulator import createShip, createPlanet, planMission
from wtforms import Form, TextField, DecimalField, BooleanField, validators
from os import environ

app = Flask(__name__)
app.config.from_pyfile("relativistic.cfg")


class MissionForm(Form):
    shipname = TextField("Ship name: ",  validators = [validators.Required()])
    acceleration = DecimalField("Acceleration as a multiple of 'g': ", validators = [validators.Required()])
    planetname = TextField("Planet name: ", validators = [validators.Required()])
    brachistrone = BooleanField("Brachistrone mission? ", validators = [validators.Optional()])
    distance = DecimalField("Distance (light years): ", validators = [validators.Required()])


@app.route('/', methods=['GET', 'POST'])
def mission():
    form = MissionForm(request.form)
    print(form.errors)
    mission = None
    if request.method == 'POST':
        shipname = request.form['shipname']
        acceleration = request.form['acceleration']
        planetname = request.form['planetname']
        brachistrone = request.form['brachistrone']
        distance = request.form['distance']

        if form.validate():
            ship = createShip(shipname, acceleration)
            planet = createPlanet(planetname)
            mission = planMission(brachistrone, distance, ship, planet)
        else:
            flash("Please fill out the required fields.")

    return render_template('relativistic.html', form = form, mission = mission)
