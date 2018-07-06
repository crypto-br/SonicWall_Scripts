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

HOST = '0.0.0.0'  # IP DO SONICWALL
USER = 'USER' # USUARIO ADMINISTRATIVO DO SONICWALL
PASSWORD = 'PASS' # SENHA DO USUARIO ADMINISTRATIVO



client = pm.SSHClient()
client.load_system_host_keys()
client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
client.set_missing_host_key_policy(AllowAllKeys())
client.connect(HOST, username=USER, password=PASSWORD)

channel = client.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')

print ("REALIZANDO O BACKUP DO FIREWALL (MODELO)")

stdin.write('''
export current-config exp ftp ftp://USERFTP:SENHAFTP@O.O.O.O (IPFTP)/ARQUIVO.exp
exit
''')
print stdout.read()
print ("################################################################")
time.sleep(1)
print ("BACKUP FIREWALL (MODELO) REALIZADO COM SUCESSO")
print ("################################################################")
print ("################################################################")
time.sleep(1)

stdout.close()
stdin.close()
client.close()
