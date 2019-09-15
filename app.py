from flask import Flask, jsonify, render_template, request
from parsers import redditParser, hackerNewsParser

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/reddit.json')
def reddit_json():
	subreddit = request.args.get('subreddit')
	sort = request.args.get('sort')

	return jsonify(redditParser.get_reddit_json(subreddit, sort))


@app.route('/hacker.json')
def hacker_json():
	return jsonify(hackerNewsParser.get_hacker_json())



if __name__ == '__main__':
	app.run(debug=True)