from flask import Flask
from flask_cors import CORS
from flask_sse import sse
import time


app = Flask(__name__)
app.config['SSE_REDIS_URL'] = 'redis://localhost:6379'
cors = CORS(app, origins=['localhost:3000', 'localhost:6379'])

app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def home():
    return {'Guitarist': 'Glenn Tipton'}

@app.route('/posting')
def make_post():
    for index in range(10):
        time.sleep(5)
        sse.publish({"progress": index}, type="progress")
    return 'This is a post'