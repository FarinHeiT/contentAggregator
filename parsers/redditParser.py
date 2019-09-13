import requests
import json


HEADERS = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
		   'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'}


def get_reddit_json(subreddit='AskReddit', sort='hot'):
	''' Returns the list of dicts with threads of
		:subreddit - the subreddit to parse threads from
		:sort - type of sorting (Hot New Controversial Top Rising)
	'''
	URL = f'https://www.reddit.com/r/{subreddit}/{sort}.json'
	response = requests.get(URL, headers=HEADERS).text
	response_json = json.loads(response)

	THREADS_LIST = []

	# 25 threads
	for item in response_json['data']['children']:
		thread = {
			'title': item['data']['title'],
			'upvotes': item['data']['ups'],
			'url': item['data']['url'],
			'num_comments': item['data']['num_comments']
		}

		THREADS_LIST.append(thread)

	return THREADS_LIST
