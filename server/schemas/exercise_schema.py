from marshmallow import Schema, fields

class ExerciseMiniSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    category = fields.Str()
    equipment_needed = fields.Bool()


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(required=True)