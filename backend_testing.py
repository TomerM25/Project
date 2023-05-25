import pymysql
import requests


user_id = 26
user_name = 'Tomer'
db_host = 'sql7.freemysqlhosting.net'
db_user = 'sql7620888'
db_pass = 'r3b4L5FbeQ'
db_schema_name = 'sql7620888'


# Send a POST request to create the user
req_post = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": user_name})


# Send a GET request to retrieve the user
req_get = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
req_get_data = req_get.json()
req_get_user_name = req_get_data.get('user_name')

# Check if the retrieved user name matches the expected user name
if req_get.status_code == '200' and user_name == req_get_user_name:
    print('SUCCESS: user name matches')

else:
    print('ERROR: user name does not match')
    raise Exception("test failed")


# Check if the user name is in the Database
try:
    # Establishing a connection to DB
    conn = pymysql.connect(host=db_host, port=3306, user=db_user, passwd=db_pass, db=db_schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    # Getting data from table “users”
    cursor.execute(f"SELECT * FROM users WHERE user_id={user_id};")

    # Check if data received from Database
    if cursor.rowcount == 0:
        print('ERROR: the user id is not exists')
        raise Exception("test failed")
    else:
        data = cursor.fetchone()
        if data[1] == user_name:
            print('SUCCESS: user name is matching to id')

        else:
            print('ERROR: the user name is not matching to id')
            raise Exception("test failed")

    cursor.close()
    conn.close()

except pymysql.Error as e:
    print(f'error in connection to DB:\n', e)
    raise Exception("test failed")
