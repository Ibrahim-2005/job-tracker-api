from marshmallow import Schema, fields, validate

class JobSchema(Schema):
    company = fields.String(required=True)
    role = fields.String(required=True)
    status = fields.String(validate=validate.OneOf(["applied", "interview", "offer", "rejected"]))