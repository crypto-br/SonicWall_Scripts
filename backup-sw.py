#-------------------------------------------#
#-- Backup SonicWall -----------------------#
#-- by: @cryptobr - on Telegram ------------#
#-------------------------------------------#

import sys
sys.stderr = open('/dev/null')       # Silence silly warnings from paramiko
import paramiko as pm
sys.stderr = sys.__stderr__
import os
import time


class AllowAllKeys(pm.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

HOST = '0.0.0.0'  # SONICWALL IP
USER = 'USER' # ADMIN USER
PASSWORD = 'PASS' # PASSWORD ADMIN USER



client = pm.SSHClient()
client.load_system_host_keys()
client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
client.set_missing_host_key_policy(AllowAllKeys())
client.connect(HOST, username=USER, password=PASSWORD)

channel = client.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')

print ("RUNING BACKUP SONICWALL (MODEL)")

stdin.write('''
export current-config exp ftp ftp://USERFTP:PASSWORDFTP@O.O.O.O (IPFTP)/FILE.exp
exit
''')
print stdout.read()
print ("#---------------------------------------#")
time.sleep(1)
print ("BACKUP SONICWALL (MODEL)  - SUCCESS")
print ("#---------------------------------------#")
time.sleep(1)

stdout.close()
stdin.close()
client.close()
