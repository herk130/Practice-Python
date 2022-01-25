# /bin/python3
import sys
import socket
from datetime import datetime
from unittest import result

# define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")

# add banner
print("-" * 50)
print("Scanning Target"+target)
print("Time Started:" + str(datetime.now))
print("-" * 50)


try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # returns an error indecator
        if result == 0:
            print("Port {} is open" .format(port))
    s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()
