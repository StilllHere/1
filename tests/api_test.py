import random
from run import app
from api.utils import load_data

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