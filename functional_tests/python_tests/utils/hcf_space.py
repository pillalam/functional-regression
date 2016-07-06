import common


def create_space(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'create-space', positional_args=[name],
        optional_args=optional_args)
    return out, err


def delete_space(name, input_data='y\n', optional_args=dict()):
    print " input data in delete_space is %s" % input_data
    out, err = common.frame_command(
        'hcf', 'delete-space', positional_args=[name],
        input_data=input_data, optional_args=optional_args)
    return out, err


def list_space(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'spaces', optional_args=optional_args)
    return out, err


def rename_space(old_name, new_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'rename-space', positional_args=[old_name, new_name],
        optional_args=optional_args)
    return out, err


def space(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'space', positional_args=[name],
        optional_args=optional_args)
    return out, err
