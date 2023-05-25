from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


user_id = 25
driver_path = "C:/Users/tomer/Downloads/chromedriver_win32/chromedriver.exe"


# Initialize driver instance
driver = webdriver.Chrome(service=Service(driver_path))

driver.implicitly_wait(10)
driver.get(f'http://127.0.0.1:5001/users/get_user_data/{user_id}')
driver.maximize_window()

# Find user element by ID and handle cases where it's not found or multiple elements match
my_element = driver.find_elements(By.ID, value='user')

# Check how many elements was found
if len(my_element) == 0:
    print('user element not found')
    driver.quit()
    raise Exception("test failed")

elif len(my_element) == 1:
    user_name = my_element[0].text
    print(user_name)
    driver.quit()

else:
    print('too many user elements was found')
    driver.quit()
    raise Exception("test failed")
