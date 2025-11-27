from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey welcome to site, which is served by docker and deployed using multi stage builds'

@app.route('/health')
def health():
    return 'Server is up and running'
