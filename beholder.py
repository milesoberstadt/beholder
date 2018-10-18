import socket
import json
import sys
import time
import requests
from json import JSONDecodeError
from errno import ECONNREFUSED

offline_hosts = {}
hosts_to_report = []

def portscan(target,port):
    try:
        # Create Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketTimeout = 5
        s.settimeout(socketTimeout)
        s.connect((target,port))
        print(f"{target}:{port} is open")
        return port
    except socket.error as err:
        if err.errno == ECONNREFUSED:
            return False

def check_host(target, port):
    online = portscan(target, port)
    host_url = target + ":" + str(port)
    if (online == False):
        #offline_hosts.append(host["ip"])
        if host_url in offline_hosts:
            offline_hosts[host_url]["times_offline"] += 1
        else:
            host["times_offline"] = 1
            offline_hosts[host_url] = host
        if offline_hosts[host_url]["times_offline"] == config["attempts_before_report"]:
            hosts_to_report.append(host_url)
    else:
        if host_url in offline_hosts:
            del offline_hosts[host_url]

def notify_ifttt(offline_hosts, config):
    message = "\n".join(offline_hosts)
    message = "\n"+message
    options = config["notifier"]["ifttt"]
    url = "https://maker.ifttt.com/trigger/{}/with/key/{}".format(options["event_name"], options["api_key"])
    headers = {'Content-Type': 'application/json'}
    print(url)
    r = requests.post(url, data = {'value1': message})
    print(r.text)

if __name__ == "__main__":
    config = []
    with open("config.json") as f:
        try:
            config = json.load(f)
        except JSONDecodeError as e:
            print("Error parsing your config file, you could try validating it here: https://codebeautify.org/jsonvalidator")
            sys.exit(e)

    while (True):
        for host in config["hosts"]:
            if ('port' in host):
                check_host(host["ip"], int(host["port"]))
            elif ('ports' in host):
                for port in host['ports']:
                    check_host(host['ip'], int(port))

        if (len(hosts_to_report)):
            notify_ifttt(hosts_to_report, config)
            hosts_to_report = []
        sys.stdout.flush()
        # Wait 1 minute between checks
        time.sleep(10)
