
import pytest
from test_simple_form_demo import test_simple_form_demo
from test_drag_drop_sliders import test_drag_drop_sliders
from test_input_form_submit import test_input_form_submit

# Define two sets of capabilities for different browser/OS combinations
capabilities1 = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "LT:Options": {
        "platformName": "Windows 10",
        "project": "Selenium 101 Assignment",
        "build": "Parallel Tests",
        "name": "Test on Windows 10 Chrome",
        "selenium_version": "4.0.0",
        "w3c": True,
        "network": True,
        "video": True,
        "visual": True,
        "console": True
    }
}

capabilities2 = {
    "browserName": "Safari",
    "browserVersion": "latest",
    "LT:Options": {
        "platformName": "macOS Catalina",
        "project": "Selenium 101 Assignment",
        "build": "Parallel Tests",
        "name": "Test on macOS Catalina Safari",
        "selenium_version": "4.0.0",
        "w3c": True,
        "network": True,
        "video": True,
        "visual": True,
        "console": True
    }
}

@pytest.mark.parametrize("capabilities", [capabilities1, capabilities2])
def test_simple_form_demo_parallel(capabilities):
    test_simple_form_demo(capabilities)

@pytest.mark.parametrize("capabilities", [capabilities1, capabilities2])
def test_drag_drop_sliders_parallel(capabilities):
    test_drag_drop_sliders(capabilities)

@pytest.mark.parametrize("capabilities", [capabilities1, capabilities2])
def test_input_form_submit_parallel(capabilities):
    test_input_form_submit(capabilities)