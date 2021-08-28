# This program is written for iniitating a client process for requesting the time to clock Server
# Demonstration of Implementing the Christian ALgorithm


"""Time returned by server = Tserver
Process Delay = T0-T1
Synchronized processs Client Time = T client """
 
import socket
import time
import datetime
from dateutil import parser
from timeit import default_timer as timer
from termcolor import colored

 
# function used to Synchronize client process time
def updateTime(n):    
      
	"""socket.socket(): used to create sockets (required on both server 
	as well as client ends to create sockets)"""
	node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
		
	# Server port
	port = 9000    

	# node.connect(): used to connect to a remote address specified as the parameter
	node.connect(('127.0.0.1', port))

	request_time = timer()

	# receive data from the server
	server_time = parser.parse(node.recv(1024).decode())
	response_time = timer()
	actual_time = datetime.datetime.now()


	lines = colored("---------------------------------------------------------------",attrs=['bold'])
	print('Iteration Number: ',n , ' Current Time of Request: ' + str(actual_time), '\n' )

	print(colored('  Implementation of Christian Algorithm in Client Server Model','white'),'\n' )

	formated_disp = colored("  Time returned by server: " ,'green',attrs=['bold'])
	print(formated_disp + str(server_time))

	process_delay_latency =response_time - request_time
	display_latency = round((response_time - request_time)*1000, 5)
	formated_disp1 = colored("  Process Delay latency: "  ,'green',attrs=['bold'])
	print(formated_disp1 + str(display_latency) + " mili-seconds")

	formated_disp2 = colored("  Actual clock time at client side: ", 'green',attrs=['bold'])
	print(formated_disp2 + str(actual_time))

	# synchronize process client clock time
	client_time = server_time + datetime.timedelta(seconds =(process_delay_latency) / 2)
		
		
	formated_disp3 = colored("  Synchronized process client time: "+ str(client_time), 'yellow',attrs=['bold'])
	print(formated_disp3)

	# calculate synchronization error
	sync_error = actual_time - client_time

	display_sync_error = str(sync_error.total_seconds()*1000000)
	formated_disp4 = colored("  Synchronization error : "+ (display_sync_error) +' micro-seconds', 'green',attrs=['bold'])
	print(formated_disp4)

	Tserver = server_time
	Delay = display_latency

			
	lines1 = colored("                                   ",'blue', attrs=['bold'])
	print(lines1)

	print('  Manual Verification via value substitution: ')
	print(colored('  Tserver = ', attrs=['bold']) + colored(str(Tserver), 'white') )
	print(colored('  T0- T1 = ', attrs=['bold'])  + colored(str(Delay)+ ' mili-seconds', 'white')  )
	print( colored('  Tclient =  Tserver + { (T0-T1)/2 }','yellow'))


	format_Tserver = colored (str(Tserver), 'yellow')
	format_delay = colored (str(process_delay_latency) + '/2', 'yellow')
	format_plus = colored(' + ', 'white')
	left_bracket = colored('(', 'white')
	right_bracket = colored(')', 'white')
	c_leftbracket = colored('{', 'white')
	c_Rightbracket = colored('}', 'white')


	print('        = '+ left_bracket+format_Tserver +right_bracket+ format_plus + c_leftbracket + format_delay + c_Rightbracket)
	print('        =' + '  ' + colored (str(client_time), 'yellow'))
	print (  '  ')
	print('   Client"s synchronized Time is numerically verified as well.')
	#node.close(): used to mark the socket as closed
	node.close()       

	lines1 = colored("---------------------------------------------------------------",attrs=['bold'])
	print(lines1)
	print('          ')


# Driver function
if __name__ == '__main__':
	n= 1
    # synchronize time using clock server
	while True:

		updateTime(n)
		time.sleep(60)
		n += 1


# 1. Server- Background
# Every 60 seconds- Update time.
 
