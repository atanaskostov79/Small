from opencart_api import OpenCartAPI as oci

opencart_api = oci('https://eunimag.com/api/rest_admin/', 'kuramiqnko')
print(opencart_api.get('categories'))
print(opencart_api.get('products'))
