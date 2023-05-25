import pymysql
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


user_id = 25
user_name = 'Tomer'
db_host = 'sql7.freemysqlhosting.net'
db_user = 'sql7620888'
db_pass = 'r3b4L5FbeQ'
db_schema_name = 'sql7620888'
driver_path = "C:/Users/tomer/Downloads/chromedriver_win32/chromedriver.exe"


# Send a POST request to create the user
req_post = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": user_name})


# Send a GET request to retrieve the user
req_get = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
req_get_data = req_get.json()
req_get_user_name = req_get_data.get('user_name')

# Check if the retrieved user name matches the expected user name
if req_get.status_code == 200 and user_name == req_get_user_name:
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


# Test the UI element
driver = webdriver.Chrome(service=Service(driver_path))

driver.implicitly_wait(10)
driver.get(f'http://127.0.0.1:5001/users/get_user_data/{user_id}')
driver.maximize_window()

# Find user element by ID and handle cases where it's not found or multiple elements match
my_element = driver.find_elements(By.ID, value='user')

# Check how many elements was found
if len(my_element) == 1:
    elem_user_name = my_element[0].text
    if user_name == elem_user_name:
        print('SUCCESS: the user names are matching')
        driver.quit()
    else:
        print('ERROR: the user names are not matching')
        driver.quit()
        raise Exception("test failed")

elif len(my_element) == 0:
    print('user element not found')
    driver.quit()
    raise Exception("test failed")

else:
    print('too many user elements was found')
    driver.quit()
    raise Exception("test failed")
