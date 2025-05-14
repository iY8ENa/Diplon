import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    # Настройки для обхода защиты
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')

            safe_nodeid = report.nodeid.replace("::", "_").replace("/", "-").replace("\\", "-")
            screenshot_path = f"screenshots/failure_{safe_nodeid}.png"

            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to: {screenshot_path}")