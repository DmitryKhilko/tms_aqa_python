import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def test_menu_item():
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver.get('https://spb.minfin.gov.by')
    driver.fullscreen_window()

    time.sleep(1)

    menu_item_locator = driver.find_element(By.XPATH, '//div[contains(text(),"Справочная информация")]')
    menu_item_locator.click()

    header_locator = driver.find_element(By.XPATH, '//h3[contains(text(),"Справочная информация")]')
    assert header_locator.is_displayed()

    driver.close()  # закрываем окно
    driver.quit()  # обязательно делать, иначе память закончится
