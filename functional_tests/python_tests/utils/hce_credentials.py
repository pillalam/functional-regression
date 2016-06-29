import common


def list_credentials(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'list-credentials', optional_args=optional_args)
    return out, err
