# Python script using Netmiko to capture running config from the CSR100v Router

import netmiko
import getpass
host = input("Which IOS Device would you like to connect to ?")
login = input("Enter Valid Username: ")
pwd = getpass.getpass("Enter Valid Password: ")
connection = netmiko.ConnectHandler(ip=host, device_type="cisco_ios", username="developer", password=pwd)
print(connection.send_command("show version"))
connection.disconnect()