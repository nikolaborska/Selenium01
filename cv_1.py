
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "file:///Users/nikolaborska/Desktop/cv_selenia/cv_1.html"
driver.get(url)

my_btn_one = driver.find_element("id", "btn1")
my_btn_one.click()

driver.close()