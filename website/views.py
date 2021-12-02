from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Regime, Locations
from . import db
import json
import geopy.distance
import requests
import urllib.parse



views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("index.html", user=current_user)


@views.route('/fitness-regime', methods=['GET', 'POST'])
@login_required
def fitness_regime():
    type = msg = True
    regime = Regime.query.filter().first()
    if request.method == 'POST':
        type = False
        height = request.form.get('height')
        weight = request.form.get('weight')
        gender = request.form.get('gender')
        active = request.form.get('active')
        age = request.form.get('age')

        # print("Your body mass index is: ", round(weight / (height * height), 2))
        regime = Regime.query.filter(float(height) >= Regime.from_height,
                                     Regime.to_height >= float(height),
                                     float(weight) >= Regime.from_weight,
                                     Regime.to_weight >= float(weight),
                                     Regime.gender == gender,
                                     Regime.active == active,
                                     Regime.age == age, ).first()
        if regime:
            msg = False
            print('regime: ', regime)
        else:
            print('No Regime Found')

    return render_template("regime.html", user=current_user,
                           regime=regime, type=type, msg=msg)


@views.route('/nearby-gyms', methods=['GET', 'POST'])
@login_required
def nearby_gyms():
    type = msg = True
    coords_1 = (0.0, 0.0)
    try:
        locations = Locations.query.filter().first()
        if request.method == 'POST':
            type = False
            latitude = request.form.get('latitude')
            longitude = request.form.get('longitude')
            if latitude and longitude is not None:
                coords_1 = (latitude, longitude)
            else:
                street = request.form.get('street')
                zip = request.form.get('zip')
                city = request.form.get('city')
                country = request.form.get('country')
                address = street + ' , ' + city  + ' , ' + country
                url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
                response = requests.get(url).json()
                print('ss',response)
                if len(response) >= 1:
                    if response[0]["lat"] and response[0]["lon"]:
                        coords_1 = (response[0]["lat"], response[0]["lon"])
            points = Locations.query.filter().all()
            print(points)
            points_list = {}
            for p in points:
                coords_2 = (p.lat, p.long)
                if coords_1 and coords_2:
                    points_list[p.id] = geopy.distance.geodesic(coords_1, coords_2).km

            top = sorted(points_list.items(), key=lambda x: x[1])
            print(top)
            print('req: ', request.form)
            locations = Locations.query.limit(3).all()
            if locations:
                msg = False
                print('location: ', locations)
            else:
                print('No location Found')
    except ValueError as e:
        print(e, "An exception occurred")
    return render_template("gyms.html", user=current_user, locations=locations,
                           type=type, msg=msg)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
