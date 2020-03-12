import socket, subprocess, sys
from datetime import datetime

#subprocess.call('clear', shell=True)
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
		#sock.close()

except KeyboardInterrupt:
	print "...Oh..you stopped the scanning."
	sys.exit()

except Exception as e:
	print e
	sys.exit()

t2 = datetime.now()
total = t2 - t1
print "Scanning completed in ", total
