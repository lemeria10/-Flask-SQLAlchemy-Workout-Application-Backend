from marshmallow import Schema, fields
from schemas.workout_exercise_schema import WorkoutExerciseSchema

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True)