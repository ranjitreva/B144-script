import os
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
import allure


@allure.title("Script1-Ranjit")
@allure.description("Attach screenshot to allure report")
def test_script1():
    grid_url = os.getenv('GRID_URL', 'http://localhost:4444')
    print(grid_url)
    
    with allure.step("Step1 : Open Chrome Browser"):
        driver = Remote(grid_url, options=Options())
        
    with allure.step("Step2 : Enter the URL : http://www.google.com"):
        driver.get("http://www.google.com")
        
    with allure.step("Step3 : Take screenshot"):
        allure.attach(driver.get_screenshot_as_png(), name='Google Page', attachment_type=allure.attachment())
        
    with allure.step("Step4 : Close the browser"):
        driver.quit()
        
        
        
    