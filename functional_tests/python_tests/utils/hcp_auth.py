import common


def connect_target(api_url, optional_args=dict()):
    out, err = common.frame_command(
        'hcp', 'api', positional_args=[api_url],
        optional_args=optional_args)
    return out, err


def login(user, optional_args=dict()):
    out, err = common.frame_command(
        'hcp', 'login', positional_args=[user],
        optional_args=optional_args)
    return out, err
