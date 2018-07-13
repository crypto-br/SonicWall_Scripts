#-------------------------------------------#
#-- Backup SonicWall -----------------------#
#-- by: @cryptobr - on Telegram ------------#
#-------------------------------------------#

# IMPORT LIBS
import sys
sys.stderr = open('/dev/null')       # Silence silly warnings from paramiko
import paramiko as pm
sys.stderr = sys.__stderr__
import os
import time
import smtplib
import socket

class AllowAllKeys(pm.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return


HOST = '0.0.0.0'  # SONICWALL IP
USER = 'USER' # ADMIN USER
PASSWORD = 'PASS' # PASSWORD ADMIN USER
PORT = 22
IP = # SET IP FOR ADD LIST

try:
	client = pm.SSHClient()
	client.load_system_host_keys()
	client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
	client.set_missing_host_key_policy(AllowAllKeys())
	client.connect(HOST, PORT, username=USER, password=PASSWORD)

	channel = client.invoke_shell()
	stdin = channel.makefile('wb')
	stdout = channel.makefile('rb')

except socket.error:
	print "SonicWall without connection"
	sys.exit()


print ("ADD IP ON EXCLUSION LIST")

stdin.write('''
configure
gateway-antivirus
exclusion list
exclusion host IP
yes
commit
exit
exit
exit
''')
print stdout.read()

print ("################################################################")
print ("SCRIPT RUNING SONICWALL (MODEL)  - SUCCESS")
print ("################################################################")

time.sleep(1)

stdout.close()
stdin.close()
client.close()
