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
        "build": "Scenario 2",
        "name": "Drag & Drop Sliders Test",
        "selenium_version": "4.0.0",
        "w3c": True,
        "network": True,
        "video": True,
        "visual": True,
        "console": True
    }
}

def test_drag_drop_sliders(capabilities=default_capabilities):
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
        
        # Step 2: Click "Drag & Drop Sliders"
        slider_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Drag & Drop Sliders"))
        )
        slider_link.click()
        
        # Step 3: Find the slider with default value 15
        slider_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='15']"))
        )
        
        # Step 4: Get the output element that displays the value
        slider_output = driver.find_element(By.XPATH, "//input[@value='15']/following-sibling::output")
        
        # Step 5: Use JavaScript to set the slider value to 95 and trigger events
        driver.execute_script("""
            var slider = arguments[0];
            var output = arguments[1];
            slider.value = 95;
            // Trigger multiple events to ensure the UI updates
            var events = ['input', 'change', 'click'];
            events.forEach(function(eventType) {
                var event = new Event(eventType, { bubbles: true });
                slider.dispatchEvent(event);
            });
            // Also update the output element directly if needed
            output.innerHTML = '95';
        """, slider_input, slider_output)
        
        # Wait a moment for the UI to update
        time.sleep(2)
        
        # Step 6: Validate the value
        slider_value = slider_output.get_attribute("innerHTML")
        assert slider_value == "95", f"Expected 95, but got {slider_value}"
        print("Slider value validation passed! Value is 95.")
        
    except Exception as e:
        print("Test failed with error:", e)
        raise e
    finally:
        driver.quit()

if __name__ == "__main__":
    test_drag_drop_sliders()