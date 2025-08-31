import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# LambdaTest credentials
username = "amitk26hexaware"
access_key = "LT_UFlLBmBg2aRNL2E6LCGaka48SXIFRhjKG8V02N5MO4MMyOo"
grid_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"

# Default capabilities
default_capabilities = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "LT:Options": {
        "platformName": "Windows 10",
        "project": "Selenium 101 Assignment",
        "build": "Scenario 1",
        "name": "Simple Form Demo Test",
        "selenium_version": "4.0.0",
        "w3c": True,
        "network": True,
        "video": True,
        "visual": True,
        "console": True
    }
}

def test_simple_form_demo(capabilities=default_capabilities):
    # Create ChromeOptions and set capabilities
    options = webdriver.ChromeOptions()
    options.set_capability('LT:Options', capabilities['LT:Options'])
    options.set_capability('browserName', capabilities['browserName'])
    options.set_capability('browserVersion', capabilities['browserVersion'])
    
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )
    
    try:
        # Step 1: Open LambdaTest's Selenium Playground
        driver.get("https://www.lambdatest.com/selenium-playground")
        
        # Step 2: Click "Simple Form Demo"
        simple_form_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Simple Form Demo"))
        )
        simple_form_link.click()
        
        # Step 3: Validate that the URL contains "simple-form-demo"
        assert "simple-form-demo" in driver.current_url
        print("URL validation passed!")
        
        # Step 4: Create a variable for the string
        message = "Welcome to LambdaTest"
        
        # Step 5: Enter the value in the text box
        input_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "user-message"))
        )
        input_field.send_keys(message)
        
        # Step 6: Click "Get Checked Value"
        get_value_button = driver.find_element(By.ID, "showInput")
        get_value_button.click()
        
        # Step 7: Validate the displayed message
        displayed_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        assert displayed_message.text == message
        print("Message validation passed!")
        
    except Exception as e:
        print("Test failed with error:", e)
        raise e
    finally:
        driver.quit()

if __name__ == "__main__":
    test_simple_form_demo()