import time

import pytest
from utils.webdriver_instence_setup import webdriver_instance
import pymongo
from common.actions import Actions
from test_data import test_data as TD

@pytest.fixture()
def driver():
    driver = webdriver_instance()
    action = Actions(driver)
    driver.get("http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/")
    connection_string = "mongodb+srv://qa_agency:!5szveK7%24TE%2493u@cluster0.qnr3p.mongodb.net/"
    time.sleep(9)
    logic_bar = action.find_element(TD.login)
    logic_bar.send_keys(TD.phone)

    logic_btn = action.find_element(TD.login_btn)
    logic_btn.click()
    driver.implicitly_wait(5)

    client = pymongo.MongoClient(connection_string)
    db = client['trado_qa']
    collection = db['adminusers']
    users = collection.find({"phone":TD.phone})

    for user in users:
         login_code = user["loginCode"]
    logic_bar = action.find_element(TD.code)
    logic_bar.send_keys(login_code)

    logic_btn = action.find_element(TD.code_btn)
    logic_btn.click()

    yield driver
    driver.close()
    driver.quit()

