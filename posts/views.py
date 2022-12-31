from os import abort
from flask import Blueprint, render_template, request
from .CommentsDAO.comments_dao import CommentsDAO
from .PostsDAO.posts_dao import PostsDAO
from json import JSONDecodeError
import textwrap
import logging
from logs.logger import logger_api


posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO('./data/posts.json')

comments_blueprint = Blueprint('comments_blueprint', __name__, template_folder='templates')
comments_dao = CommentsDAO('./data/comments.json')

@posts_blueprint.route('/')
def page_posts_all():
    posts = posts_dao.get_posts_all()
    logger_api.info('Get all posts')
    return render_template('index.html', posts = posts)

@posts_blueprint.route('/posts/<int:postid>')
def user_page(postid):
    """
    При вызове такой страницы, в логи записывется 404 page not found, почему - не понимаю
    """
    post = posts_dao.get_post_by_pk(postid)
    logger_api.info(f'Получение поста с id {postid}')
    if post is None:
        abort(404)
        logger_api.error('no post')
    comments = comments_dao.get_comments_by_post_id(postid)
    len_c = len(comments)
    return render_template('post.html', post = post, comments = comments, len_c = len_c)


@posts_blueprint.route('/search', methods=['GET'])
def post_search():
    ss = request.args['s']
    logger_api.info("Searching..")
    try:
        if ss:
            posts = posts_dao.search_for_posts(ss)
            l_p = len(posts)
            del posts[10:]
            for post in posts:
                post['content'] = textwrap.shorten(post['content'], width=30, placeholder='...')
            return render_template('search.html', ss=ss, posts=posts, l_p=l_p)
        else:
            return "Вы ничего не ввели"
    except FileNotFoundError:
        logger_api.info('File is not found')
        return "Файл не найден"
    except JSONDecodeError:
        logger_api.info('Doesnt become list')
        return "Не превращается в список"

@posts_blueprint.route('/users/<username>')
def user_posts(username):
    if username:
        user_posts = posts_dao.get_posts_by_user(username)
        logger_api.info(f'Получение поста юзера {username}')
        return render_template('user-feed.html', user_posts=user_posts)
    else:
        logger_api.info(f"No user")
        return f'Нет такого юзера'
