#!/usr/bin/env python

import requests, json, os
from datetime import datetime
from os import path

def send_sms(dst, text):
        voip_post = {
                "api_username" : "bhartsel@gmail.com",
                "api_password" : "p0813qRlIxrCkJrg30U9T5h3DW",
                "method" : "sendSMS",
                "did" : "6306920729",
                "dst" : dst,
                "message" : text
        }

        base_url = "https://voip.ms/api/v1/rest.php?"
        add_ons = []

        for k in voip_post.keys():
                add_ons.append(k + "=" + voip_post[k])

        url = base_url + "&".join(add_ons)
        print(url)
        voip_result = requests.get(url)
        voip_result = voip_result.text
        print(voip_result)
        voip_result = json.loads(voip_result)

data=requests.get(url="http://10.25.25.91/jc").json()

if( data["door"]==1 and path.exists("garageopen.txt") ):
	requests.get("http://10.25.25.91/cc?dkey=&close=1")
	print("Garage door closed at", datetime.now())
	os.remove("garageopen.txt")
elif ( data["door"]==1 and not path.exists("garageopen.txt") ):
	file=open("garageopen.txt", "wb")
	file.close()
	print("Garage door open at", datetime.now(),"- 15 min warning")
	send_sms("6305318070", "Garage door open!  Closing in 15 minutes")
	send_sms("6303031127", "Garage door open!  Closing in 15 minutes")
elif ( data["door"]==0 and path.exists("garageopen.txt") ):
	os.remove("garageopen.txt")
	print("Removing old garage open file, garage is closed")
