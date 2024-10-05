from flask import Flask
from src.mlproject.logger import logging

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    logging.info("testing a method of logging")
    return "welcome to e2e ml project"

if __name__ == "__main__":
    app.run(debug=True)
