 #!/usr/bin/python 
#import Pusher
#import DataDog
#import Wunderground API manager
import config as cfg
import BeautifulSoup
import urllib3
import json

from datadog import initialize

options = { 'api_key':'227b3e60446aec4a62a48ef3a88e5510', 'app_key':'48bb55b1194e4e33a4fa7f3fe48e83f2cd40138a' }
initialize(**options)

from datadog import api

title = "Something big happened!" 
text = 'And let me tell you all about it here!' 

tags = ['version:1', 'application:web']

api.Event.create(title=title, text=text, tags=tags)

from datadog import statsd

statsd.increment('whatever') 
statsd.gauge('foo', 42)

from datadog import ThreadStats 

stats = ThreadStats() 
stats.start() 
stats.increment('home.page.hits') 
stats.end()

# Setup vars

# url=$config + $date + $PWS
# Call Wunderground based on vars (x times)
# result=json....


def main():
#Build up input url
    if cfg.testResponse <> '':
    	Soutput = parseJsonWunderground(cfg.testResponse)
    else:
		Sdate = '20180102'
		Surl = cfg.weather['url'] + cfg.weather['apiKey'] + cfg.weather['url2'] + Sdate + cfg.weather['url3']
		http = urllib3.PoolManager()
		r = http.request('GET',Surl)
		j = json.loads(r.data.decode('utf-8'))
		Soutput = parseJsonWunderground(j)
		

def parseJsonWunderground(s1):
#Fix up the json string to send to Datadog.
	print s1['history']['observations']



# parsedResult = cleanup(result)

# urlToSend=$config+ $parsedResult

# Map wunderground data to output (x times)

# Pusher.push(urlToSend)

# Pusher.logResults

# exit
# Send data to Datadog
main()