from flask import Blueprint, request
from models import db, WorkoutExercise
from schemas.workout_exercise_schema import WorkoutExerciseSchema

we_bp = Blueprint("workout_exercises", __name__)
schema = WorkoutExerciseSchema()

@we_bp.route("/workout_exercises", methods=["POST"])
def add_exercise():
    try:
        data = request.get_json()
        we = WorkoutExercise(**data)
        db.session.add(we)
        db.session.commit()
        return schema.dump(we), 201
    except Exception as e:
        return {"error": str(e)}, 400