import common


def list_catalogs(catalog_host, headers):
    url = "v1/catalogs"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    headers = {'Authorization': headers}
    return common.send_request(req_url, method='GET', headers=headers)


def show_catalog(catalog_host, catalog_id, headers):
    url = "v1/catalogs" + "/" + catalog_id
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    headers = {'Authorization': headers}
    return common.send_request(req_url, method='GET', headers=headers)


def list_services(catalog_host, headers):
    url = "v1/services"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    headers = {'Authorization': headers}
    return common.send_request(req_url, method='GET', headers=headers)


def show_service(catalog_host, service_id, headers):
    url = "v1/services" + "/" + service_id
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    headers = {'Authorization': headers}
    return common.send_request(req_url, method='GET', headers=headers)


def list_service_versions(catalog_host, service_id, headers):
    url = "v1/services" + "/" + service_id + "/" + "versions"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    headers = {'Authorization': headers}
    return common.send_request(req_url, method='GET', headers=headers)


def show_service_version(catalog_host, service_id, version, headers):
    url = "v1/services" + "/" + service_id + "/" + "versions" + "/" + version
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    headers = {'Authorization': headers}
    return common.send_request(req_url, method='GET', headers=headers)


def list_categories():
    url = "v1/categories"
    catalog_host = "http://" + catalog_host
    req_url = '%s/%s' % (catalog_host, url)
    return common.send_request(req_url, method='GET')
