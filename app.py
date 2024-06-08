from flask import Flask
from flask_cors import CORS
from src.users.infrastructure.routes.routes import users_routes

app = Flask(__name__)

app.register_blueprint(users_routes, url_prefix='/users')


CORS(app)

if __name__ == '__main__':
    app.run()
