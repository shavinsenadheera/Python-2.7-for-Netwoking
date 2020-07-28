import telnetlib as tel
import getpass as pas

HOST = raw_input("HOST IP ADDRESS:")
user = raw_input("TELNET ACCOUNT NAME: ")
password = pas.getpass()

tconn = tel.Telnet(HOST)

tconn.read_until(b"Username: ")
tconn.write(user.encode('ascii') + b"\n")
if password:
    tconn.read_until(b"Password: ")
    tconn.write(password.encode('ascii') + b"\n")

print("Connection established!")
print("Starting to configuring...")
tconn.write(b"conf t\n")
for i in range(110, 201, 10):
    print(b"Creating VLAN " + str(i))
    tconn.write(b"vlan " + str(i).encode('ascii') + b"\n")
    tconn.write(b"name vlan_" + str(i).encode('ascii') + b"\n")
    tconn.write("exit\n")

tconn.write(b"end\n")
tconn.write(b"wr\n")
tconn.write(b"exit\n")

print("Hey Admin! All configurations has done successfully!")
