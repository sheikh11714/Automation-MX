from Login import Login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://172.20.12.43")
driver.implicitly_wait(2)
login = Login(driver=driver)
login.enter_username("sabadmin")
login.enter_password("sabadmin")
login.click_on_Login_button()
sleep(2)
