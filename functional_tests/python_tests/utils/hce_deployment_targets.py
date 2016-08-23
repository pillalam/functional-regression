import common


def create_deployment_target(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'create-deployment-target', optional_args=optional_args)
    return out, err


def update_deployment_target(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'update-deployment-target', optional_args=optional_args)
    return out, err


def get_deployment_target(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'get-deployment-target', optional_args=optional_args)
    return out, err


def list_deployment_targets(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'list-deployment-targets', optional_args=optional_args)
    return out, err


def delete_deployment_target(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'delete-deployment-target', optional_args=optional_args)
    return out, err
