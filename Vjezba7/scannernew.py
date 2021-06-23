
import socket
from multiprocessing import Pool
import time
import sys

openPorts = []  #
scannedPorts = []

try:
    ip = sys.argv[1]  # python script.py IP
except IndexError:
    print("[!] Error: No IP Entered")
    print("\n[+] Syntax: python portscan.py IP")
    sys.exit()

def banner():
    """ Banner Message"""
    banner = """
=====================Port Scanner====================
    Multiprocessing Port Scanner and Banner Check    
=====================================================
Syntax: python portscan.py IP
e.g python portscan.py 192.168.1.8
    """
    return banner

def portScan(port):
    """ Checks open port"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)  # Timeout
        pcheck = s.connect_ex((str(ip), port))
        if pcheck == 0:  # If pcheck response = 0, It means the port is open
            openPorts.append(port) # Append the open ports to openPorts
            return pcheck   # Returns pcheck to be used in main()
        s.close()  # Close the socket ~ important!
    except socket.error as e: # Error Exceptions
        pass
        # print(e)


def bannerGrab(port):
    """ Retrieves Banner Message from Service if it exists"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Timeout for banner check
        s.connect((str(ip), port))  # Connect to the IP
        bann = s.recv(50)
        return bann  # Returns the banner massage
    except socket.error as e:
        # print("Error: %s" % e)
        pass


def main(port):
    """ Runs the main script"""
    if portScan(port) == 0:
        print("[+] Port Open: %d" % port)

        if bannerGrab(port):  # If port is open, check for banner message
            print("  [-] Port %d Banner: %s" % (port, str(bannerGrab(port))))
    else:
        pass



if __name__ == "__main__":  # Initates the main script
    print(banner())  # Print our banner message
    tstart = time.time()  # Start timing
    print("[+] Reading Ports from File")
    #newPorts = open("portnum.txt", "r").read().splitlines()
    newPorts = range(1, 65536)  # All ports
    print("[+] Starting up the engines!\n")
    print("[+] Scanning IP Address: %s" % ip)
    print("[+] Scanning %d Ports" % len(newPorts))

    with Pool(processes=40) as pool:
# Starts 40 Processes, It isn't bad on memory, we can use many
        for i in pool.imap_unordered(main, [int(p) for p in newPorts]):
            if i:
                continue
            else:
                pass

    tend = time.time() - tstart  # End Timer
    print("\n[+] Finished in %d Seconds" % tend)