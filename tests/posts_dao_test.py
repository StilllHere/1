from posts.PostsDAO.posts_dao import PostsDAO
import pytest

@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO('../data/posts.json')
    return posts_dao_instance

keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

class TestPostsDao:
    """
    Check function get_posts_all in posts_dao
    """
    def test_all_posts(self, posts_dao):
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список"

    def test_get_posts_by_user(self, posts_dao):
        """
        Check function get_posts_by_user in posts_dao
        """
        user_posts = posts_dao.get_posts_by_user('hank')
        assert type(user_posts) == list, "возвращается не список"
        assert len(user_posts) > 0, "нет постов"
        assert set(user_posts[0].keys()) == keys_should_be, "неверный список"

    def test_get_post_by_pk(self, posts_dao):
        """
        Check function get_post_by_pk in posts_dao
        """
        post = posts_dao.get_post_by_pk(1)
        assert post['poster_name'] == "leo", "возвращает неправильное значение"
        assert type(post) == dict, "возвращается не словарь"
        assert post.keys() == keys_should_be, "неверные ключи словаря"

    def test_search_for_posts(self, posts_dao):
        """
        Check function search_for_posts in posts_dao
        """
        posts = posts_dao.search_for_posts("Проверка")
        assert len(posts) == 7, "возвращает неправильное значение"
        assert type(posts) == list, "возвращается не список"
        assert set(posts[0].keys()) == keys_should_be, "неверные ключи словаря"