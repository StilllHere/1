import json

class PostsDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def get_posts_all(self):
        return self.load_data()

    def get_posts_by_user(self, user_name):
        posts = self.load_data()
        user_posts = []
        for el in posts:
            if el['poster_name'] == user_name:
                user_posts.append(el)
        return user_posts

    def search_for_posts(self, query):
        posts = self.load_data()
        query_posts = []
        query = query.lower()
        for el in posts:
            if query in el['content'].lower():
                query_posts.append(el)
        return query_posts

    def get_post_by_pk(self,pk):
        posts = self.load_data()
        for el in posts:
            if el['pk'] == pk:
                return el

