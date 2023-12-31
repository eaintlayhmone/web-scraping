from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import find_elem
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



def scrape_each_page(driver:webdriver.Chrome,url,product_name):
    driver.set_page_load_timeout(30)
    try :
        driver.get(url)
        print("URL successfully Accessed")
    except :
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    # Perform scraping actions on the page
    # ...
    sleep(5)
    # Find elements containing the desired information
    try:
        product_type_element = find_elem(driver,By.XPATH,"//div[contains(., 'Product Type')]/following-sibling::div")
        product_type = product_type_element.text.strip()
    except:
        product_type = '-'
    try:
        chemical_composition_element = find_elem(driver,By.XPATH,"//div[contains(., 'Chemical Composition')]/following-sibling::div")
        chemical_composition = chemical_composition_element.text.strip()
    except:
        chemical_composition = '-'
    try:
        application_element = find_elem(driver,By.XPATH,"//div[contains(., 'Applications/ Recommended for')]/following-sibling::div")
        application = application_element.text.strip()
    except:
        application = "-"

   

    # Output the extracted information
    print(f"[{product_type}, {chemical_composition}, {application}]")

    #access_link = find_elem(driver,By.CLASS_NAME,"bt_cta_1")

    # Click on the link to access the full datasheet
    #access_link.click()

    # Wait for the content to load (assuming the content loads dynamically)
    # You might need to adjust the timeout and locator strategy based on your website's behavior
    WebDriverWait(driver, 10)
    
    #product_attr = find_elem(driver,By.XPATH,"//div[contains(@class, 'col') and contains(@class, 'w60') and contains(@class, 'small-w100')]/strong",elems=True)
    print(driver.current_url)
    # Close the WebDriver instance
    return {"Product_name":product_name,"Product type":product_type,"Chemical_composition":chemical_composition,"Application (Recommended for)":application}

    






