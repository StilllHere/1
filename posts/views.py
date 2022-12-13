from os import abort
from flask import Blueprint, render_template, request
from .CommentsDAO.comments_dao import CommentsDAO
from .PostsDAO.posts_dao import PostsDAO
from werkzeug.exceptions import NotFound

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO('./data/posts.json')

comments_blueprint = Blueprint('comments_blueprint', __name__, template_folder='templates')
comments_dao = CommentsDAO('./data/comments.json')

@posts_blueprint.route('/')
def page_posts_all():
    posts = posts_dao.get_posts_all()
    return render_template('index.html', posts = posts)

@posts_blueprint.route('/posts/<int:postid>')
def user_page(postid):
    post = posts_dao.get_post_by_pk(postid)
    if post is None:
        abort(404)
    comments = comments_dao.get_comments_by_post_id(postid)
    len_c = len(comments)
    return render_template('post.html', post = post, comments = comments, len_c = len_c)

@posts_blueprint.route('/search')
def post_search():
    s = request.args.get('s')
    posts = posts_dao.search_for_posts(s)
    print(posts)
    if s:
        posts = posts_dao.search_for_posts(s)
        print (posts)
        l_p = len(posts)
        return render_template('search.html', s=s, posts=posts, l_p=l_p)
    else:
        raise NotFound

@posts_blueprint.route('/users/<username>')
def user_posts(username):
    if username:
        user_posts = posts_dao.get_posts_by_user(username)
        return render_template('user-feed.html', user_posts=user_posts)
    else:
        return f'Нет такого юзера'
