import json

class CommentsDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        """
        Get data from file
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def get_comments_by_post_id(self, post_id):
        """
        Get comments for post using post id
        """
        posts = self.load_data()
        comments = []
        allowed_id = []
        for el in posts:
            allowed_id.append(el['post_id'])
        if post_id not in allowed_id:
            raise ValueError
        for el in posts:
            if el['post_id'] == post_id:
                comments.append(el)
        return comments
