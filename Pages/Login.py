import time


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.Login_button_xpath = "//span[.='Login']"

    def enter_username(self, username):
        self.driver.find_element("name", self.username_textbox_name).sendkeys(username)

    def enter_password(self, password):
        self.driver.find_element("name", self.password_textbox_name).sendkeys(password)

    def click_on_Login_button(self):
        self.driver.find_element("xpath", self.Login_button_xpath).click()
        time.sleep(2)


