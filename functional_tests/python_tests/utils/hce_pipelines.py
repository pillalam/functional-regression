import common


def create_pipeline_task(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'create-pipeline-task', optional_args=optional_args)
    return out, err


def update_pipeline_task(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'update-pipeline-task', optional_args=optional_args)
    return out, err


def list_pipeline_tasks(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'list-pipeline-tasks', optional_args=optional_args)
    return out, err


def delete_pipeline_task(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'delete-pipeline-task', optional_args=optional_args)
    return out, err


def trigger_pipeline(optional_args=dict()):
    out, err = common.frame_command(
        'hce', 'trigger-pipeline', optional_args=optional_args)
    return out, err
