import telnetlib as tel
import getpass as pas

HOST = raw_input("HOST IP ADDRESS:")
user = raw_input("TELNET ACCOUNT NAME: ")
password = pas.getpass()

tconn = tel.Telnet(HOST)

tconn.read_until("Username: ")
tconn.write(user + "\n")
if password:
    tconn.read_until("Password: ")
    tconn.write(password + "\n")

print("Connection established!")
print("Starting to configuring...")
tconn.write("conf t\n")
for i in range(10, 101, 10):
    print("Creating VLAN " + str(i))
    tconn.write("vlan " + str(i) + "\n")
    tconn.write("name vlan_" + str(i) + "\n")
    tconn.write("exit\n")

tconn.write("end\n")
tconn.write("wr\n")
tconn.write("exit\n")

print("Hey Admin! All configurations has done successfully!")
