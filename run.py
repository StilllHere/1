from flask import Flask

from posts.views import posts_blueprint, comments_blueprint

app = Flask(__name__)

app.register_blueprint(posts_blueprint)
app.register_blueprint(comments_blueprint)

if __name__ == "__main__":
    app.run(debug=True)