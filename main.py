from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def print_sections(driver):
    elems = driver.find_elements(By.XPATH, "//ul[@class='sp-site-nav-mainlist']/li/div")
    print(f'Количество нужных элементов: {len(elems)}\n')

    print('Элементы:')
    for elem in elems:
        print(f'  {elem.text}')


def goto_section(driver, idx):
    elems = driver.find_elements(By.XPATH, "//ul[@class='sp-site-nav-mainlist']/li/div")
    req_section = elems[idx]
    print(req_section.get_property('data-cid'))
    print(req_section.get_attribute('data-cid'))
    print(req_section.get_dom_attribute('data-cid'))
    req_section.click()


def main():
    driver = webdriver.Chrome('/Users/dipaolo/Downloads/chromedriver')
    driver.get("https://stroyparkdiy.ru/")
    print('')
    print(f'Тайтл страницы: {driver.title}\n')

    # print_sections(driver)
    print('нажимаю')
    goto_section(driver, 5)
    print('нажал')

    sleep(3)


if __name__ == '__main__':
    main()
