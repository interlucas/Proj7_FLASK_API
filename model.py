


#output schema. This code maps the variable attribute to field objects 
class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):#in Meta, we define the model to relate to our schema. So this should help us return JSON from SQLAlchemy.
        model = Authors
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialisation = fields.String(required=True)
