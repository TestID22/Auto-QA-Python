"# Auto-QA-Python" 
1. 1.TestFrameWork - (https://opensource-demo.orangehrmlive.com/)
2.(https://demoqa.com/)


Workflow
1. Create Project (activate venv) .\venv\scripts\activate
2. Import libraries - pip install pytest selenium webdriver_manager
3. pip freeze>requirenments.txt
4. Create conftest.py
5. import services 
	from selenium import webdriver
	from selenium.webdriver.chrome.service import Service
6. import webdriverWait to BasePage
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions
7. Created config folder with Links Class
8. Created first Base page open, isopened and 
9. Login page object page was inherited from Base page
	LOGIN_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
