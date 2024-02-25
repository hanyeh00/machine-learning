import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
from bs4 import BeautifulSoup
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
        #baseUrl = "https://setkava.ir/"
        driver = webdriver.Chrome()
        #driver.get(baseUrl)
        #time.sleep(30)


        url = 'https://setkava.ir'
        driver.get(url)
        #path="//*[@id=\"insForm"]/div[1]/div[10]/div/div[2]/div[2]/div[3]/div/select"
        time.sleep(50)
        x=driver.find_element(By.CLASS_NAME, "card-header bg-secondary text-white")
        driver.find_element(By.CLASS_NAME,"brands[44757][1]").send_keys("مطهر")

        print(x)
       # elementByLinkText = driver.find_element(By.PARTIAL_LINK_TEXT()



        #elementByPartialLinkText = driver.find_element(Fi)

        #if elementByPartialLinkText is not None:
         #   print("We found an element by Partial Link Text")

ff = FindByLinkText()
ff.test()