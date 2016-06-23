import common


def connect_target(api_url, optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'api', positional_args=[api_url],
        optional_args=optional_args)
    return out, err


def login(username, password, optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'login', positional_args=[username, password],
        optional_args=optional_args)
    return out, err


def logout(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'logout',
        optional_args=optional_args)
    return out, err
