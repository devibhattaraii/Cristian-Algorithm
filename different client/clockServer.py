# Python3 program initiating a clock server

"""
Creating a process to run in background: 

Step1: Python3 name.py &
To kill it: 
Step2: fg
Step3:   ctrl+c
"""
 
import socket
import time
import datetime
from termcolor import colored
   
# function used to initiate the Clock Server
def startTimeServer():
 
    #used to create socket objects (required on both server 
    # as well as client ends to create sockets)
    node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('       ') 

    print(colored('Congratulations! The Socket has been successfully created!', 'green',attrs=['bold']))

       
    #The port number for the Server 
    port = 9000

    #used to bind to the address that is specified as a parameter
    node.bind(('', port))
      
    # node.listen(): enables the server to accept connections
    node.listen(5)    
    print(colored(' The server Socket is now listening to the client request...',attrs=['bold']))
       
   
    # Initiating the Clock Server to Run infinitely
    while True:
       
       # Establish connection with client
       """node.accept(): used to accept a connection. It returns a pair of values (conn, address)
       where conn is a new socket object for sending or receiving data and address 
       is the address of the socket present at the other end of the connection
       """
       
       conn, address = node.accept()     
       print(colored('  Server connection established to','blue',attrs=['bold']), colored(address, 'yellow',attrs=['bold']))
       
       # Respond the client with server clock time
       conn.send(str(
                    datetime.datetime.now()).encode())
       
       # Close the connection with the client process
       conn.close()
 
 
# Designing the driver function
if __name__ == '__main__':
 
    # This function is for Triggering the Clock Server  
    startTimeServer()
