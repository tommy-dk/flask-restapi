from flask import Flask
app = Flask(__name__)
import time

@app.route('/')
def hello_world():
    return 'Hello world, from Docker with Flask'

@app.route('/time')
def time():
    return time.time()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
