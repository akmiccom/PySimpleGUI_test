#!/usr/bin/env python
# coding: utf-8

# # PySimpleGUI Watch
# - PySimpleGUI を使って時計ウィジェットを作成
# - 

# In[6]:


import PySimpleGUI as sg
from datetime import datetime
from pyautogui import size


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
]

window = sg.Window(
    title="clock",
    layout=layout,
    size=(400, 200),
    location=(size()[0] - 395, size()[1] - 275),
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

