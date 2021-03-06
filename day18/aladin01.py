
from selenium import webdriver
from bs4 import BeautifulSoup
import time as t

# 파일 입출력 내장함수 open -> 웹데이터의 인코딩을 해석하지 못함
import codecs

# 날짜처리 라이브러리
from datetime import datetime
# 오늘 날짜 시간
d = datetime.today()

# 파일명
file_name = f'알라딘베스트셀러데이터_{d.year}_{d.month}_{d.day}.txt'

# 파일 저장 경로
file_save_path = f'D:/isec_ysyy/py_study/{file_name}'

# 물리드라이버 설정
browser = webdriver.Chrome('D:/isec_ysyy/py_study/c_driver/chromedriver.exe')

# 브라우저 최대창으로 띄우기
browser.maximize_window()

# 타겟 사이트로 이동
browser.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we')

# 현재 페이지 소스코드 불러오기
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

###############핵심 로직(데이터추출)#################

# 베스트 셀러 정보는 div.ss_book_box에 있음
# div_book_box_list = soup.select('div.ss_book_box')
div_book_box_list = soup.find_all('div',class_='ss_book_box')

rank = 1
for boox_box in div_book_box_list:
    div_book = boox_box.select_one('div.ss_book_list')
    # print(div_book)

    li_list = div_book.select('li')

    # 책 제목 추출
    #사은품이 있으면 1번, 없으면 0번
    if len(li_list) == 4:
        title = li_list[0].text
        info = li_list[1].text
        price = li_list[2].text
    else:
        title = li_list[1].text
        info = li_list[2].text
        price = li_list[3].text

    # info 세가지 데이터로 분해
    info_list = info.split('|')
    author, company, pub_date = info_list

    # price 에서 할인 후 가격만 추출
    price = price.split('(')[0]
    price = price[ price.find('→')+1 : ].strip()

    print(title)
    print(author.strip())
    print(company.strip())
    print(pub_date.strip())
    print(price)
    print('='*50)

    # 파일에 저장
    try:
        f = codecs.open(file_save_path, mode = 'a', encoding='utf-8')
        f.write(f'순위: {rank}\n')
        f.write(title + '\n')
        f.write(author.strip() + '\n')
        f.write(company.strip() + '\n')
        f.write(pub_date.strip() + '\n')
        f.write(price + '\n')
        f.write('='*50 + '\n')
    except:
        pass
    finally:
        f.close()
    
    rank += 1