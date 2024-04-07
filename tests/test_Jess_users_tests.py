import time
import pytest
from test_data import parametized_data as PD
from common.actions import *
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize("phone_number, shops", [("972054111111", "test")])
def test_add_new_user(driver, phone_number, shops):
    driver.implicitly_wait(5)


    users_btn = driver.find_element(By.XPATH, "//button[text()='Users']")
    users_btn.click()

    menu = actions.find_element(TD.drop_down_manu)
    menu.click()

    add_user_btn = driver.find_element(By.XPATH, "//button[text()='Add User']")
    add_user_btn.click()


    phone_number_field = driver.find_element(By.ID, "phone_number")
    phone_number_field.send_keys(phone_number)

    shops_field = driver.find_element(By.ID, "shops")
    shops_field.send_keys(shops)


    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_btn.click()


    success_message = driver.find_element(By.ID, "success_message")
    inner_text_success_message = success_message.get_attribute('innerText')

    assert inner_text_success_message == 'User added successfully'
