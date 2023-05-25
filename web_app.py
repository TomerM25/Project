import os
import signal
from flask import Flask
from db_connector import ConnectionDb


# Create a class to extend Flask with db_connector class
class MyApp(Flask):
    def __init__(self, name):
        super().__init__(name)
        self.db = ConnectionDb()


app = MyApp(__name__)


# supported methods
@app.route('/users/get_user_data/<user_id>')
def get_user_data(user_id):
    user_data = app.db.get_user(user_id)

    if user_data == '':
        return f"<H1 id='error'> no such user: {user_id} </H1>", 500
    else:
        return f"<H1 id='user'> {user_data[1]} </H1>", 200


# supported methods
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5001)
