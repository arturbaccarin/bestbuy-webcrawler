import pytest
import re
import crawler


@pytest.fixture()
def setup():
    driver = crawler.execute_web_driver()
    yield driver
    driver.close()
    

class TestBestBuyCrawler():
    def test_get_home_page_categories_should_return_a_string_list(self, setup):
        driver = setup
        url_homepage = 'https://www.bestbuy.com/'
        cats = crawler.get_home_page_categories(url_homepage, driver)
        assert isinstance(cats, list)
        assert isinstance(cats[0], str)
        assert re.match('http.+bestbuy.com.+', cats[0])

    def test_get_products_urls_in_page_should_return_a_string_list(self, setup):
        driver = setup
        url_prods_page = 'https://www.bestbuy.com/site/promo/smart-home-wi-fi-security-deals'
        prods = crawler.get_products_urls_in_page(url_prods_page, driver)
        assert isinstance(prods, list)
        assert isinstance(prods[0], str)
        assert re.match('http.+bestbuy.com.+', prods[0])

    def test_get_products_urls_in_category_should_return_a_string_list(self, setup):
        driver = setup
        url_cat = 'https://www.bestbuy.com/site/promo/small-appliance-deals'
        prods = crawler.get_products_urls_in_category(url_cat, driver)
        assert isinstance(prods, list)
        assert isinstance(prods[0], str)
        assert re.match('http.+bestbuy.com.+', prods[0])

    def test_get_products_urls_in_categories_should_return_a_string_list(self, setup):
        driver = setup
        cats = [
            'https://www.bestbuy.com/site/promo/smart-home-wi-fi-security-deals',
            'https://www.bestbuy.com/site/promo/printer-and-home-office-deals'
            ]
        prods_cats = crawler.get_products_urls_in_categories(cats, driver)
        assert isinstance(prods_cats, list)
        assert isinstance(prods_cats[0], str)
        assert re.match('http.+bestbuy.com.+', prods_cats[0])

    def test_get_product_info(self, setup):
        driver = setup
        url_prod = 'https://www.bestbuy.com/site/apple-airpods-pro-2nd-generation-white/4900964.p?skuId=4900964'
        prod_info = crawler.get_product_info(url_prod, driver)
        assert isinstance(prod_info, dict)
        assert prod_info['name'] == 'Apple - AirPods Pro (2nd generation) - White'
