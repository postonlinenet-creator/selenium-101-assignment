# Selenium 101 Assignment Submission

This repository contains my submission for the LambdaTest Selenium 101 assignment.

## Test Scenarios Implemented

1. **Simple Form Demo**: Validates input field functionality
2. **Drag & Drop Sliders**: Tests slider manipulation
3. **Input Form Submit**: Tests form validation and submission

## Setup Instructions for Gitpod

1. Open this repository in Gitpod by prefixing the URL with `gitpod.io/#/`
   Example: `https://gitpod.io/#/https://github.com/postonlinenet-creator/selenium-101-assignment`

2. The environment will automatically set up with all required dependencies from `requirements.txt`

3. Configure your LambdaTest credentials in the test files:
   - Replace `username` and `access_key` variables in each test file with your actual credentials

4. Run tests:
   - Individual tests: `python test_simple_form_demo.py`
   - All tests in parallel: `pytest test_parallel.py -n 2`

## LambdaTest Configuration

- Tests run on LambdaTest's cloud grid
- Parallel execution on Windows 10 Chrome and macOS Catalina Safari
- Network logs, video recordings, screenshots, and console logs are enabled
- Build name: "Selenium 101 Assignment"

## Files Structure

- `test_simple_form_demo.py`: Test Scenario 1 implementation
- `test_drag_drop_sliders.py`: Test Scenario 2 implementation  
- `test_input_form_submit.py`: Test Scenario 3 implementation
- `test_parallel.py`: Parallel test execution setup
- `requirements.txt`: Python dependencies
- `.gitpod.yml`, `.gitpod.Dockerfile`: Gitpod configuration
- `README.md`: This file


## Test IDs

- Windows 10 Chrome: [DA-WIN-2764528-1756426064835658832EDR]
- macOS Catalina Safari: [DA-MAC-2764528-1756426077949618098KXP]