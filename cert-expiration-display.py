#!/usr/bin/env python
# Author: Pierce Ortlieb
# Date: 10/27/17
# Title: cert-expiration-display.py
# About: Script runs a openssl chained commands to display certificate expiration info, the user will have the option to input the desired servername and port
import subprocess 
from subprocess import Popen, PIPE

print("------ Cert Depth & Expiration Display v1.0  ------")
server_name = raw_input("Enter server name: ")
port_number = raw_input("Enter port number: ")

def display_cert_info(servername, portnum):
	# translate parameters to String for Unix commands
	pn = str(server_name + ":" + port_number)
	
	# Unix commands we want to run
	cmd1 = ["openssl", "s_client", "-servername", str(servername), "-connect", pn]
	cmd2 = ["openssl", "x509", "-noout", "-dates"]
	
	# Use subprocess to pipe our commands through one another
	proc1 = subprocess.Popen(cmd1, stdout=PIPE)
	proc2 = subprocess.Popen(cmd2, stdin=proc1.stdout, stdout=PIPE) # Set stdin to the stdout of subproc you want output from
	
	print(proc2.communicate()[0])
	print("-----------------------------------------------------------------")

def crypto_type_info(servername, portnum):
	pn = str(server_name + ":" + port_number)

	# Unix commands we want to run
	cmd1 = ["openssl", "s_client", "-servername", str(servername), "-connect", pn]
	proc1 = subprocess.Popen(cmd1, stdout=None)

	text_holder = [str(proc1)]
	
	print("-----------------------------------------------------------------")
	print(text_holder)
			
display_cert_info(server_name, port_number)	
# crypto_type_info(server_name,port_number)















