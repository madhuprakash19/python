from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
driver = webdriver.Chrome('/home/madhu/Downloads/chromedriver') 
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
target = '"Knchi"'
string = "Message sent using Python!!!"
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click() 
msg_box = driver.find_element_by_class_name('_3uMse')
msg_box.send_keys(string + Keys.ENTER)
