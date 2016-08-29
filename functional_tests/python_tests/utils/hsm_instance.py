import os
import common
import json


def list_instances(catalog_host, headers):
    url = "v1/instances"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    headers = {'Authorization': headers}
    return common.send_request(req_url, method='GET', headers=headers)


def show_instance(catalog_host, instance_id, headers):
    url = "v1/instances" + "/" + instance_id
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    headers = {'Authorization': headers}
    return common.send_request(req_url, method='GET', headers=headers)


def create_instance(catalog_host, instance_id, service_id, labels,
                    product_version, sdl_version, description,
                    headers, **kwargs):
    data = {}
    request_data = {
                       "instance_id": instance_id,
                       "description": description,
                       "service_id": service_id,
                       "product_version": product_version,
                       "sdl_version": sdl_version,
                       "labels": labels
                   }
    if kwargs.get('parameters'):
        data = kwargs.get('parameters')
        request_data['parameters'] = data
    body = json.dumps(request_data)
    headers = {'Content-Type': 'application/json', 'Authorization': headers}
    url = "v1/instances"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='POST',
                               body=body, headers=headers)


def delete_instance(catalog_host, instance_id, headers):
    url = "v1/instances" + "/" + instance_id  
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    headers = {'Authorization': headers}
    return common.send_request(req_url, method='DELETE', headers=headers)

def configure_instance(catalog_host, instance_id, service_id,
                       description, product_version, sdl_version,
                       vendor, headers, **kwargs):
    parameters = []
    if kwargs.get('parameters'):
        parameters = kwargs.get('parameters')
    post_body = {
                    "service_id": service_id,
                    "description": description,
                    "product_version": product_version,
                    "sdl_version": sdl_version,
                    "vendor": vendor,
                    "parameters": parameters
                }
    body = json.dumps(post_body)
    headers = {'Content-Type': 'application/json', 'Authorization': headers}
    url = "v1/instances" + "/" + instance_id
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='PUT',
                               body=body, headers=headers)
