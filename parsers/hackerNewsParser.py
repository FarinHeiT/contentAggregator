import requests
import json
import asyncio
from aiohttp import ClientSession

HEADERS = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
		   'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'}


THREADS_LIST = []

async def fetch_thread(URL):
	async with ClientSession() as session:
		async with session.get(URL) as resp:
			resp = await resp.read()
			response_json = json.loads(resp)
			THREADS_LIST.append(response_json)



async def main():
	#  Get list of ID's
	IDS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
	async with ClientSession() as session:
		async with session.get(IDS_URL) as resp:
			resp = await resp.read()
	response_ids_json = json.loads(resp)

	tasks = []

	#  Create 25 tasks
	async with ClientSession() as session:
		for id in response_ids_json[:25]:
			URL = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
			task = asyncio.create_task(fetch_thread(URL))

			tasks.append(task)

	# Run until all tasks completed
	await asyncio.gather(*tasks)

	return THREADS_LIST


def get_hacker_json():
	return asyncio.run(main())

if __name__ == '__main__':
	result = asyncio.run(main())
	print(result)
