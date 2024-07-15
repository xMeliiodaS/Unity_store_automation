Unity Asset Store Testing Framework
Overview
This repository contains a testing framework for automating tests on the Unity Asset Store website. The framework utilizes Selenium for browser automation to test various functionalities such as adding assets to the cart, filtering by price, and editing user bio information.

Installation
To set up the testing framework locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/unity-asset-store-testing.git
cd unity-asset-store-testing
Install dependencies:

Ensure you have Python installed. Then, install the required Python packages using pip:

bash
Copy code
pip install -r requirements.txt
This installs necessary packages including Selenium for browser automation.

WebDriver setup:

You need to download the appropriate WebDriver executable for your browser and operating system:

Chrome: ChromeDriver
Firefox: GeckoDriver
Make sure the WebDriver executable is either in your PATH or specify its location in your test scripts.

Usage
Running tests:

You can run the tests using pytest. For example:

bash
Copy code
pytest test_suite.py
Replace test_suite.py with your actual test suite file.

Writing tests:

Tests are written using Python and pytest framework.
Customize test scripts in accordance with your testing requirements.
Adding new tests:

Create new test scripts in the test directory.
Organize tests into logical suites for better management.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

License
This project is licensed under the MIT License.

