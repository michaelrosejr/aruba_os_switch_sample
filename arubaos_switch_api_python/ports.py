from requests.packages.urllib3 import disable_warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

import requests
import json
import logging
from arubaos_switch_api_python import common

disable_warnings(InsecureRequestWarning)

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

def get_ports(data, cookie_header):
    """
    Get all ports on switch
    :param data: imported data dict with switch info 
    :param cookie_header: Parse cookie resulting from successful loginOS.login_os(baseurl)
    :return: a list of ports 
    """ 
    baseurl = "https://{}/rest/v4".format(data['ip'])
    url = baseurl + '/ports'
    headers = {'cookie': cookie_header}
    response = requests.get(url, verify=False, data="" , headers=headers)
    if response.status_code == 200:
        pass
    return(response)

def set_port_status(data, cookie_header, port, state):
    """
    Set port to a given status true or false
    :param data: imported data dict with switch info 
    :param port: switch port to change
    :param state: set port status to true/up or false/down 
    :param cookie_header: Parse cookie resulting from successful loginOS.login_os(baseurl)
    :return: a list of ports 
    """   
    baseurl = "https://{}/rest/v4".format(data['ip'])
    url = baseurl + '/ports/' + port
    data = {
        "uri": "/ports/" + port,
        "id": port,
        "is_port_enabled": str2bool(state)
    }
    headers = {'cookie': cookie_header}
    response = requests.put(url, verify=False, data=json.dumps(data), headers=headers)
    return(response)
