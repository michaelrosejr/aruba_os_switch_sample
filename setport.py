from arubaos_switch_api_python import loginOS, common, ports
import logging

data = {
    "ip": "10.0.1.16",
    "user": "manager",
    "password": "Aruba123",
    "DEBUG": 1
}
port = '11'
state = 'up'


if bool(data["DEBUG"]):
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
else:
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)



cookie_header = loginOS.login_os(data)   
logging.debug(cookie_header)

current = ports.set_port_status(data, cookie_header, port, "true")
print(current)

loginOS.logout(data, cookie_header)