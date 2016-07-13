import common


def connect_target(cluster_url, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'api', positional_args=[cluster_url],
        optional_args=optional_args)
    return out, err


def login(input_data='n\n', optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'login', optional_args=optional_args)
    return out, err


def logout(cluster_url, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'logout', positional_args=[cluster_url],
        optional_args=optional_args)
    return out, err


def target(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'target', optional_args=optional_args)
    return out, err

def hsm_api(hsm_endpoint):
    out, err = common.frame_command(
        'hcf_hsm', 'api',  positional_args=[hsm_endpoint])
    return out, err
