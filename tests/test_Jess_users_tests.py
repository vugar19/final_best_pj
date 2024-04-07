import time
import pytest

from common import actions
from test_data import parametized_data as PD
from common.actions import *
from selenium.webdriver.common.keys import Keys

@pytest.mark.parametrize(PD.test_add_new_user_keys, PD.test_add_new_user_values)
def test_add_new_user(driver, phone_number_id, shops_id, phone_number_value, shops_value):
    actions = Actions(driver)
    driver.implicitly_wait(5)

    users = actions.find_element(TD.users_btn)
    users.click()
    time.sleep(3)

    menu = actions.find_element(TD.drop_down_manu)
    menu.click()

    add_btn = actions.find_element(TD.add_btn)
    add_btn.click()

    phone_number_field = actions.find_element(phone_number_id)
    phone_number_field.send_keys(phone_number_value)

    shops_field = actions.find_element(shops_id)
    shops_field.send_keys(shops_value)

    final_add_button = actions.find_element(TD.final_add_btn)
    final_add_button.click()

    time.sleep(3)

    success_message = actions.find_element(TD.success_message)
    inner_text_success_message = success_message.get_attribute('innerText')

    assert inner_text_success_message == 'user created successfully'
