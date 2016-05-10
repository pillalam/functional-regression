import common


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
