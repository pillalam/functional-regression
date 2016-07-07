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


def quota_info(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'quota', positional_args=[name],
        optional_args=optional_args)
    return out, err


def set_quota(org_name, quota_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'set-quota', positional_args=[org_name, quota_name],
        optional_args=optional_args)
    return out, err


def set_target(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'target', optional_args=optional_args)
    return out, err


def update_quota(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'update-quota', positional_args=[name],
        optional_args=optional_args)
    return out, err


def create_space_quota(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'create-space-quota', positional_args=[name],
        optional_args=optional_args)
    return out, err


def update_space_quota(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'update-space-quota', positional_args=[name],
        optional_args=optional_args)
    return out, err


def space_quota_info(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'space-quota', positional_args=[name],
        optional_args=optional_args)
    return out, err


def set_space_quota(space_name, space_quota_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'set-space-quota',
        positional_args=[space_name, space_quota_name],
        optional_args=optional_args)
    return out, err


def list_space_quotas(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'space-quotas', optional_args=optional_args)
    return out, err


def unset_space_quota(space_name, space_quota_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'unset-space-quota',
        positional_args=[space_name, space_quota_name],
        optional_args=optional_args)
    return out, err


def delete_space_quota(name, input_data='y\n', optional_args=dict()):
    print " input data in delete_space_quota is %s" % input_data
    out, err = common.frame_command(
        'hcf', 'delete-space-quota', positional_args=[name],
        input_data=input_data, optional_args=optional_args)
    return out, err
