from posts.PostsDAO.posts_dao import PostsDAO
import pytest

@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO('../data/posts.json')
    return posts_dao_instance

keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

class TestPostsDao:
    def test_all_posts(self, posts_dao):
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список"
