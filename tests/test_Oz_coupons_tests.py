import time
import pytest
from test_data import parametized_data as PD
from common.actions import *
from selenium.webdriver.common.keys import Keys

@pytest.mark.parametrize(PD.test_test_4_2_add_invalid_keys,PD.test_4_2_add_invalid_values)
def test_4_2_add_invalid(driver,name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id,validation_message):
    actions = Actions(driver)
    driver.implicitly_wait(5)
    coupons = actions.find_element(TD.coupon_btn)
    coupons.click()
    time.sleep(3)

    menu = actions.find_element(TD.drop_down_manu)
    menu.click()

    add_btn = actions.find_element(TD.add_btn)
    add_btn.click()

    name_field = actions.find_element(name_id)
    name_field.send_keys(name_value)

    code_field = actions.find_element(code_id)
    code_field.send_keys(code_value)

    min_cart_field = actions.find_element(min_cart_id)
    min_cart_field.send_keys(min_cart_value)

    start_date = actions.find_element(start_date_id)
    start_date.send_keys(start_date_value)

    end_date = actions.find_element(end_date_id)
    end_date.send_keys(end_date_value)

    discount_amount = actions.find_element(discount_amount_id)
    discount_amount.send_keys(discount_amount_value)

    discount_tyoe_manu = actions.find_element(TD.add_form_type)
    discount_tyoe_manu.click()

    discount_type = actions.find_element(discount_type_id)
    discount_type.click()

    final_add_button = actions.find_element(TD.final_add_btn)
    final_add_button.click()

    validation = actions.find_element(validation_message)
    validation_text = validation.get_attribute('validationMessage')

    assert validation_text == 'מס׳ טלפון לא תקין'



@pytest.mark.parametrize(PD.test_4_2_add_valid_keys,PD.test_4_2_add_valid_values)
def test_4_2_add_valid(driver,name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id):
    actions = Actions(driver)
    driver.implicitly_wait(5)
    coupons = actions.find_element(TD.coupon_btn)
    coupons.click()
    time.sleep(3)

    menu = actions.find_element(TD.drop_down_manu)
    menu.click()

    add_btn = actions.find_element(TD.add_btn)
    add_btn.click()

    name_field = actions.find_element(name_id)
    name_field.send_keys(name_value)

    code_field = actions.find_element(code_id)
    code_field.send_keys(code_value)

    min_cart_field = actions.find_element(min_cart_id)
    min_cart_field.send_keys(min_cart_value)

    start_date = actions.find_element(start_date_id)
    start_date.send_keys(start_date_value)

    end_date = actions.find_element(end_date_id)
    end_date.send_keys(end_date_value)

    discount_amount = actions.find_element(discount_amount_id)
    discount_amount.send_keys(discount_amount_value)

    discount_tyoe_manu = actions.find_element(TD.add_form_type)
    discount_tyoe_manu.click()

    discount_type = actions.find_element(discount_type_id)
    discount_type.click()

    final_add_button = actions.find_element(TD.final_add_btn)
    final_add_button.click()

    sucsess_mess = actions.find_element(TD.sucsess_mess)
    inner_text_success_mess = sucsess_mess.get_attribute('innerText')

    assert inner_text_success_mess == 'coupon created successfully'



@pytest.mark.parametrize(PD.test_4_4_search_by_keys,PD.test_4_4_search_by_values)
def test_4_4_search_by(driver,search_value,xpath,attribute):
    actions = Actions(driver)
    coupons = actions.find_element(TD.coupon_btn)
    coupons.click()
    search_bar = actions.find_element(TD.search_bar)
    search_bar.send_keys(search_value)

    elements = driver.find_elements(TD.elements)
    for element in elements:
        element.click()
        element_xpath = element.find_element(By.XPATH,xpath)
        element_inner_text = element_xpath.get_attribute(attribute)
        assert search_value == element_inner_text




@pytest.mark.parametrize(PD.edit_test_4_5_keys,PD.edit_test_4_5_values)
def test_4_5_edit_coupon(driver,edit_id,edit_value):
    actions = Actions(driver)
    coupons = actions.find_element(TD.coupon_btn)
    coupons.click()

    row = find_row_by_index(driver, 2)
    row.click()

    edit_element = actions.find_element(edit_id)

    edit_element.send_keys(Keys.CONTROL + 'a')
    edit_element.send_keys(Keys.BACKSPACE)

    edit_element.send_keys(edit_value)

    submit_btn = actions.find_element(TD.edit_submit_btn)
    submit_btn.click()

    row = find_row_by_index(driver,2)
    row.click()

    edit_id_default_value = actions.find_element(edit_id).get_attribute('value')
    assert edit_id_default_value == edit_value



