import time
import pymongo
import pytest
from selenium.common.exceptions import WebDriverException
from utils.webdriver_instence_setup import webdriver_instance
from common.actions import Actions
from test_data import test_data as TD
from selenium.webdriver.common.keys import Keys
@pytest.fixture()
def driver():
    driver = webdriver_instance()
    action = Actions(driver)
    driver.get("http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/")

    # MongoDB connection
    connection_string = "mongodb+srv://qa_agency:!5szveK7%24TE%2493u@cluster0.qnr3p.mongodb.net/"
    client = pymongo.MongoClient(connection_string)
    db = client['trado_qa']
    collection = db['adminusers']


    logic_bar = action.find_element(TD.login)

    logic_bar.send_keys(Keys.CONTROL + 'a')
    logic_bar.send_keys(Keys.BACKSPACE)

    logic_bar.send_keys(Keys.CONTROL + 'a')
    logic_bar.send_keys(Keys.BACKSPACE)

    logic_bar.send_keys(TD.phone)
    logic_btn = action.find_element(TD.login_btn)
    logic_btn.click()

    # Find user data from MongoDB
    users = collection.find({"phone": TD.phone})
    driver.implicitly_wait(3)
    # Perform login actions
    for user in users:
        login_code = user.get("loginCode")
        print(login_code)
        driver.implicitly_wait(5)

        code_bar = action.find_element(TD.code)
        code_bar.send_keys(login_code)

        logicode_btn = action.find_element(TD.code_btn)
        logicode_btn.click()

    yield driver
    driver.close()
    driver.quit()
