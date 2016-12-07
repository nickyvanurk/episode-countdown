#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup

def is_url_valid(url):
  return requests.get(url).status_code == 200

def get_countdown_data(url):
  request = requests.get(url)
  soup = BeautifulSoup(request.content, 'lxml')
  element = soup.find(id='next_episode')
  if element == None:
    return False
  return element.get_text()

def filter_data(data):
  data = data.replace('Next Episode', '')
  data = data.strip()
  if 'Name' in data:
    data = data.split('\n', 2)[2];
  data = data[:data.rfind('\n')]
  return data.strip()

def main(query):
  URL = 'http://next-episode.net/' + query
  if is_url_valid(URL):
    data = get_countdown_data('http://next-episode.net/' + query)
    if data:
      print(filter_data(data))
      return 0
  print('Unable to aquire any data, please check your query.')

if __name__ == "__main__":
  sys.exit(main(sys.argv[1]))
