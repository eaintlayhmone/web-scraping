from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pandas
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import *
username = "minkhant@utycc.edu.mm"


def scrape_link(driver:webdriver.Chrome,keyword):
    print("Keyword is ", keyword)
    driver.set_page_load_timeout(30)
    cookies = driver.get_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    try :
        driver.get('http://polymer-additives.specialchem.com/')
        print("URL successfully Accessed")
    except :
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()
    product_lst = []
    print(driver.title)

    search_bar = find_elem(driver,By.NAME,"keyword")
    sleep(3)
    search_bar.clear()
    search_bar.send_keys(keyword)
    sleep(10)
    driver.execute_script("if (!window.__cfRLUnblockHandlers) return false; fnSearch();")
    print(driver.current_url)
    product_num= find_elem(driver,By.CLASS_NAME,"products-count.inbl")
    if product_num.text.split(' ')[0] != 0:
        products = find_elem(driver,By.XPATH,"//a[@class='tdn']",elems=True)
        for product in products[1:]:
            product_lst.append(product.text)
        product_details = find_elem(driver,By.XPATH,"//a[@class='c7']",elems=True)
        product_links= [element.get_attribute('href') for element in product_details]
        product_map =dict(zip(product_lst, product_links))
        return product_map

    else:
        driver.quit()
        return None
    
    
if __name__ == '__main__':
    scrape_link()