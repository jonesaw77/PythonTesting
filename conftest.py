import pytest
import os
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="edge", help="browser selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.headless = False
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        #firefox_options.add_argument("--headless")
        firefox_options.add_argument("--ignore-certificate-errors")
        firefox_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=firefox_options)
    elif browser_name == "edge":
        edge_options = webdriver.EdgeOptions()
        # edge_options.add_argument("--headless")
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Edge(options=edge_options)

    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    global driver
    """Embed screenshot in HTML report on failure."""
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ("setup", "call"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get("browserInstance")
            if driver:
                reports_dir = os.path.join(os.path.dirname(__file__), "reports")
                os.makedirs(reports_dir, exist_ok=True)
                file_name = os.path.join(
                    reports_dir,
                    report.nodeid.replace("::", "_").replace("/", "_") + ".png"
                )
                print(f"[Screenshot] Saved: {file_name}")
                _capture_screenshot(driver, file_name)

                html = (
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

    report.extras = extra



def _capture_screenshot(driver, file_name):
    driver.get_screenshot_as_file(file_name)

