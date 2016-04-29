import common


def list_services(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'services', optional_args=optional_args)
    return out, err
