from link_scrape import *
from page_scrape import *
from utils import *
from selenium import webdriver
import pandas as pd
import time

def scraper_pipeline(keyword):
    print("Start Scraping for ", keyword)
    final_result = []

    # Link Scraping
    urls_to_scrape = scrape_link(driver,keyword)

    if urls_to_scrape == "None":
        print("No items found")
        driver.quit()
    print(keyword , urls_to_scrape)

    # Content Scraping
    for link in urls_to_scrape:
        result_dict = scrape_each_page(driver,urls_to_scrape[link],link)
        final_result.append(result_dict)
        print(link," scraping done")
        print("_________________________________________________-")
    print('Final result ',final_result)

    df = pd.DataFrame(final_result)

    # Write DataFrame to an Excel file
    df.to_excel(f'{keyword}.xlsx', index=False)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    search_keywords = ["Triclosan","Tributyl phosphate","Acrylamide"]
    #login
    login_user(driver)
    for search_keyword in search_keywords:
        start=time.time()
        scraper_pipeline(search_keyword)
        end = time.time()-start
        print("Duration :",end)



"""# Create a ThreadPoolExecutor with max workers
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to scrape each URL concurrently
    futures = [executor.submit(scrape_page, url) for url in urls_to_scrape]

    # Wait for all tasks to complete
    for future in futures:
        future.result()"""
        
