import os
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


def create_instance(catalog_host, instance_id,
                    service_id, labels, version, description, **kwargs):
    parameters = []
    data = {}
    request_data = {
                      "instance_id": instance_id,
                      "description": description,
                      "service_id": service_id,
                      "version": version,
                      "labels": labels
                   }
    if kwargs.get('parameters'):
        data = kwargs.get('parameters')
        parameters.append(data)
        request_data['parameters'] = parameters
    body = json.dumps(request_data)
    headers = {'Content-Type': 'application/json'}
    url = "v1/instances"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='POST',
                               body=body, headers=headers)


def delete_instance(catalog_host, instance_id):
    url = "v1/instances" + "/" + instance_id  
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='DELETE')
