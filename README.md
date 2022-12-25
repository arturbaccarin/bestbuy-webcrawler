# Best Buy Web Crawler/Scrapping

> Get some informations about products in Best Buy website and save in a database.

### Requirements
* Python 3.9+

### Setup
1. Install requirements: `pip install -r requirements.txt`;
2. Download *geckodriver* in: (https://github.com/mozilla/geckodriver/releases)
3. Extract *geckodriver* in root folder;
4. **If necessary**: change the directory where is your *firefox.exe* in crawer.py, line 18.

### What is used in this project
* Selenium;
* SQLite;
* Pytest.

### Future Improvements
* Create tests for database;
* Add multithreading.