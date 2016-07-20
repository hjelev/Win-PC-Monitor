# Win-PC-Monitor
Python parser for http://openhardwaremonitor.org/ remote web server

I am using this python script to read the temperature sensors of my windows computers and display them in home assistant. For this script to work the windows pcs must be running http://openhardwaremonitor.org/ with remote web server enabled and its port opened in windows firewall.

This is the configuration for home assistant configuration.yaml file.
You may need to modify the command: parameter depending on where you placed the script.
{code}
sensor main_cpu_temp:
  platform: command_line
  command: "/usr/bin/python /home/pi/py/pc-monitor/pccpu.py | cut -d ' ' -f 3"
  name: main pc cpu temp
  unit_of_measurement: "°C"
{code}
