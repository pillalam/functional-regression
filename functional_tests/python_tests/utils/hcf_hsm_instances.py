import common


def list_service_instances(optional_args=dict()):
    out, err = common.frame_command(
        'hcf_hsm', 'list-service-instances', optional_args=optional_args)
    return out, err


def enable_service_instance(instance_name, cf_instance_name):
    out, err = common.frame_command(
        'hcf_hsm', 'enable-service-instance',
        positional_args=[instance_name, cf_instance_name])
    return out, err


def disable_service_instance(cf_instance_name):
    out, err = common.frame_command(
        'hcf_hsm', 'disable-service-instance',
        positional_args=[cf_instance_name])
    return out, err
