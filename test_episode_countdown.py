import episode_countdown as ec

def test_is_url_valid():
  assert ec.is_url_valid('http://www.google.com') == True
  assert ec.is_url_valid('http://www.google.bullshit') == False

def test_get_countdown_data():
  assert ec.get_countdown_data('http://next-episode.net/iamnotvalid') == False
  assert ec.get_countdown_data('http://next-episode.net/vikings') != False

def test_filter_data():
  data = '\nNext Episode\n\n'
  data += 'Name:All His Angels\n\n'
  data += 'Countdown:5 hours 47 min\n'
  data += 'Date:Wed Dec 28, 2016\n'
  data += 'Season:4\n'
  data += 'Episode:15\n\n'
  data += 'Summary:Episode Summary\n\n'
  expected = 'Countdown:5 hours 47 min\n'
  expected += 'Date:Wed Dec 28, 2016\n'
  expected += 'Season:4\n'
  expected += 'Episode:15'
  assert ec.filter_data(data) == expected
