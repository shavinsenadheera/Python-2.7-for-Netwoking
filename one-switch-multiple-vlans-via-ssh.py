import paramiko
import getpass
import time

hostname = raw_input("IP ADDRESS: ")
username = raw_input("SSH ACCOUNT NAME: ")
password = getpass.getpass()

sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclient.connect(hostname=hostname,username=username,password=password)

print("The SSH connection is established!")

rconn = sshclient.invoke_shell()
rconn.send("conf t\n")
for i in range(10,201,10):
    print("Creating VLAN " + str(i))
    rconn.send("vlan " + str(i) + "\n")
    rconn.send("name vlan_" + str(i) + "\n")
    rconn.send("exit\n")
    time.sleep(0.5)

rconn.send("end\n")
rconn.send("wr\n")

print("Congratulations Admin! Configurations has successfully done!")
sshclient.close()
