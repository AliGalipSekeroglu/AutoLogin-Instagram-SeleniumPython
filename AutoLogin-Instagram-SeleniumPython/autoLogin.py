from selenium import webdriver
import time
import loginInfo

browser = webdriver.Firefox() #Starting Firefox Browser
url="https://www.instagram.com/"

browser.get(url) 

time.sleep(3) #Waiting 3 seconds after we open the page.

#Login element
login = browser.find_element_by_xpath ("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
login.click()
time.sleep (2)

"""
On the first project of me which we entered Twitter without using password,we use XPaths of
elements but in Instagram,when we refresh our website,id number of login url changes so we need
to use something different to use that link through Python Selenium. Either we can choose class name
or name selectors to use that.
"""
username=browser.find_element_by_name ("username")
username.send_keys (loginInfo.username)

password =browser.find_element_by_name ("password")
password.send_keys(loginInfo.password)

#Logging in Instagram through our password and surname which is saved under loginInfo.py file.
login_button = browser.find_element_by_xpath ("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/span/button")
login_button.click()
time.sleep(10)
                        


browser.close()
