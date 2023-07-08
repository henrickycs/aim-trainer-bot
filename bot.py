def click_auto(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Color of center: (255, 255, 255)
flag = 0
pic = pyautogui.screenshot(region=(282, 136, 800, 600))

width, height = pic.size

for x in range(0, width, 5):
    for y in range(0, height, 5):

        r, g, b = pic.getpixel((x, y))

        if b == 255:
            flag = 1
            # time.sleep(0.5)
            click_auto(x+282, y+136)
            # time.sleep(0.1)
            break

    if flag == 1:
        break
