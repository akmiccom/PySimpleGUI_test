#!/usr/bin/env python
# coding: utf-8

# # PySimpleGUI Clock
# - PySimpleGUI を使って時計ウィジェットを作成
# - フォント選択設定 [フォント選択設定 PySimpleGUI-github](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Font_Previewer.py)

# In[1]:


import PySimpleGUI as sg
from datetime import datetime
from pyautogui import size


# fonts = sg.Text.fonts_installed_list()

layout = [
    [
        sg.Text(
            font=("impact", 50),
            text_color="gray",
            key="-time-",
            auto_size_text=False,
        ),
    ],
    [
        sg.Text(
            font=("impact", 20),
            text_color="gray",
            key="-date-",
        ),
    ],
    # [
    #     sg.Listbox(
    #         # fonts,
    #         size=(30, 20),
    #         change_submits=True, key='-list-')
    # ],
]

window = sg.Window(
    title="clock",
    layout=layout,
    # size=(400, 200),
    location=(size()[0] - 350, size()[1] - 380),
    transparent_color=sg.theme_background_color(),
    no_titlebar=True,
    right_click_menu=["menu", ["Exit", "!Properties"]],
    keep_on_top=True,
    grab_anywhere_using_control=True,
    alpha_channel=0.5,
    # auto_close=True,
    # auto_close_duration=5,
)

while True:
    event, values = window.read(timeout=100, timeout_key="-timeout-")
    if event in [sg.WIN_CLOSED, "Exit"]:
        break
    elif event in "-timeout-":
        now = datetime.now()
        time = now.strftime("%#H:%M:%S")
        date = now.strftime("%#Y/%#m/%#d")
        weekday = now.strftime("%a")
        window["-time-"].update(time)
        window["-date-"].update(f"{date} {weekday}")

window.close()

