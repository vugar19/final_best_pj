from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.webdriver import Options

def webdriver_instance():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument('disable-extensions')
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument('start-minimized')
    chrome_options.add_argument('disable-notifications')
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--disable-offline-load-stale-cache")
    chrome_options.add_argument("--disk-cache-size=0")
    chrome_options.add_argument("--media-cache-size=0")
    my_driver = webdriver.Chrome(options=chrome_options,service=service)
    return my_driver



