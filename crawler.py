from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

# handler
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r"C:/Users/윤국희/Desktop/vscode/python/crawler/webdriver/chromedriver.exe")
# 왜 상대 경로로 했을 때는 안 됐을까? --> 절대 경로로 바꿔서 오류 해결됨.

# 크롬 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈 설정
browser.set_window_size(1928, 1280)

# 페이지 이동
browser.get("http://prod.danawa.com/list/?cate=12210596&15main_12_02")

# webdriverwait 사용, 체크박스 클릭
WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#searchMakerRep1452'))).click()
time.sleep(2)



#---------------------------------------------------------------------------

#bs4 객체 생성
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 상품 리스트 가져오기
prod_list = soup.select("div.main_prodlist.main_prodlist_list > ul > li")
print(prod_list)

for product in prod_list:
    prod_name = product.select_one("p.prod_name > a").text.strip()
    prod_price = product.select_one("p.price_sect > a > strong").text.strip()
    print(prod_name)
    print(prod_price)
