from marshmallow import Schema, fields
from schemas.exercise_schema import ExerciseMiniSchema

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)

    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()

    exercise = fields.Nested(ExerciseMiniSchema, dump_only=True)