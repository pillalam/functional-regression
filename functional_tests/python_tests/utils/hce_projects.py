import common


def create_project(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'create-project', optional_args=optional_args)
    return out, err


def update_project(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'update-project', optional_args=optional_args)
    return out, err


def list_projects(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'list-projects', optional_args=optional_args)
    return out, err


def delete_project(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'delete-project', optional_args=optional_args)
    return out, err
