import common


def create_user(name, password,  optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'create-user', positional_args=[name, password],
        optional_args=optional_args)
    return out, err


def delete_user(name, input_data='y\n', optional_args=dict()):
    print " input data in delete_user is %s" % input_data
    out, err = common.frame_command(
        'hcf', 'delete-user', positional_args=[name],
        input_data=input_data, optional_args=optional_args)
    return out, err
