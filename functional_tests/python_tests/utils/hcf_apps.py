import common


def list_apps(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'apps', optional_args=optional_args)
    return out, err


def push_app(app_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'push', positional_args=[app_name],
        optional_args=optional_args)
    return out, err
