import json
from json import JSONDecodeError

def load_data():
    """
    Get data from file
    """
    try:
        with open('./data/posts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except(FileNotFoundError, JSONDecodeError):
        return "Не удается получить данные из posts.json"

    return data

def get_posts_by_id(post_id):
    """
    Get one post using his number
    """
    posts = load_data()
    for el in posts:
        if el['pk'] == post_id:
            return el