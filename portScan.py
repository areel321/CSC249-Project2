from socket import *

print("scanning for open ports...")
try:
    for port in range (8000,10000):
        mySocket = socket(AF_INET, SOCK_STREAM)
        result = mySocket.connect_ex(('131.229.234.254', port))
        if result == 0:
            print('port '+str(port)+' is open')
        else:
            print('port '+str(port)+' is not open')
        mySocket.close()


except error:
    print('error!')
    mySocket.close()