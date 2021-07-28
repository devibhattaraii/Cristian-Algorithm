# Cristian's Algorithm

The Cristian algorithm is implemented in python code designing a network of client server model. The server listens to port 9000 and waits for client to request the Server time. 
The server then returns its time to Client. The parameters are recorded and delay, Server time are taken into account to calculate the synxhronized time for Updating the client Computer. 

### Working Demo in Fedora 34(workstation)

This screenshot is taken in Fedora 34 (workstation). The working demo with the running server and client fetching the server time for synchronizzation is demonstrated.

![alt text](https://raw.githubusercontent.com/devibhattaraii/Cristian-Algorithm/master/WorkingDemo.png)

### Running the project

The follwoing steps define how to run this project. The steps I explain are tested and verified for Fedora 34 (Workstation). First get inside the project folder.
- Run clockServer.py in terminal with command "python3 clockServer.py &. 
  This will run the clockServer by creating a thread to listen port 9000 in background.
- Then in the same terminal, run Client.py by command "python3 Client.py". 
  This will request the server for time and synchronizes itself with the calculated time.
  
 The program is configured to re-request server time in ever 60 seconds while the server is running in thread we created.
