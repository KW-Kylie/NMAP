import nmap

nmscan = nmap.PortScanner()

nmscan.scan('192.168.2.1','20-90')

for host in nmscan.all_hosts():
	print('Host: %s (%s)' % (host, nmscan[host].hostname()))
	print('State: %s' % nmscan[host].state())
	for proto in nmscan[host].all_protocols():
		print('Protocol: %s ' % proto)
		lport = nmscan[host][proto].keys()
		#lport.sorted(port)
		for port in lport:
			print('port: %s\tstate: %s ' % (port, nmscan[host][proto][port]['state'] ))
