import common


def add_user(name, password, familyname, givenname, email,
     optional_args=dict()):
    out, err = common.frame_command(
        'hcp', 'add-user',
        positional_args=[name, password, familyname, givenname, email],
        optional_args=optional_args)
    return out, err

def update_user(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcp', 'update-user', positional_args=[name],
        optional_args=optional_args)
    return out, err

def delete_user(name, optional_args=dict()):
    out, err = common.frame_command(
        'hcp', 'delete-user', positional_args=[name],
        optional_args=optional_args)
    return out, err
