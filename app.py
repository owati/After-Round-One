from flask import Flask
from dotenv import load_dotenv
from flask_socketio import SocketIO
from flask_cors import CORS

from api.api import api_bp

load_dotenv()

app = Flask(__name__)
socketio = SocketIO(app)

CORS(app)
app.register_blueprint(api_bp, url_prefix="/api/games")



if __name__ == "__main__":
    socketio.run(app)