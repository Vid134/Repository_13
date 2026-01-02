# Repository_13
AJAX Dynamic element
📌 Project Overview:
This project automates the World Population Live Counter available on TheWorldCounts website using Python
and Selenium.
It demonstrates real-time data extraction by continuously fetching and displaying the live world population 
count from the webpage.
The project also includes a pytest-based test case to validate that the population counter is displayed correctly.


🛠️ Technologies Used
1.Python 3
2.Selenium WebDriver
3.webdriver-manager
4.Pytest
5.Chrome Browser
6.HTML Reports (pytest-html)


📄 Description of Files
🔹 population_live_loop.py
Opens Chrome browser
Navigates to World Population Live Counter page
Handles cookie popup if present
Extracts live population value
Prints population continuously every second
Stops gracefully when user presses CTRL + C

🔹 test_population_once.py
Pytest automation script
Launches the browser
Fetches the population count once
Asserts that the population value is not empty
Used for validation, not continuous tracking

🔹 conftest.py
Contains shared configuration and reusable logic
Helps keep test code clean and modular
Supports pytest execution

🔹__init__.py
Marks folders as Python packages
Required for imports and pytest discovery 

✅ Key Features
1.Real-time data extraction
2.Cookie popup hand
3.Infinite loop with safe exit
4.CTRL + C interrupt handling
5.Selenium automation best practices
6.Pytest-based validation
7.HTML report generation


🎯 Learning Outcomes
Selenium WebDriver automation
XPath handling for dynamic elements
Exception handling in automation
Infinite loop control
Pytest framework usage
Automation project structuring


📌 Future Enhancements
Add logging instead of print statements
Add explicit waits
Store population history in a file
Integrate CI/CD execution
Add screenshot capture on failure





