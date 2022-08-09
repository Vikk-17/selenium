from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome("path_to_the_driver")
#print(chrome_browser)

# to maximixe window
# chrome_browser.maximize_window()

# open the browser and load the page at the given url
# browser.get("http://selenium.dev/")

# load google homepage and search for selenium and then close the browser
# browser.get('https://www.google.com')
# assert 'Google' in browser.title

# elem = browser.find_element(By.name, 'p') # find the search box
# elem.send_keys('selenium' + Keys.RETURN)

# browser.quit() # or .close()


# browser.maximize_window()
browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
show_msg_button = browser.find_element(By.CLASS_NAME, 'btn-default')
# print(show_msg_button.get_attribute('innerHTML'))
# browser.find_element(By.CSS_SELECTOR, '#get-inout > .btn')
usr_msg = browser.find_element(By.ID, 'user-message')
usr_msg.clear()
usr_msg.send_keys('I am testing')

show_msg_button.click()

output_msg = browser.find_element(By.ID, 'display')

assert "I am extra cool" in output_msg.text