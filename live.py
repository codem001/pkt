from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pyttsx3
import time

def automateYoutube(searchtext):


	path = "~/fox"

	url = "https://youtu.be/lmSrR4f0SLg"
	 
	driver = webdriver.Firefofx(path)
	driver.get(url)
  driver.implicitly_wait(10)
	webBrowser.execute_script("window.open('about:blank', 'secondtab');")
  driver.implicitly_wait(5)
	webBrowser.switch_to.window("secondtab")
  driver.implicitly_wait(2)
	webBrowser.get('url')
driver.implicitly_wait(1000)
