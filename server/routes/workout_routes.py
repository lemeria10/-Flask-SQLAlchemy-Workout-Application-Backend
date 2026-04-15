from flask import Blueprint, request, jsonify
from models import db, Workout
from schemas.workout_schema import WorkoutSchema
from datetime import datetime

workout_bp = Blueprint("workouts", __name__)
schema = WorkoutSchema()

@workout_bp.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(schema.dump(workouts, many=True))

@workout_bp.route("/workouts", methods=["POST"])
def create_workout():
    try:
        data = request.get_json()

        # FIX: convert string → date
        data["date"] = datetime.strptime(data["date"], "%Y-%m-%d").date()

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