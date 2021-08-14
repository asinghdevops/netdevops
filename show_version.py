# Python NEtmiko script to run IOS command on CSR1000v Router

import netmiko
connection = netmiko.ConnectHandler(ip="10.10.20.48", device_type="cisco_ios", username="developer", password="C1sco12345")

print(connection.send_command("show version"))
connection.disconnect()