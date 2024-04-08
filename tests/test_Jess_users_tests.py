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

    autocomplete_option_select = actions.find_element(TD.autocomplete_option)
    autocomplete_option_select.click()

    final_add_button = actions.find_element(TD.final_add_btn)
    final_add_button.click()

    time.sleep(3)

    success_message = actions.find_element(TD.success_message)
    inner_text_success_message = success_message.get_attribute('innerText')

    assert inner_text_success_message == 'user created successfully'


@pytest.mark.parametrize(PD.test_try_invalid_new_user_keys, PD.test_try_invalid_new_user_values)
def test_try_invalid_new_user(driver, phone_number_id, shops_id, phone_number_value, shops_value):
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

    autocomplete_option_select = actions.find_element(TD.autocomplete_option)
    autocomplete_option_select.click()

    final_add_button = actions.find_element(TD.final_add_btn)
    final_add_button.click()

    time.sleep(3)

    success_message = actions.find_element(TD.success_message)
    inner_text_success_message = success_message.get_attribute('innerText')

    assert inner_text_success_message == 'מס׳ טלפון לא תקין'


@pytest.mark.parametrize(PD.test_search_by_user_keys, PD.test_search_by_user_values)
def test_search_by_user(driver, search_value, xpath, attribute):
    actions = Actions(driver)
    driver.implicitly_wait(5)

    users = actions.find_element(TD.users_btn)
    users.click()
    time.sleep(3)

    search_bar = actions.find_element(TD.search_bar)
    search_bar.send_keys(search_value)

    elements = driver.find_elements(TD.elements)
    for element in elements:
        element.click()
        element_xpath = element.find_element(By.XPATH, xpath)
        element_inner_text = element_xpath.get_attribute(attribute)
        assert search_value == element_inner_text


@pytest.mark.parametrize(PD.edit_user_keys,PD.edit_user_values)
def test_edit_user(driver, edit_id, edit_value):
    actions = Actions(driver)
    driver.implicitly_wait(5)

    users = actions.find_element(TD.users_btn)
    users.click()
    time.sleep(3)

    row = find_row_by_index(driver, 2)
    row.click()

    update_next_btn = actions.find_element(TD.next_first_btn_etrade)
    update_next_btn.click()

    edit_element = actions.find_element(edit_id)

    edit_element.send_keys(Keys.CONTROL + 'a')
    edit_element.send_keys(Keys.BACKSPACE)

    edit_element.send_keys(edit_value)

    submit_btn = actions.find_element(TD.submit_etrade_update_btn)
    submit_btn.click()
    submit_btn.click()
    submit_btn.click()
    submit_btn.click()

    row = find_row_by_index(driver, 2)
    row.click()
    update_next_btn = actions.find_element(TD.next_first_btn_etrade)
    update_next_btn.click()

    edit_id_default_value = actions.find_element(edit_id).get_attribute('value')
    assert edit_id_default_value == edit_value
