from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import csv

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# 우리가 컨트롤 할 수 있는 브라우저가 실행이된다.

driver.get("https://papago.naver.com/")
time.sleep(3)

# 작성할 'my_papago.csv' 파일을 생성하여 변수 'f'에 저장
f = open('./my_papago.csv', 'w', newline = '')

# CSV 파일을 작성하는 객체 변수 'wtr' 생성
wtr = csv.writer(f)

# 열 제목 작성
wtr.writerow(['영단어', '번역결과'])

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# 우리가 컨트롤 할 수 있는 브라우저가 실행이된다.

driver.get("https://papago.naver.com/")
time.sleep(3)

question = input("번역 할 영단어를 입력하세요. : ")
form = driver.find_element(By.CSS_SELECTOR,"textarea#txtSource")
form.send_keys(question)

button = driver.find_element(By.CSS_SELECTOR,"button#btnTranslate")
button.click()

time.sleep(5)
result = driver.find_element(By.CSS_SELECTOR,"div#txtTarget")
print(question, "->", result.text)

#반목문 작성
while True:
    keyword = input('번역할 영단어 입력 (0 입력하면 종료) : ')
    if keyword == '0':
        print('번역 종료')
        break
    # 영단어 입력, 번역 버튼 클릭
    form = driver.find_element(By.CSS_SELECTOR,'textarea#txtSource')
    form.send
    button = driver.find_element(By.CSS_SELECTOR, 'button#btnTranslate')
    button.click()
    time.sleep(1)

	# 번역 결과 저장
    output = driver.find_element(By.CSS_SELECTOR, 'div#txtTarget').text
    
	# my_papago.csv 파일에 [영단어, 번역결과] 작성
    wtr.writerow([keyword, output])

    if keyword in driver.find_element:
            print(f"{keyword}은(는) 이미 my_papago.csv에 번역되어 저장되어 있습니다.")
            continue
    
	# 영단어 입력 칸 초기화
    driver.find_element(By.CSS_SELECTOR,'textarea#txtSource').clear()


driver.close()