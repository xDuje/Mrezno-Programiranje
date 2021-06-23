import socket
def get_remote_machine_info():
 remote_host = 'www.aspira.hr'
 try:
    print ("IP address: %s" %socket.gethostbyname(remote_host))
 except socket.error as err_msg:
    print ("%s: %s" %(remote_host, err_msg))
if __name__ == '__main__':
 get_remote_machine_info()

#local_machine_info.py

def print_machine_info():
 host_name = socket.gethostname()
 ip_address = socket.gethostbyname(host_name)
 print ("Host name: %s" % host_name)
 print ("IP address: %s" % ip_address)
if __name__ == '__main__':
 print_machine_info()

#find_service_name.py

def find_service_name():
 protocolname = 'tcp'
 for port in [80, 25]:
    print ("Port: %s => service name: %s" %(port, socket.getservbyport(port,
protocolname)))

    print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp')))
if __name__ == '__main__':
    find_service_name()
    
print(socket.gethostbyaddr('8.8.8.8'))