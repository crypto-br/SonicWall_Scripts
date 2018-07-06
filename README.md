# Backup script for SonicWall - all versions <br />

This script run in all versions UTM Sonicwall's, one FTP server is necessary for éxport backup file <br />

Use this script combined with crontab <br />

ex: ***23 50 * * * python backup-sw.py*** (Everyday on 23:50 execute script backup) <br /><br />

Another tip is: Combined with https://github.com/crypto-br/sendmailpython for recived Sucessful of Error in script execution. <br />

ex: ***python backup-sw.py > log.txt and send log in e-mail.*** <br />
