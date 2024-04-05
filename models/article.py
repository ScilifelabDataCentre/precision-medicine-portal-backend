from db import db

class ArticleModel(db.Model):
    """
    Article is a piece of content that will be in markdown format together with this
    database class that will include meta-data, including the link to the content in storage.
    """
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable = False)
    url_str = db.Column(db.String(80), nullable = False, default="article_"+id)
    is_available = db.Column(db.Boolean, nullable = False, default=False)
    markdown_text = db.Column(db.String, nullable = False)