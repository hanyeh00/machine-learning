import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome....
sr = Service(r"C:\Program Files\chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument('--headless')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
options.add_argument('headless')
options.add_argument('window-size=0x0')
chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"





class FindByLinkText():

    def test(self):
        baseUrl = "https://mahka.ir/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element(By.PARTIAL_LINK_TEXT,("ورود")).click()
        username=driver.find_element(By.ID,"l_username")
        username.send_keys("test")
        password=driver.find_element(By.ID,"l_password")
        password.send_keys(123456)
        login=driver.find_element(By.PARTIAL_LINK_TEXT,"ورود").click()
        time.sleep((15))


        #elementByPartialLinkText = driver.find_element(Fi)

        #if elementByPartialLinkText is not None:
         #   print("We found an element by Partial Link Text")

ff = FindByLinkText()
ff.test()