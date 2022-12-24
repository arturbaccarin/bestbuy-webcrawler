import db
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from typing import Optional


def execute_web_driver() -> WebDriver:
    """Create, configure and return a WebDriver

    Returns:
        webdriver: Firefox Webdriver
    """
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    return webdriver.Firefox(options=options)


def select_country_when_enter_the_site(driver: WebDriver) -> None:
    """Choose United States automatically in 'Choose a country.'

    Args:
        driver (WebDriver): Firefox Webdriver
    """
    try:
        headings = driver.find_element(By.CLASS_NAME, 'heading')
        if headings.text == 'Hello!':
            driver.find_element(By.CLASS_NAME, 'us-link').click()
    except NoSuchElementException:
        pass


def get_home_page_categories(url_homepage: str, driver: WebDriver) -> list[str]:
    """Get the urls' categories of the products.

    Args:
        url_homepage (str): the homepage link from site
        driver (WebDriver): Firefox Webdriver

    Returns:
        list[str]: list of the categories links
    """
    categories_urls = []

    driver.get(url_homepage)
    select_country_when_enter_the_site(driver)
    
    categories_elements = driver.find_elements(By.CLASS_NAME, 'se-item-text')
    for category_element in categories_elements:
        categories_urls.append(
            category_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        )
    return categories_urls


def get_products_urls_in_categories(categories_urls: list[str], driver: WebDriver) -> list[str]:
    """Get the product's urls of the all categories.

    Args:
        categories_urls (list[str]): categories of the site
        driver (WebDriver): Firefox Webdriver

    Returns:
        list[str]: list of the products links
    """
    products_urls = []
    for category_url in categories_urls:
        products_urls.extend(get_products_urls_in_category(category_url, driver))
    return products_urls


def get_products_urls_in_category(category_url: str, driver: WebDriver) -> list[str]:
    """Get the product's urls from a unique category

    Args:
        category_url (str): category link
        driver (WebDriver): Firefox Webdriver

    Returns:
        list[str]: all products links of the category
    """
    category_products_url = []
    page_number = 1
    while True:
        products_urls = get_products_urls_in_page(category_url+f'?cp={page_number}', driver)
        if products_urls:
            category_products_url.extend(products_urls)
            page_number += 1
            continue
        break
    return category_products_url


def get_products_urls_in_page(url: str, driver: WebDriver) -> Optional[list[str]]:
    """Get the product's urls from a unique page

    Args:
        url (str): products page link
        driver (WebDriver): Firefox Webdriver

    Returns:
        Optional[list[str]]: return a products links url or None
    """
    products_urls = []
    driver.get(url)
    select_country_when_enter_the_site(driver)
    web_elements = driver.find_elements(By.CLASS_NAME, 'sku-title')
    if not web_elements:
        return
    for web_element in web_elements:
        try:
            url_product = web_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except NoSuchElementException:
            continue
        if url_product not in products_urls:
            products_urls.append(url_product)
    return products_urls


def save_products_info(urls_product: list[str], driver: WebDriver) -> None:
    """Save the products data in db

    Args:
        urls_product (list[str]): products links list
        driver (WebDriver): Firefox Webdriver
    """
    all_products_saved = db.select_values()
    urls_saved = [item[1] for item in all_products_saved]
    for url_product in urls_product:
        if url_product in urls_saved:
            continue
        product_info = get_product_info(url_product, driver)
        db.insert_values(product_info)


def get_product_info(url_product: str, driver: WebDriver) -> dict[str, str]:
    """Get the product's data from a product link

    Args:
        url_product (str): the product link
        driver (WebDriver): Firefox Webdriver

    Returns:
        dict[str, str]: the product data
    """
    driver.get(url_product)
    select_country_when_enter_the_site(driver)
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 1100)")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'c-accordion-trigger-label').click()

    try:
        name = driver.find_element(By.CLASS_NAME, 'sku-title').find_element(By.TAG_NAME, 'h1').text
        name = name.strip()
    except NoSuchElementException:
        name = ''

    try:
        sku = driver.find_element("xpath", "//div[@class='sku product-data']").text
    except NoSuchElementException:
        sku = ''

    try:
        description = driver.find_element(
            "xpath", "//div[@class='long-description-container body-copy ']"
            ).find_element(By.TAG_NAME, 'div').text
        description = ' '.join(description.split())
        description = description.strip()
    except NoSuchElementException:
        description = ''

    img_list = []
    img_elements = driver.find_elements("xpath", "//li[@class='image-thumbnail']")
    for img_element in img_elements:
        url_img = img_element.find_element(By.TAG_NAME, 'img').get_attribute('src')
        url_img = url_img.split(';')[0]
        if url_img not in img_list:
            img_list.append(url_img)
    images = ';'.join(img_list)

    return {
        'url': url_product,
        'sku': sku,
        'name': name,
        'description': description,
        'images': images
    }
