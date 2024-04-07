import re
import time
from common.actions import *
from selenium.webdriver.common.by import By
import pytest
from common.actions import Actions
from test_data import test_data as TD
from test_data import parametized_data as PD
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize(PD.test_18_3_search_info_pages_keys, PD.test_18_3_search_info_pages_values)
def test_18_3_search_info_pages(driver, search_value, xpath, attribute):
    actions = Actions(driver)

    info_pages = actions.find_element(TD.info_pages_tab)
    info_pages.click()

    search_bar = actions.find_element(TD.info_pages_search)
    search_bar.send_keys(search_value)

    time.sleep(3)

    count_findings = actions.find_element(TD.count_findings_info_pages).get_attribute('innerText')
    count_findings_number = re.search(r'\d+', count_findings)
    if count_findings_number:

        count_findings_number = int(count_findings_number.group())
        if count_findings_number > 0:

            tbodies = driver.find_elements(By.TAG_NAME, 'tbody')
            for tbody in tbodies:
                rows = tbody.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    driver.implicitly_wait(3)
                    row.click()
                    element_xpath = actions.find_element(xpath)
                    element_inner_text = element_xpath.get_attribute(attribute)
                    assert search_value == element_inner_text
        else:
            assert False, 'cant be found'

