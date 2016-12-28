# Episode Countdown

[![Build Status](https://travis-ci.org/nickyvanurk/episode-countdown.svg?branch=master)](https://travis-ci.org/nickyvanurk/episode-countdown)
[![Coverage Status](https://coveralls.io/repos/github/nickyvanurk/episode-countdown/badge.svg?branch=master)](https://coveralls.io/github/nickyvanurk/episode-countdown?branch=master)

A simple but useful script that will display a countdown from now until the next episode release of a specified TV show.

## Requirements
* Python 3
* Active internet connection

## Usage
* Allow the script to be executed: `chmod +x episode_countdown.py`
* Run the script: `./episode_countdown.py [name]`

## How it works
This script will take your given argument and slugify it. Next it will concatenate the slug to the URL string `http://next-episode.net/` and tries to scrape the required data from the website. Finally it will remove all unnecessary information from the scraped data and outputs the result.

## Troubleshooting
If you get the error message `Unable to aquire any data, please check your argument.` please make sure that the web page `http://next-episode.net/` + `slugified-argument` does exist.
