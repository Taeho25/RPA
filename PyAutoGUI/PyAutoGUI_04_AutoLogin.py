# 실습용 웹 사이트: http://dowellcomputer.com/
# 아이디: pyautogui
# 비밀번호: pyautogui

import time
import pyautogui

time.sleep(3) # 3초간 기다리기(실습 환경 준비 시간)

# 로그인 페이지로 이동
page_location = pyautogui.locateOnScreen("Image\login_1.png", confidence=0.5)
pyautogui.moveTo(page_location)
pyautogui.click()

time.sleep(1) # 1초간 기다리기

# 아이디 입력
id_location = pyautogui.locateOnScreen("Image\id.png", confidence=0.6)
pyautogui.moveTo(id_location) # 커서를 아이디 위치로 이동
#pyautogui.moveRel(300, 0) # 오른쪽으로 300px 이동
pyautogui.click() # 입력창 클릭
pyautogui.typewrite("pyautogui") # 아이디 입력

# 비밀번호 입력
password_location = pyautogui.locateOnScreen("Image\password.png", confidence=0.6)
pyautogui.moveTo(password_location) # 커서를 비밀번호 위치로 이동
#pyautogui.moveRel(300, 0) # 오른쪽으로 300px 이동
pyautogui.click() # 입력창 클릭
pyautogui.typewrite("pyautogui") # 비밀번호 입력

# 로그인 진행
login_location = pyautogui.locateOnScreen("login_2.png", confidence=0.6)
pyautogui.moveTo(login_location) # 커서를 로그인 버튼 위치로 이동
pyautogui.click() # 로그인 버튼 클릭
