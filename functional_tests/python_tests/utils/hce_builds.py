import common


def get_build(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'get-build', optional_args=optional_args)
    return out, err


def get_build_logs(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'get-build-logs', optional_args=optional_args)
    return out, err


def list_builds(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'list-builds', optional_args=optional_args)
    return out, err


def list_build_events(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'list-build-events', optional_args=optional_args)
    return out, err
