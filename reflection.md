  For my first attack, I attempted a denial of service attack by creating a short client program to send many requests to a webserver. I referenced the python socket documentation for
 this.  My program has a function and does the work of sending a packet in a while true block. Once the packet is sent, the function is called again to send another packet, and keeps going until 
 it’s stopped.  I attempted this attack on my Diana Diaz and Larissa Savitsky’s.  The attack did get through to connecting to Larissa and Diana’s webservers.  Their webservers remained the same, 
 but kept printing out the connected statements whenever a new packet came through. They never got shut down from receiving too much traffic though.  I think I’d need to send the packets at 
 possibly a faster interval and also do a distributed denial of service with more hardware to knock over a server. A potential drawback of my DoS attack is that it requires the IP address of the server hard coded in. 
    A defense I implemented to prevent this attack is keeping track of the IP addresses connected to my server and stop an IP address for making more than two connection requests.  I
 got the IP address from each connection, added it to a list, then scanned the list to make sure it only appeared twice. If it appears more times, my server denies the request and sends an error message. 
    In my group with Larissa, Diana, Paola Calle, and Hamssatou Almahamoudou Maiga, we attempted a distributed denial of service attack by all attempting to attack each other’s servers 
 using Paola’s DoS attack program. We chose one person to attack, and then all ran the program to attack their webserver at the same time. When running this, the connection got slower but did 
 not shut down the server. I also got an error that my connections weren’t accepted after sending around 1980 packets.  
    Another attack I attempted was a port scan on my server. This exploits the vulnerabilities of my server not having much security. The program goes through each of the ports in range(1, 
 1500) and uses the .connect_ex() method to see if there is a connection on a port. If a port is open, the number is printed out on the console. When running this attack on my server, I didn’t 
 observe any changes on the behavior of the server, but it was able to find the port used to create the server.  I also attempted this attack on Diana’s server as well, where performed the same but 
 took much longer to go through all the ports, most likely because it had to find the connection on another piece of hardware. Hers also printed out when it was connected and when the connection was closed when trying on each port. 
    A defense I could implement is adding a password to connect to the server.  This would prevent anyone that wasn’t given direct access through knowledge of the password from 
 accessing the webserver. Although, someone could still do a port scan if they are given the password, so if I’m trying to protect my server I should be careful with who I give access to.  
