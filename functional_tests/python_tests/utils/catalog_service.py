import common


def list_service(catalog_host):
    url = "v1/services"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='GET')
