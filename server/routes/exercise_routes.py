from flask import Blueprint, request, jsonify
from models import db, Exercise
from schemas.exercise_schema import ExerciseSchema

exercise_bp = Blueprint("exercises", __name__)
schema = ExerciseSchema()

@exercise_bp.route("/exercises", methods=["GET"])
def get_exercises():
    return jsonify(schema.dump(Exercise.query.all(), many=True))

@exercise_bp.route("/exercises", methods=["POST"])
def create_exercise():
    try:
        data = request.get_json()
        ex = Exercise(**data)
        db.session.add(ex)
        db.session.commit()
        return schema.dump(ex), 201
    except Exception as e:
        return {"error": str(e)}, 400

@exercise_bp.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    ex = Exercise.query.get_or_404(id)
    db.session.delete(ex)
    db.session.commit()
    return {"message": "Deleted"}