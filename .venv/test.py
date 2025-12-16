import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import os
import time
#driverpath=r"'/Users/mac/Downloads/chrome-mac-arm64/Google Chrome for Testing.app'"
# 创建 Chrome 驱动服务
#service = Service(driverpath)
# 加载浏览器驱动
#driver = webdriver.Chrome()
# 访问网址
#path = '/usr/local/bin/chromedriver'
# 设置ChromeDriver的路径
chrome_driver_path = '/usr/local/bin/chromedriver'
os.environ["PATH"] += os.pathsep + chrome_driver_path

# 使用ChromeDriver创建Chrome浏览器实例
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://www.baidu.com")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
baker = driver.find_element(By.ID, "chat-textarea")
baker.send_keys("bakerfdfd")
time.sleep(1)