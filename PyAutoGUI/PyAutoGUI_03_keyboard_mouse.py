import pyautogui
import pyperclip
import time

# 메인 모니터의 해상도 가져오기
screen_width, screen_height = pyautogui.size()
print(screen_width, screen_height)

# 현재 마우스의 XY 좌표 가져오기
current_mouse_X, current_mouse_Y = pyautogui.position()
print(current_mouse_X, current_mouse_Y)


# 키보드 제어
time.sleep(2)  # 2초간 기다리기
pyautogui.write("Hello World!\n", interval=0.1)
pyautogui.write("We are going to learn PyAutoGUI.\n", interval=0.1)

# 키보드 제어2 - 한글 문자열 통째로 복사 및 Ctrl + V
pyperclip.copy("한글을 입력하겠습니다.")
pyautogui.hotkey("ctrl", "v")


# 마우스 제어
time.sleep(2)  # 2초간 기다리기
position = pyautogui.position()
print(position)  # 현재 마우스 포인터의 위치 출력
pyautogui.click(position)  # 클릭