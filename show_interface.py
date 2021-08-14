#Python script using Netmiko to run commands on CSR1000v

import netmiko

connection = netmiko.ConnectHandler(ip="10.10.20.48", device_type="cisco_ios", username="developer", password="C1sco12345")

print(connection.send_command("show ip int brief"))
connection.disconnect()