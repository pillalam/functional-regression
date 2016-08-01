import common


def connect_target(api_url, optional_args=dict()):
    out, err = common.frame_command(
        'hsm', 'api', positional_args=[api_url],
        optional_args=optional_args)
    return out, err


def login(optional_args=dict()):
    out, err = common.frame_command(
        'hsm', 'login --skip-ssl-validation',
        optional_args=optional_args)
    return out, err
