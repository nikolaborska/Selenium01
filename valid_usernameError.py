from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InvalidUserLoginError:
    
    url = "http://demostore.supersqa.com/my-account/"
    invalid_email = "abc@supersqa.com"
    expected_message = "ERROR: Invalid email address. Lost your password?"
    
#otevreni browseru
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/Users/nikolaborska/Testing/chromedriver")
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def go_to_my_account(self):
        self.driver.get(self.url)
#element pro uz.jmeno
    def input_email(self):
        field = self.driver.find_element(By.ID, "username")
        field.send_keys(self.invalid_email)
        time.sleep(2)
#element pro heslo
    def input_password(self):
        field = self.driver.find_element(By.ID, "password")
        field.send_keys("abcdefge")
        time.sleep(2)
#klikni
    def click_login(self):
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(2)
#overeni error message
    def verify_error_message(self):
        err_elm = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
        displayed_err = err_elm.text
        assert displayed_err == self.expected_message, "The displayed error is not expected."
        print("PASS")
        time.sleep(2)

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.click_login()
        self.verify_error_message()
        self.driver.quit()


if __name__ == "__main__":

    obj = InvalidUserLoginError()
    obj.main()
