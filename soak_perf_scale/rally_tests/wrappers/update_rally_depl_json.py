#!/usr/bin/python

"""
This script will update the rally deployment json file based on
environment variables (rc file) OS_AUTH_URL, OS_USERNAME, OS_PASSWORD
OS_PROJECT_NAME, RALLY_HTTPS_INSECURE, RALLY_HTTPS_CACERT, RALLY_TIMEOUT
"""

import os
import json
import argparse
from urlparse import urlparse

parser = argparse.ArgumentParser(
    description='Update Rally deployment Json file.')
parser.add_argument('-j', '--jsonfile', help='json file path', required=True)

parser_args = parser.parse_args()
jsonfile = parser_args.jsonfile

auth_url = os.getenv('OS_AUTH_URL', None)
username = os.getenv('OS_USERNAME', None)
password = os.getenv('OS_PASSWORD', None)
tenant_name = os.getenv('OS_PROJECT_NAME', None)
https_insecure = os.getenv('RALLY_HTTPS_INSECURE', "false")
https_insecure = json.loads(https_insecure)
https_cacert = os.getenv('RALLY_HTTPS_CACERT', "None")
timeout = os.getenv('RALLY_TIMEOUT', 300)

users_default_val = '[{"username": "%s"\
, "password": "%s", "tenant_name": "%s"}]'\
                    % (username, password, tenant_name)
users = os.getenv('RALLY_USERS', users_default_val)
users = json.loads(users)

with open(jsonfile, "r+") as fileobj:
    data = json.load(fileobj)
    for key in data:
        if key == "auth_url":
            data[key] = auth_url
        if key == "admin":
            admin = json.dumps(data[key])
            admin = json.loads(admin)
            for key2 in admin:
                if key2 == "username":
                    data[key][key2] = username
                if key2 == "password":
                    data[key][key2] = password
                if key2 == "tenant_name":
                    data[key][key2] = tenant_name
        if key == "https_insecure":
            data[key] = https_insecure
        if key == "https_cacert":
            data[key] = https_cacert
        if key == "timeout":
            data[key] = timeout
        if key == "users":
            data[key] = users

    fileobj.seek(0)
    fileobj.write(json.dumps(data))
    fileobj.truncate()
