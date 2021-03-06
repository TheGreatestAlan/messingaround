#!/usr/bin/python
from subprocess import Popen, PIPE
import smtplib
from socket import gaierror
import string
import subprocess

# This script attepts to retrieve the IP address of a specified interface.
# If successful it then emails the retrieved IP to a specified email address

#	FILL OUT THE VALUES BETWEEN THE COMMENT BLOCKS
#######################################################################
# Specify the sender credentials and recipient email address here
SENDER = {}
SENDER['addr'] = 'PiSperiment@gmail.com' 
SENDER['pass'] = 'ThisIsMyEmailPassword!'
SENDER['serv'] = 'smtp.gmail.com'
SENDER['port'] = 465  # default GMAIL SMTP port

RECEIVER = {}
RECEIVER['addr'] = [ 'teriaki99@gmail.com' ]; 
# Note: RECEIVER['addr']  must be a list (ie don't delete the brackets)!
# This allows the specification of a list of addresses ['me@addr.com', 'you@addr.com', 'them@addr.com']

# specify the interface to query
INTERFACE = 'eth0' # default interface for a Raspberry Pi

# specify the name of the computer to display in the email
HOSTNAME = Popen(['hostname'], stdout=PIPE).communicate()[0].replace('\n', '')

#######################################################################

# Execute the call to ifconfig 
# Use AWK to remove everything but the IP Address


oldIP = ""
subprocess.call("/home/pi/getIP.sh")
with open("/home/pi/currentIP") as f:
    for line in f:
        currentIP = line
with open("/home/pi/ipAddr") as fr:
    for line in fr:
        oldIP = line
if currentIP != oldIP:
    with open("/home/pi/ipAddr", 'w+') as file:
        file.write(currentIP)

# Construct the Email
TO = RECEIVER['addr']
FROM = SENDER['addr'] 
BODY = currentIP

# Try to send the email
try:
	server = smtplib.SMTP_SSL( SENDER['serv'], SENDER['port'] )     # NOTE:  This is the GMAIL SSL port.
	server.login( SENDER['addr'], SENDER['pass'] )
	server.sendmail( FROM, TO, BODY )
	server.quit()

except smtplib.SMTPAuthenticationError:
	print "Error, authentication failed! Please check your username and password."

except gaierror:
	print 'Error, cannot connect to: %s!  Please ensure it is a valid smtp server.' %(SENDER['serv'])
