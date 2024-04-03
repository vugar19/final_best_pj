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

                    update_next_btn = actions.find_element(TD.next_first_btn_etrade)
                    update_next_btn.click()

                    driver.implicitly_wait(3)
                    element_text = actions.find_element(xpath)
                    element_inner_text=element_text.get_attribute('value')

                    assert search_value == element_inner_text
        else:
            assert False,'can\'t be found'



@pytest.mark.parametrize(PD.edit_test_etrade_11_5_keys,PD.edit_test_etrade_11_5_values)
def test_11_5_edit_etrade(driver,edit_id, edit_value):
    actions = Actions(driver)
    etrade = actions.find_element(TD.etrade)
    etrade.click()

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

    row = find_row_by_index(driver,2)
    row.click()
    update_next_btn = actions.find_element(TD.next_first_btn_etrade)
    update_next_btn.click()

    edit_id_default_value = actions.find_element(edit_id).get_attribute('value')
    assert edit_id_default_value == edit_value
