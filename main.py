from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

opts = FirefoxOptions()
# opts.add_argument("--headless")
opts.add_argument("maximize_window")
opts.set_preference("general.useragent.override", UserAgent().random)

service = FirefoxService(GeckoDriverManager().install())


driver = webdriver.Firefox(service=service, options=opts)
url = 'https://pagination.js.org/'
driver.get(url=url)

driver.maximize_window()
