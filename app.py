from flask import Flask, jsonify
from parsers import redditParser

app = Flask(__name__)


@app.route('/')
def index():
	data = jsonify(redditParser.get_reddit_json())
	return data


if __name__ == '__main__':
	app.run(debug=True)