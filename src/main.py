 #!/usr/bin/python 
#import Pusher
#import DataDog
#import Wunderground API manager
import config as cfg
import BeautifulSoup
import urllib3
import json

from datadog import initialize
from datadog import api
from datadog import statsd

def main():
#Build up input url
    if cfg.testResponse <> '':
    	Soutput = parseJsonWunderground(cfg.testResponse)
    else:
		Surl = cfg.weather['url'] + cfg.weather['apiKey'] + cfg.weather['url2'] + cfg.weather['url3']
		http = urllib3.PoolManager()
		print Surl
		r = http.request('GET',Surl)
		j = json.loads(r.data.decode('utf-8'))
		Soutput = parseJsonWunderground(j)
		

def parseJsonWunderground(s1):
#Fix up the json string to send to Datadog.
	options = { 'api_key':'XX', 'app_key':'XX' }
	initialize(**options)

	title = "Update from Wunderground" 
	text = 'Sending data from the Wunderground Python App' 

	tags = ['version:1', 'application:Python']

	api.Event.create(title=title, text=text, tags=tags)

	for key in s1['current_observation']:
		print key, s1['current_observation'][key]
		statsd.gauge("weather."+key,s1['current_observation'][key])

main()