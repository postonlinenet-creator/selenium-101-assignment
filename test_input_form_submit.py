import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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
        "build": "Scenario 3",
        "name": "Input Form Submit Test",
        "selenium_version": "4.0.0",
        "w3c": True,
        "network": True,
        "video": True,
        "visual": True,
        "console": True
    }
}

def test_input_form_submit(capabilities=default_capabilities):
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
        
        # Step 2: Click "Input Form Submit"
        form_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Input Form Submit"))
        )
        form_link.click()
        
        # Step 3: Click "Submit" without filling in any information
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))
        )
        submit_button.click()
        
        # Step 4: Assert "Please fill out this field." error message
        name_field = driver.find_element(By.ID, "name")
        validation_message = name_field.get_attribute("validationMessage")
        # Updated assertion to handle browser differences in validation message
        assert "fill out this field" in validation_message.lower(), f"Expected validation message, but got: {validation_message}"
        print("Validation message assertion passed!")
        
        # Step 5: Fill in Name, Email, and other fields
        name_field.send_keys("Amit Kumar")
        driver.find_element(By.ID, "inputEmail4").send_keys("amit@example.com")
        driver.find_element(By.ID, "inputPassword4").send_keys("password123")
        driver.find_element(By.ID, "company").send_keys("Hexaware")
        driver.find_element(By.ID, "websitename").send_keys("https://example.com")
        
        # Step 6: From the Country drop-down, select "United States" using the text property
        country_dropdown = Select(driver.find_element(By.NAME, "country"))
        country_dropdown.select_by_visible_text("United States")
        
        driver.find_element(By.ID, "inputCity").send_keys("New York")
        driver.find_element(By.ID, "inputAddress1").send_keys("123 Main St")
        driver.find_element(By.ID, "inputAddress2").send_keys("Apt 101")
        driver.find_element(By.ID, "inputState").send_keys("NY")
        driver.find_element(By.ID, "inputZip").send_keys("10001")
        
        # Step 7: Fill in all fields and click "Submit"
        submit_button.click()
        
        # Step 8: Validate the success message
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Thanks for contacting us')]"))
        )
        expected_message = "Thanks for contacting us, we will get back to you shortly."
        assert success_message.text == expected_message, f"Expected: {expected_message}, but got: {success_message.text}"
        print("Success message validation passed!")
        
    except Exception as e:
        print("Test failed with error:", e)
        raise e
    finally:
        driver.quit()

if __name__ == "__main__":
    test_input_form_submit()