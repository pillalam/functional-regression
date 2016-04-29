import common


def create_quota(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'create-quota', positional_args=[name],
        optional_args=optional_args)
    return out, err


def delete_quota(name, input_data='y\n', optional_args=dict()):
    print " input data in delete_quota is %s" % input_data
    out, err = common.frame_command(
        'hcf', 'delete-quota', positional_args=[name],
        input_data=input_data, optional_args=optional_args)
    return out, err


def list_quotas(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'quotas', optional_args=optional_args)
    return out, err


def set_quota(org_name, quota_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'set-quota', positional_args=[org_name, quota_name],
        optional_args=optional_args)
    return out, err
