from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    with open("views/index.html", 'r') as main:
        return main.read()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

