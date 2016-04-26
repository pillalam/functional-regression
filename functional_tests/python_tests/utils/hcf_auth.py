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
