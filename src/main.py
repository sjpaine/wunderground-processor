 #!/usr/bin/python3 
#import Pusher
#import DataDog
#import Wunderground API manager
import config as cfg
import APIKeys as keys
import urllib3
import json

from datadog import initialize
from datadog import api
from datadog import statsd

def main():
#Build up input url
	if cfg.testResponse != '':
		Soutput = parseJsonWunderground(cfg.testResponse)
	else:
		Surl = cfg.weather['url'] + keys.APIKeys['WundergroundKey'] + cfg.weather['url2'] + cfg.weather['url3']
		http = urllib3.PoolManager()
		print(Surl)
		r = http.request('GET',Surl)
		j = json.loads(r.data.decode('utf-8'))
		Soutput = parseJsonWunderground(j)
		

def parseJsonWunderground(s1):
#Fix up the json string to send to Datadog.
	options = { 'api_key':keys.APIKeys['DataDogMainKey'], 'app_key':keys.APIKeys['DataDogAppKey'] }
	initialize(**options)

	title = "Update from Wunderground" 
	text = 'Sending data from the Wunderground Python App' 

	tags = ['version:1', 'application:Python']

	api.Event.create(title=title, text=text, tags=tags)
	
	output = []
	tempDict = {}
	for key in s1['current_observation']:
		if (is_number(str(s1['current_observation'][key]))):
			tempDict['metric'] = "weather." + key
			tempDict['points'] = float(s1['current_observation'][key])
			tempDict['host'] = "IShankil2"
			print(tempDict)
			output.append(tempDict)
			tempDict = {}
	print(output)
	print(api.Metric.send(output))

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False

    return True

if __name__ == "__main__":
	main()