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


driver = webdriver.Chrome()

url = "https://mahka.ir/cs/UserMgmt/19/%D9%88%D8%B1%D9%88%D8%AF-%D8%A8%D9%87-%D8%B3%D8%A7%DB%8C%D8%AA"
#url="18.64.141.58"
#driver = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe')
x="navbar-custom"
x="col-12"
    # locators
driver.get(url)

while True:
    try:

        driver.find_element(By.CLASS_NAME, x).send_keys('2131442344444444')
        print(2)
    except Exception:
        pass
