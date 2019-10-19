import json
import requests
import logging




def login_os(data):
    if bool(data["DEBUG"]):
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

    url = "https://{}/rest/v4".format(data['ip'])
    username = data['user']
    password = data['password']
    params = {'userName': username, 'password': password}
    proxies = {'http': None, 'https': None}
    url_login = url + "/login-sessions"
    response = requests.post(url_login, verify=False, data=json.dumps(params), proxies=proxies, timeout=3)
    if response.status_code == 201:
        logging.debug("Login to switch: {} is successful".format(url_login))
        session = response.json()
        r_cookie = session['cookie']
        return r_cookie
    else:
        logging.debug("Login to switch failed with status code: ".format(response.status_code))


def logout(data, cookie):
    if bool(data["DEBUG"]):
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

    url = "https://{}/rest/v4".format(data['ip'])
    url_login = url + "/login-sessions"
    headers = {'cookie': cookie}
    proxies = {'http': None, 'https': None}
    r = requests.delete(url_login, headers=headers, verify=False, proxies=proxies)
    if r.status_code == 204:
        logging.debug("Logged out! %s", r.status_code)
    else:
        logging.error("Logout is not successful: %s", r.status_code)
