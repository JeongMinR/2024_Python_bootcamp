#정보 : 당첨 번호
import requests
import bs4

URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

target = html.find('div', {'class' : 'nums'})
# print(target)
balls = target.find_all("span", {'class' : 'ball_645'})

for ball in balls:
    print("당첨번호 : ", ball.text)