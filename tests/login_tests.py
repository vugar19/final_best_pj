import time

import pytest

from common.actions import Actions
from test_data import test_data as TD
from selenium.webdriver.common.action_chains import ActionChains
@pytest.mark.skip
def test_26_1_1(driver):
    assert driver.current_url == "http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/#/"

@pytest.mark.skip
def test_26_1_2(driver):
    action = ActionChains(driver)
    actions = Actions(driver)
    driver.implicitly_wait(5)
    logout = actions.find_element(TD.logout)
    action.move_to_element(logout).click()
    time.sleep(3)
    assert driver.current_url == "http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/#/"

