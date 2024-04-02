import time

import pytest
import os
from common.actions import Actions
from test_data import test_data as TD
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.skip
@pytest.mark.parametrize("name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id,validation_message",[
                             (TD.add_form_name,"",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_name),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_code),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_min_cart_val),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_start_date),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'',TD.add_form_discount_ammount,'30',TD.add_form_types_precen,TD.add_form_end_date),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'',TD.add_form_types_precen,TD.add_form_discount_ammount),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30','',TD.add_form_types_precen),
                                     ])
def test_4_2_invalid(driver,name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id,validation_message):
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
@pytest.mark.parametrize("name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id",[
                             (TD.add_form_name,"hello_workd",TD.add_form_code,'123453',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/2024',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel)])
def test_4_2_valid(driver,name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id):
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


@pytest.mark.skip
def test_4_3_1(driver):
    actions = Actions(driver)
    driver.implicitly_wait(5)
    coupons = actions.find_element(TD.coupon_btn)
    coupons.click()
    time.sleep(3)
    download_directory = 'Downloads'
    menu = actions.find_element(TD.drop_down_manu)
    menu.click()

    export_btn = actions.find_element(TD.export_btn)
    export_btn.click()

    # Get the latest downloaded file
    list_of_files = os.listdir(download_directory)
    latest_file = max(list_of_files, key=os.path.getctime)

    # Check the file type
    file_extension = os.path.splitext(latest_file)[1]

    assert file_extension.lower() == ".csv", "File downloaded successfully but it is not a CSV file."


@pytest.mark.parametrize("search_value",[('NAME')])
def test_4_4(driver,search_value):
    actions = Actions(driver)
    if number of items > 1 save ok in a set else save bad
    and name in field is  save ok in a set else save bad
    if set equal ok pass
    else not pass







