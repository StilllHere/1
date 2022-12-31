import json

class PostsDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """
        Get data from file
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def get_posts_all(self):
        """
        Get all posts
        """
        return self.load_data()


    def get_posts_by_user(self, user_name):
        """
        Get all posts from one user
        """
        posts = self.load_data()
        user_posts = []
        for el in posts:
            if el['poster_name'] == user_name:
                user_posts.append(el)
        return user_posts

    def search_for_posts(self, query):
        """
        Find posts by specific word
        """
        posts = self.load_data()
        query_posts = []
        query = str(query).lower()
        for el in posts:
            if query in el['content'].lower():
                query_posts.append(el)
        return query_posts[:10]

    def get_post_by_pk(self,pk):
        """
        Find post using post number
        """
        posts = self.load_data()
        for el in posts:
            if el['pk'] == pk:
                return el

