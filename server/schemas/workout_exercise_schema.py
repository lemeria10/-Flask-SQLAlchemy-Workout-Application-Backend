from marshmallow import Schema, fields

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)

    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()