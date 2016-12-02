#!/usr/bin/python3
import sys
import requests
import re
from bs4 import BeautifulSoup

def get_countdown_data(url):
  request = requests.get(url)
  soup = BeautifulSoup(request.content, 'lxml')
  return soup.find(id='next_episode').get_text()

def filter_countdown_data(data):
  data = data.replace('Next Episode', '')
  data = data.strip()
  data = data.split('\n', 2)[2];
  data = data[:data.rfind('\n')]
  return data.strip()

def main(query):
  data = get_countdown_data('http://next-episode.net/' + query)
  data = filter_countdown_data(data);
  print(data)

if __name__ == "__main__":
  sys.exit(main(sys.argv[1]))