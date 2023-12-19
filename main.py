from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys
import os
import signal
import keyring

if len(sys.argv) < 2:
    cas_number = input('Enter CAS No. or reagent name >>>')
else:
    cas_number = sys.argv[1]

print('Search the reagent with ' + cas_number)

# driver = webdriver.Chrome()
# driver = webdriver.Chrome("/usr/local/bin/chromedriver")


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(3)
window_num = 0

#Nacalai
driver.maximize_window()
driver.switch_to.window(driver.window_handles[window_num])
driver.get("https://www.nacalai.co.jp/ss/ec/EC-srchtop.cfm")
# driver.find_element_by_xpath('//*[@id="srchwordAll"]').send_keys(cas_number)
target = driver.find_element(by=By.XPATH, value='//*[@id="srchwordAll"]').send_keys(cas_number)
# target = driver.find_element_by_xpath('//*[@id="formall"]/div[1]/div[3]')
target = driver.find_element(by=By.XPATH, value='//*[@id="formall"]/div[1]/div[3]')
# target = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/div[1]/dl/dd/form/div[1]/div[3]')
driver.execute_script("arguments[0].click();", target)
driver.get(driver.current_url.replace("&Kensu=20", "&Kensu=100"))
driver.refresh()
try:
    Select(driver.find_element_by_xpath('//*[@id="sortSelect"]')).select_by_value('5a')
except:
    pass

window_num = window_num + 1

#Wako
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[window_num])
driver.get("https://labchem-wako.fujifilm.com/jp/index.html")
# driver.find_element_by_xpath('//input[@id="search_box"]').send_keys(cas_number)
driver.find_element(by=By.XPATH, value='//input[@id="search_box"]').send_keys(cas_number)
# driver.find_element_by_xpath('//*[@id="suggestApp"]/div[1]/div/fieldset/label/input').click()
driver.find_element(by=By.XPATH, value='//*[@id="suggestApp"]/div[1]/div/fieldset/label/input').click()
time.sleep(1)
try:
    # Select(driver.find_element_by_xpath('//*[@id="select_siz"]')).select_by_value('option[2]')
    Select(driver.find_element(by=By.XPATH, value='//*[@id="select_siz"]')).select_by_value('option[2]')
    # driver.find_element_by_xpath('//*[@id="select_siz"]/option[2]').click()
except:
    pass
# try:
#     driver.find_element_by_xpath('//*[@id="product-list"]/div[3]/ul/li[1]/span').click()
# except:
#     pass

window_num = window_num + 1

#Kanto
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[window_num])
driver.get("https://cica-web.kanto.co.jp/CicaWeb/servlet/wsj.front.LogonSvlt")
# driver.find_element_by_xpath('//input[@name="text_search"]').send_keys(cas_number)
driver.find_element(by=By.XPATH, value='//input[@name="text_search"]').send_keys(cas_number)
# driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/div/div[1]/div/button[1]').click()
driver.find_element(by=By.XPATH, value='/html/body/form/div[1]/div[2]/div/div[1]/div/button[1]').click()

window_num = window_num + 1

#Kishida
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[window_num])
driver.get("http://www.kishida.co.jp/index.html")
Select(driver.find_element(by=By.XPATH, value='//*[@id="condition"]')).select_by_value('2')
driver.find_element(by=By.XPATH, value='//input[@name="word"]').send_keys(cas_number)
driver.find_element(by=By.XPATH, value='//*[@id="cond_search"]').click()

window_num = window_num + 1

driver.switch_to.window(driver.window_handles[0])
#kill chromedriver process
os.kill(driver.service.process.pid,signal.SIGTERM)