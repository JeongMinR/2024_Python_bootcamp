from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# WebDriver 설정
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Papago 웹사이트 열기
driver.get("https://papago.naver.com/")
time.sleep(3)

# 기존 번역 결과 읽어오기
existing_translations = set()
try:
    with open('my_papago.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 행 건너뛰기
        for row in reader:
            existing_translations.add(row[0])
except FileNotFoundError:
    pass  # 파일이 없으면 나중에 생성됨

# 새로운 번역 결과 추가를 위해 CSV 파일 열기
with open('my_papago.csv', 'a', newline='') as f:
    wtr = csv.writer(f)
    
    # 파일이 비어있는 경우 헤더 행 작성
    if not existing_translations:
        wtr.writerow(['영단어', '번역결과'])
    
    # 번역 반복문
    while True:
        keyword = input('번역할 영단어 입력 (0 입력하면 종료) : ')
        if keyword == '0':
            print('번역 종료')
            break
        
        if keyword in existing_translations:
            print(f"{keyword}은(는) 이미 my_papago.csv에 번역되어 저장되어 있습니다.")
            continue
        
        # 텍스트 영역 찾고 비우기
        form = driver.find_element(By.CSS_SELECTOR, "textarea#txtSource")
        form.clear()
        
        # 키워드 입력
        form.send_keys(keyword)
        
        # 번역 버튼 클릭
        button = driver.find_element(By.CSS_SELECTOR, "button#btnTranslate")
        button.click()
        
        # 번역이 완료될 때까지 대기
        time.sleep(5)
        
        # 번역 결과 가져오기
        result = driver.find_element(By.CSS_SELECTOR, "div#txtTarget").text
        print(keyword, "->", result)
        
        # 번역 결과를 CSV 파일에 저장
        wtr.writerow([keyword, result])
        existing_translations.add(keyword)

# 브라우저 닫기
driver.quit()
