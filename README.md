#ui tests of gmail with selenium webdriver, pytest and allure reports


# gmail_test
test sending and receiving letters


pip install pytest
pip install selenium

#установка и запуск виртуального окружения
virtualenv venv
source venv/bin/activate

#allure on macOS
brew install allure
#создали папку с отчетом
pytest --alluredir reports
#запускаем allure с отчетом в папке reports
allure serve reports

webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME,
    command_executor='http://selenium_hub:4444/wd/hub'

