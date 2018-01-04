#!
import Pusher
import DataDog?
import Wunderground API manager
import BeautifulSoup

Setup vars

url=$config + $date + $PWS
Call Wunderground based on vars (x times)
result=json....

parsedResult = cleanup(result)

urlToSend=$config+ $parsedResult

Map wunderground data to output (x times)

Pusher.push(urlToSend)

Pusher.logResults

exit
Send data to Datadog