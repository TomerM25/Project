import requests


# Send a GET request to stop rest_app server
requests.get(f'http://127.0.0.1:5000/stop_server')


# Send a GET request to stop web_app server
requests.get(f'http://127.0.0.1:5001/stop_server')
