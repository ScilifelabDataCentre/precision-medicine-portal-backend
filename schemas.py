from marshmallow import Schema, fields

class PlainArticleSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    markdown_text = fields.Str(required=True)

class ArticleGetSchema(PlainArticleSchema):
    url_str = fields.Str(required=True)
    is_available = fields.Bool(required=True)

class ArticleUpdateSchema(Schema):
    title = fields.Str()
    url_str = fields.Str()
    markdown_text = fields.Str()