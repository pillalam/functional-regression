import common
import random
import json


def create_secgroup_rule_json():
    """
    :param jsonFileLocation: Location of json_create base file
    :returns: json file location
    """
    param_list = []
    param_dict = {}
    jsonFileName = "jsonFile" + str(random.randint(1024, 4096))
    param_dict["protocol"] = "tcp"
    param_dict["destination"] = "10.244.1.18"
    param_dict["ports"] = "3306"
    param_list.append(param_dict)
    with open(jsonFileName, 'w') as json_file:
        json.dump(param_list, json_file)
    json_file.close()
    return jsonFileName


def updated_secgroup_rule_json():
    """
    :param jsonFileLocation: Location of json_create base file
    :returns: json file location
    """
    param_list = []
    param_dict = {}
    jsonFileName = "jsonFile" + str(random.randint(1024, 4096))
    param_dict["protocol"] = "tcp"
    param_dict["destination"] = "10.244.1.19"
    param_dict["ports"] = "3306"
    param_list.append(param_dict)
    with open(jsonFileName, 'w') as json_file:
        json.dump(param_list, json_file)
    json_file.close()
    return jsonFileName


def create_security_group(secgroup, secgroup_path,  optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'create-security-group', positional_args=
        [secgroup, secgroup_path], optional_args=optional_args)
    return out, err


def list_security_groups(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'security-groups', optional_args=optional_args)
    return out, err


def update_security_group(secgroup, secgroup_path,  optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'update-security-group', positional_args=
        [secgroup, secgroup_path], optional_args=optional_args)
    return out, err


def delete_security_group(secgroup, input_data='y\n', optional_args=dict()):
    print " input data in delete_security group is %s" % input_data
    out, err = common.frame_command(
        'hcf', 'delete-security-group', positional_args=[secgroup],
        input_data=input_data, optional_args=optional_args)
    return out, err


def view_security_group(secgroup, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'security-group', positional_args=[secgroup],
        optional_args=optional_args)
    return out, err


def bind_security_group(secgroup, org, space, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'bind-security-group', positional_args=[secgroup, org, space],
        optional_args=optional_args)
    return out, err


def unbind_security_group(secgroup, org, space, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'unbind-security-group', positional_args=[secgroup, org, space],
        optional_args=optional_args)
    return out, err


def bind_staging_security_group(secgroup, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'bind-staging-security-group', positional_args=[secgroup],
        optional_args=optional_args)
    return out, err


def list_staging_security_groups(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'staging-security-groups', optional_args=optional_args)
    return out, err


def unbind_staging_security_group(secgroup, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'unbind-staging-security-group', positional_args=[secgroup],
        optional_args=optional_args)
    return out, err


def bind_running_security_group(secgroup, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'bind-running-security-group', positional_args=[secgroup],
        optional_args=optional_args)
    return out, err


def list_running_security_groups(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'running-security-groups', optional_args=optional_args)
    return out, err


def unbind_running_security_group(secgroup, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'unbind-running-security-group', positional_args=[secgroup],
        optional_args=optional_args)
    return out, err
