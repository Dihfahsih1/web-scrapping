import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

service = Service('/usr/bin/chromedrivers')

service.start()

driver = webdriver.Remote(service.service_url)

driver.get('https://ksanahealth.com/mental-health-blog/');

time.sleep(15)

driver.quit()