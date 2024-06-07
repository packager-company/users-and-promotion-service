from flask import Flask
from flask_cors import CORS

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World x2!'


CORS(app)

if __name__ == '__main__':
    app.run()
