import common
import json


def list_instances(catalog_host):
    url = "v1/instances"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='GET')


def show_instance(catalog_host, instance_id):
    url = "v1/instances" + "/" + instance_id
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='GET')


def create_instance(catalog_host, instance_name, service_id, version):
    request_data = {
                       "name": instance_name,
                       "description": instance_name + " server",
                       "service_id": service_id,
                       "version": version,
                       "labels": ["mysql", "CF", "dev"],
                       "parameters": [
                           {"name": "MYSQL_ROOT_PASSWORD", "value": "root123"}
                       ]
                   }
    body = json.dumps(request_data)
    headers = {'Content-Type': 'application/json'}
    url = "v1/instances"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='POST',
                               body=body, headers=headers)


def delete_instance(catalog_host, instance_id):
    url = "v1/instances" + "/" + "{" + instance_id + "}"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='DELETE')
