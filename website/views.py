from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Regime, Locations
from . import db
import json

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
    # locations = Locations.query.filter().first()
    # if request.method == 'POST':
    #     type = False
    #     latitude = request.form.get('latitude')
    #     longitude = request.form.get('longitude')
    #     street = request.form.get('street')
    #     zip = request.form.get('zip')
    #     city = request.form.get('city')
    #     country = request.form.get('country')
    #     print('req: ', request.form)
    #     locations = Locations.query.filter().first()
    #     if locations:
    #         msg = False
    #         print('location: ', locations)
    #     else:
    #         print('No location Found')
    return render_template("gyms.html", user=current_user,
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
