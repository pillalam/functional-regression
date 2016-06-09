import common


def list_domain(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'domains', optional_args=optional_args)
    return out, err


def create_domain(org_name, domain, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'create-domain', positional_args=[org_name, domain],
        optional_args=optional_args)
    return out, err


def delete_domain(domain, input_data='y\n', optional_args=dict()):
    print " input data in delete_domain is %s" % input_data
    out, err = common.frame_command(
        'hcf', 'delete-domain', positional_args=[name],
        input_data=input_data, optional_args=optional_args)
    return out, err
