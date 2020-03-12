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

# p2_port_scan_domain_name.py
# By enter the domain name and port range in the script, then it will scan the host open ports

import socket, sys, os
os.system('clear')
host = 'domain_name eg:www.baidu.com'
ip = socket.gethostbyname(host)
open_ports = []
common_ports = {define_port eg:21, 22, 23, 25, 53, 69, 80, 88, 110}
def probe_port(host, port, result = 1):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((host, port))
		if r == 0:
			result = r
		sock.close()
	except Exception as e:
		print(e)
		pass
	return result

for p in sorted(common_ports):
	sys.stdout.flush()
	print(p)
	response = probe_port(host, p)
	if response == 0:
		open_ports.append(p)
if open_ports:
	print("Open Ports")
	print(sorted(open_ports))
else:
	print("Sorry, no open ports found.")


# p2_portscan_ip.py
# Enter the required info as required

import socket, subprocess, sys
from datetime import datetime
rmip = raw_input("Please enter the remote host IP to scan: ")
r1 = int(raw_input("Please enter the start port numbert: "))
r2 = int(raw_input("Please enter the last port numbert: "))
print "Scanner is working on:", rmip
print "Please wait......"
t1 = datetime.now()
try:
	for port in range(r1, r2):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = sock.connect_ex((rmip, port))
		if result == 0:
			print "Port Open:-->t", port   #print dest_port
except KeyboardInterrupt:
	print "...Oh..you stopped the scanning."
	sys.exit()
except Exception as e:
	print e
	sys.exit()
t2 = datetime.now()
total = t2 - t1
print "Scanning completed in ", total
