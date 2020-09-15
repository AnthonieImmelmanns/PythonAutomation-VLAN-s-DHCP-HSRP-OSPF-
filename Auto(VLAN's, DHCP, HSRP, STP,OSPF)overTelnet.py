import getpass
import sys
import telnetlib

# Get username and password
user = input("AUTHORIZED ACCESS ONLY!!! Automation script \nPlease enter your telnet Username: ")
password = getpass.getpass()

# Switches 1 - 14  
for a in range (1,15):

		HOST = "192.168.1." + str(a)

		tn = telnetlib.Telnet(HOST)

		tn.read_until("Username: ")
		tn.write(user + "\n")
		if password:
			tn.read_until("Password: ")
		tn.write(password + "\n")

		# Cisco CLI
		tn.write("conf t\n")
		tn.write("no ip domain-lookup\n")
		tn.write("banner motd#Authorised Personel Only!!!#\n") # banner
		tn.write("end\n")
		tn.write("exit\n")

		print (tn.read_all())

# Switches 3 & 4 Configure VLAN's, DHCP & HSRP on the DISTRIBUTION Layer 
for b in range(3,5):
		HOST = "192.168.1." + str(b)
		ai = b

		tn = telnetlib.Telnet(HOST)

		tn.read_until("Username: ")
		tn.write(user + "\n")
		if password:
			tn.read_until("Password: ")
			tn.write(password + "\n")

		# Config VLAN's 5,10,15,20,25,30,35 & 40
		tn.write("conf t\n")
		for i in range(0,41,5):
			if i == 0: # No VLAN 0
				continue
			tn.write("vlan " + str(i) + "\n")
			tn.write("name Company_VLAN_" + str(i) + "\n")

		tn.write("exit\n")

		# Configure VLAN's ip addresses
		for j in range(0,41,5):
			if j == 0: 
				continue
			tn.write("int vlan " + str(j) + "\n")
			tn.write("ip address 192.168." + str(j) + "." + str(ai) + " 255.255.255.0\n")
			tn.write("no shut\n")

		tn.write("end\n")

		# Configure DHCP and DNS on VLAN 5,10,15,20,25,30,35 & 45
		for k in range(0,41,5):
			if k == 0:
				continue
			tn.write("conf t\n")
			tn.write("ip dhcp exclude 192.168." + str(k) + ".1 192.168." + str(k) + ".15\n")
			tn.write("ip dhcp pool VLAN" + str(k) + "\n")
			tn.write("network 192.168." + str(k) + ".0 255.255.255.0\n")
			tn.write("defau 192.168." + str(k) + ".254\n")
			tn.write("domain Anthonie.com\n")
			tn.write("dns 8.8.8.8\n")
			tn.write("end\n")

		# Configure HSRP 
		tn.write("conf t\n")
		for l in range(0, 41, 5):
			if l == 0:
				continue

			tn.write("int vlan " + str(l) + "\n")
			tn.write("standby " + str(l) + " ip 192.168." + str(l) + ".254\n")
			tn.write("exit\n")


		tn.write("end\n")
		tn.write("exit\n")
		
		print (tn.read_all())

# Switches 5 & 6 and VLAN's 5,10,15 & 20 on the ACCESS LAYER
for c in range(5,7):

		HOST = "192.168.1." + str(c)

		tn = telnetlib.Telnet(HOST)

		tn.read_until("Username: ")
		tn.write(user + "\n")
		if password:
			tn.read_until("Password: ")
			tn.write(password + "\n")

		tn.write("conf t\n")
		for i in range(0,21,5):
			if i == 0: 
				continue
			tn.write("vlan " + str(i) + "\n")
			tn.write("name Company_VLAN_" + str(i) + "\n")

		tn.write("end\n")
		tn.write("exit\n")

		print (tn.read_all())

# Switches 7 & 8 and VLAN's 25,30,35 & 40 on the ACCESS LAYER
for d in range(7,9):

		HOST = "192.168.1." + str(d)

		tn = telnetlib.Telnet(HOST)

		tn.read_until("Username: ")
		tn.write(user + "\n")
		if password:
			tn.read_until("Password: ")
			tn.write(password + "\n")

		tn.write("conf t\n")
		for i in range(25,41,5):
			tn.write("vlan " + str(i) + "\n")
			tn.write("name Company_VLAN_" + str(i) + "\n")

		tn.write("end\n")
		tn.write("exit\n")

		print (tn.read_all())

# Switches 9 & 10 Configure VLAN's, DHCP & HSRP on the DISTRIBUTION Layer 
for e in range(9,11):
		HOST = "192.168.1." + str(e)
		ai = e

		tn = telnetlib.Telnet(HOST)

		tn.read_until("Username: ")
		tn.write(user + "\n")
		if password:
			tn.read_until("Password: ")
			tn.write(password + "\n")

		# Config VLAN's 50,55,60,65,70,75,80 & 85
		tn.write("conf t\n")
		for i in range(50,86,5):
			tn.write("vlan " + str(i) + "\n")
			tn.write("name Company_VLAN_" + str(i) + "\n")

		tn.write("exit\n")
		# Configure VLAN's ip addresses

		for j in range(50,86,5):

			tn.write("int vlan " + str(j) + "\n")
			tn.write("ip address 192.168." + str(j) + "." + str(ai) + " 255.255.255.0\n")
			tn.write("no shut\n")

		tn.write("end\n")

		for k in range(50,86,5):
		# Configure DHCP and DNS on VLAN's 50,55,60,65,70,75,80 & 85

			tn.write("conf t\n")
			tn.write("ip dhcp exclude 192.168." + str(k) + ".1 192.168." + str(k) + ".15\n")
			tn.write("ip dhcp pool VLAN" + str(k) + "\n")
			tn.write("network 192.168." + str(k) + ".0 255.255.255.0\n")
			tn.write("defau 192.168." + str(k) + ".254\n")
			tn.write("domain Anthonie.com\n")
			tn.write("dns 8.8.8.8\n")
			tn.write("end\n")

		# Configure HSRP 
		tn.write("conf t\n")
		for l in range(50, 86, 5):
			tn.write("int vlan " + str(l) + "\n")
			tn.write("standby " + str(l) + " ip 192.168." + str(l) + ".254\n")
			tn.write("exit\n")


		tn.write("end\n")
		tn.write("exit\n")

		print (tn.read_all())

# Switches 11 & 12 and VLAN's 50,55,60 & 65 on the ACCESS LAYER
for f in range(11,13):

		HOST = "192.168.1." + str(f)

		tn = telnetlib.Telnet(HOST)

		tn.read_until("Username: ")
		tn.write(user + "\n")
		if password:
			tn.read_until("Password: ")
			tn.write(password + "\n")

		tn.write("conf t\n")
		for i in range(50,66,5):

			tn.write("vlan " + str(i) + "\n")
			tn.write("name Anthonie_VLAN_" + str(i) + "\n")

		tn.write("end\n")
		tn.write("exit\n")
		print (tn.read_all())

# Switches 13 & 14 and VLAN's 70,75,80 & 85 on the ACCESS LAYER
for g in range(13,15):
		HOST = "192.168.1." + str(g)

		tn = telnetlib.Telnet(HOST)

		tn.read_until("Username: ")
		tn.write(user + "\n")
		if password:
			tn.read_until("Password: ")
			tn.write(password + "\n")

		tn.write("conf t\n")
		for i in range(70,86,5):
			tn.write("vlan " + str(i) + "\n")
			tn.write("name Anthonie_VLAN_" + str(i) + "\n")

		tn.write("end\n")
		tn.write("exit\n")

		print (tn.read_all())

# Configure OSPF on Switches 1 - 4,9 & 10 (CORE & DISTRIBUTION layer)
for f in list(range(1,5)) + list(range(9,11)):

		HOST = "192.168.1." + str(f)
		number = f

		tn = telnetlib.Telnet(HOST)

		tn.read_until("Username: ")
		tn.write(user + "\n")
		if password:
			tn.read_until("Password: ")
			tn.write(password + "\n")

		# Configure OSPF
		tn.write("conf t\n")
		tn.write("router ospf 1\n")
		tn.write("router-id " + str(number) + "." + str(number) + "." + str(number) + "." + str(number) + "\n")
		tn.write("net 0.0.0.0 0.0.0.0 area 0\n")
		tn.write("end\n")
		tn.write("exit\n")

		print (tn.read_all())

# Cofigure STP on Switcher ( 14 - 1 [Reversed] )
for stp in reversed(range(1,15)):

		HOST = "192.168.1." + str(stp)

		tn = telnetlib.Telnet(HOST)

		tn.read_until("Username: ")
		tn.write(user + "\n")
		if password:
			tn.read_until("Password: ")
			tn.write(password + "\n")

		tn.write("conf t\n")
		tn.write("spanning-tree mode rapid-pvst\n")
		tn.write("end\n")
		tn.write("exit\n")

		print (tn.read_all())