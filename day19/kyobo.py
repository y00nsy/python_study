from selenium import webdriver
from bs4 import BeautifulSoup
import time as t

# 날짜처리 라이브러리
from datetime import datetime

# 엑셀저장 라이브러리 
import xlsxwriter

# 이미지 다운로드 처리 라이브러리
import urllib.request as req
from io import BytesIO

# 오늘 날짜 시간 
d = datetime.today()

# 파일명
file_name = f'교보문고베스트순위_{d.year}_{d.month}_{d.day}.xlsx'

# 파일 저장 경로
file_save_path = f'D:/isec_ysyy/py_study/{file_name}'

# 엑셀라이브러리 객체 생성
workbook = xlsxwriter.Workbook(file_save_path)

# 엑셀 워크 시트 만들기
worksheet = workbook.add_worksheet()

# 엑셀 열이름 (첫줄 정보 생성)

# 행 꾸미기
styles = {
    'bold': True,
    'font_color': 'red',
    'bg_color': 'yellow'
}
cell_format = workbook.add_format(styles)

worksheet.write('A1', '순위', cell_format)
worksheet.write('B1', '썸네일', cell_format)
worksheet.write('C1', '저자', cell_format)
worksheet.write('D1', '출판사', cell_format)
worksheet.write('E1', '출판일', cell_format)
# worksheet.write('F1', '좋아요수', cell_format)


# 물리드라이버
browser = webdriver.Chrome('D:/isec_ysyy/py_study/c_driver/chromedriver.exe')

# 브라우저 최대창으로 띄우기
# browser.maximize_window()

# 브라우저 원하는 사이즈로 키우기
browser.set_window_size(1280, 1080)

# 타겟 사이트로 이동
browser.get('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf')



######### 핵심 로직 ###########


#순위 탭 클릭
# 1위~20위 : main_contents > div:nth-child(6) > div.list_paging > ul > li:nth-child((1) > strong > a
# 21위~30위 : main_contents > div:nth-child(6) > div.list_paging > ul > li:nth-child(2) > a
for n in range(1, 2):
    if n > 1:
        browser.find_element_by_css_selector(f'#main_contents > div:nth-child(6) > div.list_paging > ul > li:nth-child({n}) > a').click()
    t.sleep(1)

    # 현재 페이지 소스코드 불러오기
    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')

    best_list = soup.select('ul.list_type01 > li') # 한페이지에 들어있는 베스트샐러 리스트들
    
    # print(len(best_list))
    for book_info in best_list:
        
        rank = int(book_info.select_one('.cover> a > strong.rank').text.strip())
        title = book_info.select_one('.title > a> strong').text.strip()
        
        info_tag = book_info.select_one('.author')
        info = info_tag.text.strip()

        info_list = info.split('|')
        author, company, pub_date = info_list

        temp = info_tag.select_one('span.popup_load > a')
        # print(temp)
        if temp:
            sep = temp.text.strip() # 저자 더보기
            info2 = author.split(sep)
            # print(info2)

            author = info2[0] # if문 걸리는 부분만 info2의 0번 인덱스
        
        img_tag = book_info.select_one('.cover > a > img')
        img_src = img_tag['src']

        print(rank)
        print(title)
        print(author.strip())
        print(company.strip())
        print(pub_date.strip())
        print('=' *40)
        
        #엑셀에 이미지 저장
        # worksheet.write('B1','썸네일')
        # 이미지경로를 통해 이미지 다운
        img_data = BytesIO(req.urlopen(img_src).read())
        worksheet.insert_image(f'B{rank+1}', img_src, {'image_data':img_data})

        # 엑셀에 데이터 저장
        worksheet.write(f'A{rank+1}',rank)
        worksheet.write(f'C{rank+1}',author)
        worksheet.write(f'D{rank+1}',company)
        worksheet.write(f'E{rank+1}',pub_date)
        #worksheet.write(f'F{rank+1}',like)
        
browser.close()
workbook.close()
    


