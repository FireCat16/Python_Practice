import pyautogui

screenWidth, screenHeight = pyautogui.size()

#cookieButton = pyautogui.locateOnScreen('cookieButton.png')
#print (cookieButton)

i=1
while i < 100:
    pyautogui.click(100,370)
    i+=1
