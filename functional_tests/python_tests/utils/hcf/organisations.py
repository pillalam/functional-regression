from utils import common


def create_org(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'create-org', positional_args=[name],
        optional_args=optional_args)
    return out, err


def delete_org(name, input_data='y\n', optional_args=dict()):
    print " input data in delete_org is %s" % input_data
    out, err = common.frame_command(
        'hcf', 'delete-org', positional_args=[name],
        input_data=input_data, optional_args=optional_args)
    return out, err


def list_orgs(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'orgs', optional_args=optional_args)
    return out, err
