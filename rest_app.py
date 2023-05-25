import os
import signal
from flask import Flask, request
from db_connector import ConnectionDb


# Create a class to extend Flask with db_connector class
class MyApp(Flask):
    def __init__(self, name):
        super().__init__(name)
        self.db = ConnectionDb()


app = MyApp(__name__)


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        user_data = app.db.get_user(user_id)

        # Check if the user id is exists, if not exists return ERROR else return OK with the user name
        if user_data == '':
            return {'status': 'error', 'reason': 'no such id'}, 500

        else:
            return {'status': 'ok', 'user_name': user_data[1]}, 200

    elif request.method == 'POST':
        user_data = app.db.get_user(user_id)

        # Check if the user id is exists, if not exists add user to DB and return OK else return ERROR
        if user_data == '':
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            # Add user name to DB
            app.db.add_user(user_id, user_name)

            return {'status': 'ok', 'user_added': user_name}, 200

        else:
            return {'status': 'error', 'reason': 'id already exists'}, 500

    elif request.method == 'PUT':
        user_data = app.db.get_user(user_id)

        # Check if the user id is exists, if not exists return ERROR else update user name and return OK
        if user_data == '':
            return {'status': 'error', 'reason': 'no such id'}, 500

        else:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')

            app.db.update_user(user_id, user_name)

            return {'status': 'ok', 'user_updated': user_name}, 200

    elif request.method == 'DELETE':
        user_data = app.db.get_user(user_id)

        # Check if the user id is exists, if not exists return ERROR else delete user and return OK
        if user_data == '':
            return {'status': 'error', 'reason': 'no such id'}, 500

        else:
            app.db.delete_user(user_id)
            return {'status': 'ok', 'user_deleted': user_data[1]}, 200


# supported methods
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
