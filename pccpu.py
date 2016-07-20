#!/usr/bin/python
import json, urllib2

pc_ip = "192.168.0.100" # the ip of the pc where open hardware monitor is running http://openhardwaremonitor.org/
pc_port = "8085" # the port on which OHM is running (default 8085) - you'll need to start the remote web server from OHM settings
json_file = "data.json" #this is the name of the json file containing sensor data

response = urllib2.urlopen('http://'+pc_ip+':'+pc_port+'/'+json_file)
data = json.load(response)   
#json.dumps(data)

cpu_temp = data['Children'][0]['Children'][1]['Children'][1]['Children'][4]['Value']
cpu_load = data['Children'][0]['Children'][1]['Children'][2]['Children'][4]['Value']

print "CPU ",cpu_temp.split(' ')[0]+ " 'C ", cpu_load
