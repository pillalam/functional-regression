#from utils import common
import common


def marketplace(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'marketplace',
        optional_args=optional_args)
    return out, err
