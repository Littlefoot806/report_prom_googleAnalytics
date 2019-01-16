from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from time import sleep
from datetime import date, timedelta


def start_webdriver():
    driver = webdriver.Firefox()
    driver.get("https://accounts.google.com/ServiceLogin/signinchooser?elo=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    sleep(2)
    return driver

def loggining(driver, login, passwd):
    try:
        login_elem = driver.find_element_by_xpath('//input[@type="email"]')
        login_elem.clear()
        login_elem.send_keys(login)
        login_elem.send_keys(Keys.RETURN)

        sleep(2)

        pass_elem = driver.find_element_by_xpath('//input[@type="password"]')
        pass_elem.clear()
        pass_elem.send_keys(passwd)
        pass_elem.send_keys(Keys.RETURN)
        sleep(2)
        return True
    except Exception as e:
        print(e)
        return False

def get_data(driver, acc_id, day):

    yesterday = date.today() - timedelta(day)
    yesterday = yesterday.strftime('%Y%m%d')

    driver.get("https://analytics.google.com/analytics/web/#/report/visitors-overview/{1}/_u.date00={0}&_u.date01={0}".format(yesterday, acc_id))
    print('Getting data from: {}'.format(acc_id))
    print('Waiting to data...')
    try:
        iframe_elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID , 'galaxyIframe')))
        driver.switch_to.frame(iframe_elem)
        sleep(10)
        sessions = driver.find_element_by_xpath('//div[@id="ID-overview-sparkline"]//div[@data-guidedhelpid="sparkline-metric-analytics.visits-group"]//div[@class="_GAGu"]').text
        print("OK, we taked some data. Let's move on")
    except Exception as e:
        print("Сan't get sessions", e, end='\n')

    driver.get("https://analytics.google.com/analytics/web/#/report/acquisition-channels/{1}/_u.date00={0}&_u.date01={0}".format(yesterday, acc_id))
    print('Waiting to data...')
    try:

        social = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID , 'galaxyIframe')))
        driver.switch_to.frame(iframe_elem)
        sleep(10)

        row = driver.find_element_by_xpath('//table/tbody/tr/td/span[text() = "Social"]/../../td[contains(@class, "visits")]/div').text
        sub_text = driver.find_element_by_xpath('//table/tbody/tr/td/span[text() = "Social"]/../../td[contains(@class, "visits")]/div/span').text

        social = row.replace(sub_text, '')
        print('OK, recorded.')
    except Exception as e:
        social = '0'
        print("Looks like, there not have social data ", end='\n')

    

    return {
        'acc_id' : acc_id,
        'sessions' : sessions,
        'social' : social
    }

def main(day=1):
    login = "..." # google email
    passwd = "..."      # google password
    print('Starting...')

    driver = start_webdriver()

    acc_ids = ['', '', '', '', ''] # Через запятую id аккаунтов ['...', '...', '...']

    if loggining(driver, login, passwd):
        data = []
        for acc_id in acc_ids:
            data.append(get_data(driver, acc_id, day))
            print(data)
        driver.quit()
        return data
    else:
        print('Failed Authorization')
        driver.quit()
        return False


if __name__ == '__main__':
    main()
