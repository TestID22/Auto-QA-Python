"# Auto-QA-Python" 
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