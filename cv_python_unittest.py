import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time 


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        time.sleep(2)   

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")
        time.sleep(2)
        self.assertIn("Python", driver.title)
        time.sleep(2)
        elem = driver.find_element_by_name("q")
        time.sleep(2)
        elem.send_keys("getting started with python")
        elem.send_keys(Keys.RETURN)
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()