from flask import Flask
from dotenv import load_dotenv
from web.routes import pages

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages)
    return app