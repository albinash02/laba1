from bs4 import BeautifulSoup
import openpyxl
from selenium import webdriver
import time


def parse():
    url = 'https://novosibirsk.cian.ru/recommendations/'
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    page = driver.page_source

    soup = BeautifulSoup(page, "html.parser")

    block = soup.select('div._4d935d0799--price--hSzzN')
    descriptions = []
    for data in block:
        if data.find('span'):
            description = data.text
            descriptions.append(description)

    driver.quit()
    return descriptions


if __name__ == '__main__':
    descriptions = parse()
    print(descriptions)



    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'Description'
    for idx, description in enumerate(descriptions, start=2):
        cell = sheet.cell(row=idx, column=1)
        cell.value = description
    wb.save('descriptions.xlsx')