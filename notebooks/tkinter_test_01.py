#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import datetime
import time
import threading


# In[11]:


class Timer:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root)
        self.label["font"] = ("Helvetica", 50)
        self.label["bg"] = "black"
        self.label["fg"] = "white"
        self.label.grid(column=0, row=0)

    def changeLabelText(self):
        while True:
            now = datetime.datetime.now()
            self.label["text"] = now.strftime("%Y/%m/%d %H:%M:%S")
            time.sleep(1)


# In[12]:


if __name__ == "__main__":
    timer = Timer()
    thread = threading.Thread(target=timer.changeLabelText)
    thread.start()
    timer.root.mainloop()
