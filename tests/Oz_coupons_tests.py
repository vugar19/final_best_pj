import time
from selenium.webdriver.common.by import By
import pytest
import os
from common.actions import Actions
from test_data import test_data as TD
from selenium.webdriver.common.action_chains import ActionChains
from test_data import parametized_data as PD
@pytest.mark.skip
@pytest.mark.parametrize("name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id,validation_message",PD.test_4_2_add_invalid)
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

    assert validation_text == 'Please fill in this field.'


@pytest.mark.skip
@pytest.mark.parametrize("name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id",PD.test_4_2_add_valid)
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



@pytest.mark.parametrize("search_value,xpath,attribute",PD.test_4_4_search_by)
def test_4_4_search_by(driver,search_value,xpath,attribute):
    actions = Actions(driver)

    search_bar = actions.find_element(TD.search_bar)
    search_bar.send_keys(search_value)

    elements = driver.find_elements(TD.elements)
    for element in elements:
        element.click()
        element_xpath = element.find_element(By.XPATH,xpath)
        element_inner_text = element_xpath.get_attribute(attribute)
        assert search_value == element_inner_text




# @pytest.mark.parametrize("edit_id,edit_value",[
#     (TD.edit_name,'not_hello'),
#     (TD.edit_code,'not_hello'),
#     (TD.edit_min_cart_range,'not_hello'),
#     (TD.edit_discount_value,'not_hello')
# ])
# def test_4_5_edit_coupon(driver,edit_id,edit_value):
#     actions = Actions(driver)
#     element = actions.find_element(TD.element)
#     element.click()
#
#     edit_id = actions.find_element(edit_id)
#     edit_value = edit_id.send_keys(edit_value)
#
#     submit_btn = actions.find_element(TD.submit)
#     submit_btn.click()
#
#     element = actions.find_element(TD.element)
#     element.click()
#
#     edit_id_inner = actions.find_element(edit_id).get_attribute('innerText')
#     assert edit_id_inner == edit_value






