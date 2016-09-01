import common


def create_route(space, domain, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'create-route', positional_args=[space, domain],
        optional_args=optional_args)
    return out, err


def list_routes(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'routes', optional_args=optional_args)
    return out, err


def map_route(app, domain, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'map-route', positional_args=[app, domain],
        optional_args=optional_args)
    return out, err


def unmap_route(app, domain, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'unmap-route', positional_args=[app, domain],
        optional_args=optional_args)
    return out, err


def delete_orphaned_routes(input_data='y\n', optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'delete-orphaned-routes', input_data=input_data,
        optional_args=optional_args)
    return out, err


def check_route(host, domain, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'check-route', positional_args=[host, domain],
        optional_args=optional_args)
    return out, err


def delete_route(domain, input_data='y\n', optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'delete-route', positional_args=[domain],
        input_data=input_data, optional_args=optional_args)
    return out, err
