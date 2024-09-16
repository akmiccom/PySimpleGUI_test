#!/usr/bin/env python
# coding: utf-8

# # PySimpleGUI Clock
# - PySimpleGUI を使って時計ウィジェットを作成
# - フォント選択設定 [フォント選択設定 PySimpleGUI-github](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Font_Previewer.py)

# In[5]:


#!/usr/bin/env python
# coding: utf-8

import PySimpleGUI as sg
from datetime import datetime
from pyautogui import size
import platform # add chatGPT


def date_info(time_format, date_format):
    now = datetime.now()
    time = now.strftime(time_format)
    date = now.strftime(date_format)
    weekday = now.strftime("%a")
    return time, date, weekday

# OSごとの時間・日付フォーマットの設定
if platform.system() == 'Windows':
    time_format = "%H:%M:%S"
    date_format = "%Y/%#m/%#d"
else:
    time_format = "%H:%M:%S"
    date_format = "%Y/%m/%d"

layout = [
    [sg.Text(font=("impact", 50), text_color="gray", key="-time-")],
    [sg.Text(font=("impact", 20), text_color="gray", key="-date-")],
]

window = sg.Window(
    title="clock",
    layout=layout,
    location=(size()[0] - 450, size()[1] - 380),
    transparent_color=sg.theme_background_color(),
    no_titlebar=True,
    right_click_menu=["menu", ["Exit", "!Properties"]],
    keep_on_top=True,
    grab_anywhere_using_control=True,
    alpha_channel=0.5,
)

while True:
    event, values = window.read(timeout=1000, timeout_key="-timeout-")
    if event in [sg.WIN_CLOSED, "Exit"]:
        break
    elif event in "-timeout-":
        time, date, weekday = date_info(time_format, date_format)
        window["-time-"].update(time)
        window["-date-"].update(f"{date} {weekday}")

window.close()

