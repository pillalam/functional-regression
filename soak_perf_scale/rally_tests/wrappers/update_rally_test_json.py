#!/usr/bin/python

"""
This script will update Rally scenario json files based on args, runner
context which can pass by command line parameters
ex: ./update_rally_test_json.py [-h] -j JSONFILE -a ARGS -r RUNNER -c CONTEXT
"""

import json
import argparse

parser = argparse.ArgumentParser(description='Rally test json update script.')
parser.add_argument('-j', '--jsonfile', help='json file path',
                    required=True)
parser.add_argument('-a', '--args', help='args fields to update',
                    required=True)
parser.add_argument('-r', '--runner', help='runner fields to update',
                    required=True)
parser.add_argument('-c', '--context', help='context fields to update',
                    required=True)

parser_args = parser.parse_args()
jsonfile = parser_args.jsonfile
args = json.loads(parser_args.args)
runner = json.loads(parser_args.runner)
context = json.loads(parser_args.context)

with open(jsonfile, "r+") as fileobj:
    data = json.load(fileobj)
    for key in data:
        for key1 in data[key][0]:
            if key1 == "args":
                for arg_fields in args:
                    data[key][0][key1][arg_fields] = args[arg_fields]
            if key1 == "runner":
                for runner_fields in runner:
                    data[key][0][key1][runner_fields] = runner[runner_fields]
            if key1 == "context":
                for context_fields in context:
                    data[key][0][key1][context_fields] =\
                        context[context_fields]
    fileobj.seek(0)
    fileobj.write(json.dumps(data))
    fileobj.truncate()
