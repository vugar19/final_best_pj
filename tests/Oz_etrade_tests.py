import re
import time
from common.actions import *
from selenium.webdriver.common.by import By
import pytest
from common.actions import Actions
from test_data import test_data as TD
from test_data import parametized_data as PD
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize('search_value,xpath',PD.test_11_3_search_etrade_by_values)
def test_11_3_search_etrade_by(driver,search_value,xpath):

    actions = Actions(driver)
    etrade = actions.find_element(TD.etrade)
    etrade.click()

    search_bar = actions.find_element(TD.search_bar)
    search_bar.send_keys(search_value)
    time.sleep(3)

    count_findings = actions.find_element(TD.count_findings).get_attribute('innerText')
    count_findings_number = re.search(r'\d+', count_findings)
    if count_findings_number:

        count_findings_number = int(count_findings_number.group())
        if count_findings_number > 0:

            tbodies = driver.find_elements(By.TAG_NAME,'tbody')
            for tbody in tbodies:
                rows = tbody.find_elements(By.TAG_NAME,"tr")
                for row in rows:
                    driver.implicitly_wait(3)
                    row.click()
                    element_xpath = row.find_element(By.XPATH,xpath)
                    element_inner_text = element_xpath.get_attribute('defaultValue')
                    assert search_value == element_inner_text
        else:
            assert False,'can\'t be found'




@pytest.mark.parametrize()
def test_4_5_edit_coupon(driver):
    actions = Actions(driver)
    coupons = actions.find_element(TD.coupons)
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

    edit_id_default_value = actions.find_element(edit_id).get_attribute('defaultValue')
    assert edit_id_default_value == edit_value




