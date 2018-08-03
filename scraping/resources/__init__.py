from os import path

RESOURCES_DIR = path.dirname(path.abspath(__file__))
API_ROUTE_FILE = path.join(RESOURCES_DIR, 'api-route.yml')

assert path.exists(API_ROUTE_FILE), f'File {API_ROUTE_FILE} not found.'
