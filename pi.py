import requests
import time
import os
index = 1
query = {'field1' : '1'}
req = "https://api.thingspeak.com/channels/1752608/fields/" + str(index) + ".json?api_key=CJQ7JA502TWCDN48&results=1"
active = True
while active:
    response = requests.get(req, params=query)
    if (response.status_code == 200):
        isopen = response.text[-5:-4]
        if (isopen == '1'):
            print("Draw is open")
            os.system('fswebcam Desktop/securitycam/%H%M%S.jpg')
        else:
            if (isopen == '0'):
                print("Draw is closed")
    time.sleep(5)
