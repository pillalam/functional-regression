import subprocess
import re
import os
import ConfigParser
import time
import httplib2
import json

BASE_PATH = os.getcwd().split()[0]
HCF_CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
    BASE_PATH + '/config/hcf.conf'))
HCE_CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
    BASE_PATH + '/config/hce.conf'))
HCP_CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
    BASE_PATH + '/config/hcp.conf'))
HSM_CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
    BASE_PATH + '/config/hsm.conf'))
CONF_SECTION_CONN = 'command'
Config = ConfigParser.ConfigParser()


def frame_command(
        cli, action, input_data=None,
        positional_args=list(), optional_args=dict()):
    args_gap = " "
    if cli == 'hcf_hsm':
        Config.read(HCF_CONF_FILE)
        shell_command = Config.get(CONF_SECTION_CONN, 'hcf_hsm_command') + " "
    if cli == 'hcf':
        Config.read(HCF_CONF_FILE)
        shell_command = Config.get(CONF_SECTION_CONN, 'hcf_command') + " "
    if cli == 'hce':
        args_gap = ""
        Config.read(HCE_CONF_FILE)
        shell_command = Config.get(CONF_SECTION_CONN, 'hce_command') + " "
    if cli == 'hcp':
        args_gap = ""
        Config.read(HCP_CONF_FILE)
        shell_command = Config.get(CONF_SECTION_CONN, 'hcp_command') + " "
    if cli == 'hsm':
        Config.read(HSM_CONF_FILE)
        shell_command = Config.get(CONF_SECTION_CONN, 'hsm_command') + " "

    command = shell_command + action + " "

    # Appending positional parameters
    if len(positional_args) != 0:
        for value in positional_args:
            command = command + value + " "

    # Checking for optional parameters
    if optional_args is not None:
        for k in optional_args.keys():
            command = command + k + args_gap + optional_args[k] + " "
    out, err = executeShellCommand(command, input_arg=input_data)
    return out, err


def frame_command_nonexecuteshell(
        cli, action, input_data=None,
        positional_args=list(), optional_args=dict()):
    if cli == 'hdpctl':
        shell_command = Config.get(CONF_SECTION_CONN, 'hdpctl_command') + " "
    if cli == 'hcf':
        Config.read(HCF_CONF_FILE)
        shell_command = Config.get(CONF_SECTION_CONN, 'hcf_command') + " "

    command = shell_command + action + " "
    # Appending positional parameters
    if len(positional_args) != 0:
        for value in positional_args:
            command = command + value + " "

    # Checking for optional parameters
    if optional_args is not None:
        for k in optional_args.keys():
            command = command + k + " " + optional_args[k] + " "
    return command


def executeShellCommand(strCommand, input_arg=None):
    proc = subprocess.Popen(strCommand, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
    time.sleep(5)
    out, err = proc.communicate(input_arg)
    if err:
        print " The Command failed due to the following error:\n" + err
    else:
        pass
    return out, err


def send_request(req_url, method, body=None, headers=None):
    req = httplib2.Http('.cache', disable_ssl_certificate_validation=True)
    response, content = req.request(
        req_url, method=method, body=body, headers=headers)
    if method == "DELETE" or method =="PUT":
        return response, content
    else:
        return response, json.loads(content)
