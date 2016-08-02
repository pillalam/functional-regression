import subprocess
import common
from git import Repo
import os
import shutil
import stat


def list_apps(optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'apps', optional_args=optional_args)
    return out, err


def downloadApplication(appCloneLocation, appDirectoryName):
    if os.path.exists(appDirectoryName):
        shutil.rmtree(appDirectoryName)
    os.mkdir(appDirectoryName)
    Repo.clone_from(appCloneLocation, appDirectoryName)
    out, err = common.executeShellCommand(
        'chmod -R 777 ' + str(appDirectoryName))
    return out, err


def push_app(app_name, app_path, optional_args=dict()):
    cmd = common.frame_command_nonexecuteshell(
        'hcf', 'push', positional_args=[app_name],
        optional_args=optional_args)
    print cmd
    cmd1 = 'cd ' + app_path + ';' + cmd + '\t'
    print cmd1
    out, err = common.executeShellCommand(cmd1)
    return out, err


def scale_app(app_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'scale', positional_args=[app_name],
        optional_args=optional_args)
    return out, err


def delete_app(app_name, input_data='y\n', optional_args=dict()):
    print " input data in delete_app is %s" % input_data
    out, err = common.frame_command(
        'hcf', 'delete', positional_args=[app_name],
        input_data=input_data, optional_args=optional_args)
    return out, err


def feature_flag(feature_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'feature-flag', positional_args=[feature_name],
        optional_args=optional_args)
    return out, err


def enable_feature_flag(feature_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'enable-feature-flag', positional_args=[feature_name],
        optional_args=optional_args)
    return out, err


def push_docker_app(docker_app_name, optional_args=dict()):
    out, err = common.frame_command(
        'hcf', 'push', positional_args=[docker_app_name],
        optional_args=optional_args)
    return out, err


def show_app(app_name, optional_args=dict()):
    out, err = common.frame_command(
        "hcf", 'app', positional_args=[app_name],
        optional_args=optional_args)
    return out, err
