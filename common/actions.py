from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_data import test_data as TD


def find_row_by_index(driver, index):
    tbodies = driver.find_elements(By.TAG_NAME, 'tbody')
    for tbody in tbodies:
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            if row.get_attribute('rowIndex') == str(index):
                return row





class Actions:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,selector):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(selector))
        return element


    def click_element(self,element):
        element.click()

    def send_keys(self,element,value):
        element.send_keys(value)

    def get_attr(self,element,attribute):
        requested_attribute = element.get_attribute(attribute)
        return requested_attribute

    def is_sorted_descending(self,lst):
        return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    def current_url(self,url):
        if self.driver.current_url == url:
            return 'True'
        else:
            return 'False'

    def input_text(self):
        code = input("Please enter the code: ")
        return code




