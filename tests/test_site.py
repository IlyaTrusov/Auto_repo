import time
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_id('Samsung galaxy s6')

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_product_count(2)


