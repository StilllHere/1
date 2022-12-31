from flask import Blueprint, jsonify
from .utils import load_data, get_posts_by_id
from logs.logger import logger_api

api_blueprint = Blueprint('api_blueprint', __name__)

@api_blueprint.route('/api/posts')
def get_all_posts_json():
    data = load_data()
    logger_api.info("Request /api/posts")
    return jsonify(data)

@api_blueprint.route('/api/posts/<int:id>')
def get_one_post(id):
    post = get_posts_by_id(id)
    logger_api.info("Request /api/posts/{id}")
    return jsonify(post)