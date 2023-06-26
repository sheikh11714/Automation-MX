from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://google.com")
sleep(2)