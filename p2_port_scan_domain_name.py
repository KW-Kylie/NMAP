import socket, sys, os

os.system('clear')

host = 'www.baidu.com'
ip = socket.gethostbyname(host)

open_ports = []
common_ports = {21, 22, 23, 25, 53, 69, 80, 88, 110}

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

#for port in xrange(start_port,end_port+1):
#	sys.stdout.flush()
#	print(port)
#	response = probe_port(host, port)
#	if response == 0:
#		open_ports.append(port)
#	if not port == end_port:
#		sys.stdout.write('\b' * len(str(port)))
#if open_ports:
#	print("Open Ports")
#	print(sorted(open_ports))
#else:
#	print("Sorry, no open ports found.")

for p in sorted(common_ports):
	sys.stdout.flush()
	print(p)
	response = probe_port(host, p)
	if response == 0:
		open_ports.append(p)

	#if not p == end_port:
	#	sys.stdout.write('\b' * len(str(p)))
if open_ports:
	print("Open Ports")
	print(sorted(open_ports))
else:
	print("Sorry, no open ports found.")