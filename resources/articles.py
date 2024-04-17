from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import ArticleModel
from schemas import ArticleGetSchema, PlainArticleSchema, ArticleUpdateSchema

from utils import generate_url_from_title
from security import api_key_required


blp = Blueprint("Articles", __name__, description="Operations on articles")

@blp.route("/article/<string:article_id>")
class Article(MethodView):
    @api_key_required
    @blp.response(200, ArticleGetSchema)
    def get(self, article_id):
        # from flask sql-alchemy, automatically aborts if not found
        article = ArticleModel.query.get_or_404(article_id)
        return article

    @api_key_required
    def delete(self, article_id):
        article = ArticleModel.query.get_or_404(article_id)
        db.session.delete(article)
        db.session.commit()
        return {"message": "Article deleted."}

    @api_key_required
    @blp.arguments(ArticleUpdateSchema)
    @blp.response(200, ArticleGetSchema)
    def put(self, article_data, article_id):
        article = ArticleModel.query.get(article_id)
        # update any or all of title, url_str and markdown_text
        if article:
            if "title" in article_data:
                article.title = article_data["title"]
            if "url_str" in article_data:
                article.url_str = article_data["url_str"]
            if "markdown_text" in article_data:
                article.markdown_text = article_data["markdown_text"]
        else:
            article = ArticleModel(id=article_id, **article_data)

        db.session.add(article)
        db.session.commit()

        return article

@blp.route("/article")
class ArticleList(MethodView):
    @api_key_required
    @blp.response(200, ArticleGetSchema(many=True))
    def get(self):
        return ArticleModel.query.all()
    
    @api_key_required
    @blp.arguments(PlainArticleSchema)
    @blp.response(201, ArticleGetSchema)
    def post(self, article_data):
        article = ArticleModel(**article_data)

        url_str = generate_url_from_title(title=article_data["title"])
        article.url_str = url_str
        try:
            db.session.add(article)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="An article with that name already exists.",
            )
        except SQLAlchemyError:
            abort(
                500, 
                message="An error occurred while inserting the article."
            )

        return article