import requests


try:
    # Send a GET request to stop rest_app server
    requests.get(f'http://127.0.0.1:5000/stop_server')

    print(f'SUCCESS: rest_app is stopped')
except Exception as e:
    print(f'Error in stopping rest_app server\n{e}')


try:
    # Send a GET request to stop web_app server
    requests.get(f'http://127.0.0.1:5001/stop_server')

    print(f'SUCCESS: web_app is stopped')
except Exception as e:
    print(f'Error in stopping web_app server\n{e}')
