from flask import Flask
from posts.views import posts_blueprint, comments_blueprint
from api.views import api_blueprint
from logs.logger import logger_api
from api.utils import load_data
import random

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(posts_blueprint)
app.register_blueprint(comments_blueprint)
app.register_blueprint(api_blueprint)

"""
Тесты API работают здесь и не работают в api_test.py :(

def test_api_posts():
    resp = app.test_client().get("/api/posts")
    assert resp.status_code == 200
    assert type(resp.json) == list

def test_api_post():
    posts_data = load_data()
    random_post = random.choice(posts_data)
    resp = app.test_client().get(f"/api/posts/{random_post['pk']}", follow_redirects=True)
    assert resp.status_code == 200
    assert type(resp.json) == dict
    post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
    assert resp.json.keys() == post_keys
"""
@app.errorhandler(500)
def internal_server_error(error):
    logger_api.error('500 internal error')
    return f'500 internal error'

@app.errorhandler(404)
def page_not_found(error):
    logger_api.error('404 page not found')
    return f'404 page not found'

if __name__ == "__main__":
    app.run()

