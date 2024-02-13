import pytest
from selenium import webdriver
chrom_option = webdriver.ChromeOptions()
chrom_option.add_argument("--headless")

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#Multiple browser Testing
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif  browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome(options= chrom_option)
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()
