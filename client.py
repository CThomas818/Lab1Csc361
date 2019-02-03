#import socket module
from socket import *
import sys # In order to terminate the program


def main():

    if(len(sys.argv) == 4):
        hostname = sys.argv[1]
        port = int(sys.argv[2])
        requestfile = sys.argv[3]

        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(5.0)

            requeststring = "GET /"+requestfile+" HTTP/1.1\n"
            print(requeststring)

            s.connect((hostname, port))
       
            s.send(requeststring.encode('utf-8'))
           
            data = s.recv(10000)
            print(data)
            s.close()

        except Exception as e:
            print(e)

    else:
        print("Please specify both a hostname/ip address, a port number, and a requested html file.")

if __name__ == "__main__":
    main()


