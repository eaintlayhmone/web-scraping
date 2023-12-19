from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pandas
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_elem(instance,attr,val,elems=False,wait=10):
    flag = True
    while flag:
        if elems:
            # elem = instance.find_elements(attr, val)
            elem = WebDriverWait(instance, wait).until(
                EC.presence_of_all_elements_located(
                    (attr,val)
                )
            )
        else:
            # elem = instance.find_element(attr, val)
            elem = WebDriverWait(instance, wait).until(
                EC.presence_of_element_located(
                    (attr,val)
                )
            )
        if not elem == None:
            flag = False
            break
    return elem

def login_user(driver):
    #login_url = "https://polymer-additives.specialchem.com/ajax/login?ajax=4&targetitem={393369BF-5D53-4365-87C2-D75F878856FA}&withcs=1&gaSource=Selector"
    login_url = "https://polymer-additives.specialchem.com/login"
    username = "mumu@doctoral.jp"
    password = "ebp123ebp"
    try :
        driver.get(login_url)
        print("URL successfully Accessed")
    except :
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()
    find_elem(driver, By.ID,"txtUsernamelogin").send_keys(username)
    find_elem(driver, By.ID,"txtPasswordlogin").send_keys(password)
    sleep(10)
    """login_link =  (driver, By.XPATH,"//a[@id='loginbtnclick']")
    print("Login link ",login_link)
    #driver.execute_script("arguments[0].click();", login_link)
    login_link.click()"""
    # Find the login link using its attributes
    login_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,"//a[@id='loginbtnclick']")
                )
            )
    # Click the login link
    login_link.click()
    sleep(3)
    print("After login",driver.current_url)
    print("login successful")