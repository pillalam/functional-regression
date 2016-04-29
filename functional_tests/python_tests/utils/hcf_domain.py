import common


def list_domain(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'domains', optional_args=optional_args)
    return out, err
