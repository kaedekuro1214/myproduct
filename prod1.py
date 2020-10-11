from selenium import webdriver

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("http://www.yahoo.co.jp")

elem_search_word = driver.find_element_by_id("srchtxt")
elem_search_word.send_keys("selenium")
elem_search_btn = driver.find_element_by_id("srchbtn")
elem_search_btn.click()
