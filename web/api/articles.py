import web.utilities.constants as constants
from flask import Blueprint, jsonify, request
from web.utilities.helpers import payload_is_valid
import json
import markdown
from markupsafe import Markup
import time

DEBUG = True
article_blueprint = Blueprint('article', __name__, url_prefix='/article/')

@article_blueprint.route('/ping', methods=['GET'])
def pong():
    return 'pong', 200

@article_blueprint.route('', methods=['GET'])
def get_random_article():
    from random import shuffle
    with open('dummy_files/database.json') as db:
        stored_articles = json.load(db)
        article_names = list(stored_articles.keys())
        shuffle(article_names)
        db.close()
    file_as_string = get_markdown_file_from_server(stored_articles[article_names[0]])
    html_content = markdown.markdown(file_as_string)
    return Markup(html_content), 200
    #return stored_articles, 200


#################### 
# External use
####################

@article_blueprint.route('/', methods=['POST'])
def post_new_article():
    payload = json.loads(request.data)
    print(payload)
    if not payload_is_valid(payload, [constants.ARTICLE_TITLE, constants.ARTICLE_URL]):
        if DEBUG:
            return jsonify({'error': 'invalid argument'}), 400
        raise AttributeError
    article_title = payload[constants.ARTICLE_TITLE]
    article_url = payload[constants.ARTICLE_URL]
    write_to_db(article_title, article_url)
    return jsonify({'article name': f'{article_title}', 'article_path': f'{article_url}'}), 200

def write_to_db(article_title, article_url):
    with open('dummy_files/database.json', 'r') as db:
        stored_articles = json.load(db)
        stored_articles[article_title] = article_url
        with open('dummy_files/database.json', 'w') as file:
            json.dump(stored_articles, file, indent=4)
            file.close()
    db.close()


def upload_markdown_to_storage():
    # Generate an upload link for the user to submit the file to the storage service directly. Will only be for internal use.
    upload_link = generate_upload_link()


#################### 
# Placeholders for S3 functions
####################

def generate_upload_link():
    return "upload_link.com"

def get_markdown_file_from_server(md_file_path):
    # Either send the markdown as text or send a link to the markdown hosted on the storage service.
    with open(md_file_path) as md:
        file_as_string = md.read()
        time.sleep(2)
        md.close()
        return file_as_string
    


# TODO: GET endpoint for an article. Include an external hosting
# TODO: Integrate a post request to post to the resoruce
# TODO: Doing presentation of the MD is fine as it is with flask. next TODO is to include React for it
# TODO: Integrate React with the project but dont do additional front-end work.