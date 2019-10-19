from arubaos_switch_api_python import loginOS, common, ports
import logging

"""
:Set switch IP
:username/password for switch
"""
data = {
    "ip": "10.0.1.16",
    "user": "manager",
    "password": "Aruba123",
    "DEBUG": 1
}

if bool(data["DEBUG"]):
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
else:
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

#
# Get the switch cookie
cookie_header = loginOS.login_os(data)   
logging.debug(cookie_header)

#
# Requesting a list of ports
#
r = ports.get_ports(data, cookie_header)
print(r.text)



#
# delete the API session from the switch
#
loginOS.logout(data, cookie_header)