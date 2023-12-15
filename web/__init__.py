from flask import Flask
from dotenv import load_dotenv
from web.api.articles import article_blueprint as article

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(article)
    return app
