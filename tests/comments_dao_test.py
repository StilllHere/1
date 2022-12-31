from posts.CommentsDAO.comments_dao import CommentsDAO
import pytest

@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentsDAO('../data/comments.json')
    return comments_dao_instance

keys_should_be = {'post_id', 'commenter_name', 'comment', 'pk'}

class TestCommentsDao:
    def test_get_comments_by_post_id(self, comments_dao):
        """
        Check comments are returned as a list with correct keys
        """
        comments = comments_dao.get_comments_by_post_id(1)
        assert type(comments) == list, "возвращается не список"
        assert set(comments[0].keys()) == keys_should_be, "неверный список"
