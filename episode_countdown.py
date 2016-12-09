#!/usr/bin/python3
import sys
import requests
import http.client
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

def have_internet():
  conn = http.client.HTTPConnection("www.google.com")
  try:
    conn.request("HEAD", "/")
    return True
  except:
    return False

def main(query):
  if not have_internet():
    return print("No internet acces.")

  URL = 'http://next-episode.net/' + query
  if is_url_valid(URL):
    data = get_countdown_data('http://next-episode.net/' + query)
    if data:
      print(filter_data(data))
      return 0
  print('Unable to aquire any data, please check your query.')

if __name__ == "__main__":
  if len(sys.argv) > 1:
    sys.exit(main(sys.argv[1]))
  else:
    print('No argument supplied.')
