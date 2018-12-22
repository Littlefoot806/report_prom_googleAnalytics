from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
from time import sleep
from random import randrange
import html
import re


def start_webdriver():
    driver = webdriver.Firefox()
    driver.get("https://my.prom.ua/cabinet/sign-in")
    sleep(3)
    return driver

def loggining(driver, login, passwd):
    login_elem = driver.find_element_by_xpath('//input[@id="phone_email"]')
    pass_elem = driver.find_element_by_xpath('//input[@id="password"]')

    login_elem.clear()
    login_elem.send_keys(login)

    pass_elem.clear()
    pass_elem.send_keys(passwd)

    pass_elem.send_keys(Keys.RETURN)
    sleep(randrange(4, 6))


def change_acc(driver):

    elem_a = driver.find_element_by_xpath('//a[contains(@href, "/cabinet/sign-to/")]')
    href = elem_a.get_attribute("href")
    
    driver.get(href)

    sleep(randrange(4, 6))

def get_data_from_Prom(driver, day):

    company = driver.find_element_by_xpath('//div[@class="b-sidebar-header__id"]').text
    company_id = re.sub(r'\D+', '', company)
    print('Getting data from: {0}'.format(company_id))
    link = driver.find_element_by_xpath('//a[@href="/cms/stats"]')
    link.click()

    yesterday_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@data-key="yesterday"]')))
    yesterday_info.click()
    
    pokazi = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="b-more-link" and contains(text(), "Все товары и услуги")]/../../div[2]'))).text
    perexodi = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="b-more-link" and contains(text(), "Все товары и услуги")]/../..//div[3]'))).text
    zakazi = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="b-more-link" and contains(text(), "Все товары и услуги")]/../..//div[5]'))).text
    zatrati = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="b-more-link" and contains(text(), "Все товары и услуги")]/../..//div[8]'))).text
    sum_of_zakazi = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="b-more-link" and contains(text(), "Все товары и услуги")]/../..//div[9]'))).text

    sum_of_zakazi = html.unescape(sum_of_zakazi).replace(' ', '').replace(',', '.').replace('\xa0', '')


    yesterday = date.today() - timedelta(day)
    yesterday = yesterday.strftime('%Y-%m-%d')

    target = 'https://my.prom.ua/cms/order?filterSetId=temporary_filter_set_id&search_term=&page=1&context=0&date_created__gte={0}&date_created__lte={0}'.format(yesterday)

    driver.get(target)
    sleep(2)
    try:
        order_ids = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@data-qaid="order_id"]')))
        phones = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//p[contains(@class,"client_phone")]')))
        orders = {}
        for order_id, phone in zip(order_ids, phones):
            orders[order_id.get_attribute('textContent')] = phone.get_attribute('textContent')
    except Exception as e:
        orders = {}
        print(e)

    return {
        'company_id' : company_id,
        'orders' : orders,
        'c' : pokazi,
        'e' : perexodi,
        'g' : zakazi,
        'j' : sum_of_zakazi,
        'i' : zatrati
    }

def main(day=1):

    login = "33korovycomua@gmail.com"
    passwd = "4mmj343u7tfgfr4#$$55rf"

    try:
        driver = start_webdriver()
        loggining(driver, login, passwd)
        print('We are inside...')
    except Exception as e:
        print('Problems with loggining or webdriver: {}'.format(e))
        return
    
    data1 = get_data_from_Prom(driver, day)
    change_acc(driver)
    data2 = get_data_from_Prom(driver, day)

    driver.quit()
    print(data1)
    print(data2)
    return [data1, data2]



if __name__ == '__main__':
    main()
