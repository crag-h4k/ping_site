# ['ip_addr':'103.18.133.34', 'port':'21776', 'code':'ID', 'country':'Indonesia', 'anon_level':'elite proxy', 'google':'no', 'https':'no'] `
from time import sleep
from subprocess import check_output
from random import randint, choice

from selenium import webdriver

from bouncer import get_proxy
from easy_utils import log_it


def get_ip():
    current_ip = check_output('hostname -I',shell=True).decode('utf-8')
    return current_ip

url = 'http://10.5.123.94'
i = 0
log_it('______  new __________')
while True:
    rand_sleep = randint(1,15)
    rand_visit = range(randint(1,10))
    #P = get_proxy()
    #proxy = P.ip_addr + ':' + P.port
    chrome_options = webdriver.ChromeOptions()
    #proxy_info = P.ip_addr + ' ' + P.port +  ' ' + P.country +' ' + P.anon_level
    #print(proxy_info)
    #chrome_options.add_argument('--proxy-server=http://%s' % P.ip_addr)
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options = chrome_options)
    i = i + 1
    try:
        driver.get(url)
        log = '\n' + get_ip()  + url +'\t'+ driver.title + '\tsleep_iter = ' + str(rand_sleep) + '\t\tvisit_num: ' + str(i) + '\n'
        log_it(log)
        print(log)
        css = 'a[href*="product"]'
        product_links = driver.find_elements_by_css_selector(css)
        product_url_list = []

        for link in product_links:
            product_url_list.append((link.get_attribute('href')))

        for visit in rand_visit:
            product_url = choice(product_url_list)

            driver.get(product_url)
            log_it(product_url)
            print(product_url)

        product_links.clear()
        product_url_list.clear()
        sleep(rand_sleep)

    except:
        log = '\n' + get_ip() + url + ' ' + driver.title + ' failed to connect ' + ' visit_num: ' + str(i) + '\n'
        log_it(log)
    finally:
        driver.close()
