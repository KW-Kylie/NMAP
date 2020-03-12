# Learning NMAP scripting
# n_map.py
# By enter the host ip and port range in the script, then it will scan the host open ports

import nmap

nmscan = nmap.PortScanner()

nmscan.scan('your_target_ip',planed_port_range')

for host in nmscan.all_hosts():
	print('Host: %s (%s)' % (host, nmscan[host].hostname()))
	print('State: %s' % nmscan[host].state())
  
	for proto in nmscan[host].all_protocols():
		print('Protocol: %s ' % proto)
		lport = nmscan[host][proto].keys()
    
		for port in lport:
			print('port: %s\tstate: %s ' % (port, nmscan[host][proto][port]['state'] ))
