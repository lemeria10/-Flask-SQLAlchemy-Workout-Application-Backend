from flask import Blueprint, request, jsonify
from models import db, Workout
from schemas.workout_schema import WorkoutSchema
from datetime import datetime

workout_bp = Blueprint("workouts", __name__)
schema = WorkoutSchema()

@workout_bp.route("/workouts", methods=["GET"])
def get_workouts():
    return jsonify(schema.dump(Workout.query.all(), many=True))

@workout_bp.route("/workouts", methods=["POST"])
def create_workout():
    try:
        data = request.get_json()
        workout = Workout(**data)
        db.session.add(workout)
        db.session.commit()
        return schema.dump(workout), 201
    except Exception as e:
        return {"error": str(e)}, 400

@workout_bp.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return {"message": "Deleted"}