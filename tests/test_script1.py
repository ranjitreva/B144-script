from selenium.webdriver import Chrome

def test_script1():
    print('Hi, Good Afternoon, this is Test Script1 with selenium')
    driver = Chrome()
    driver.get("https://www.google.com/")
    print(driver.title)
    driver.quit()