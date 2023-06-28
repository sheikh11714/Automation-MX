from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login import Login
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("http://172.20.12.43/")

login = Login(driver=driver)
login.enter_username("sabadmin")
login.enter_password("sabadmin")
login.click_on_Login_button()
time.sleep(2)
