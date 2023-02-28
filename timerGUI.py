from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as font
from playsound import playsound

app = Tk()
frm = ttk.Frame(app, padding=10)
frm.grid()

text_sec = tk.StringVar()
text_sec.set("0")
text_min = tk.StringVar()
text_min.set("30")

buff_min = tk.StringVar()
buff_min.set("30")
buff_sec = tk.StringVar()
buff_sec.set("0")


def timer(i=0):  # 分単位の関数
    for i in range(int(text_min.get())):
        for j in range(0, 60):
            if i < 10:
                buff_min.set("0" + str(i))
            else:
                buff_min.set(str(i))
            if j < 10:
                buff_sec.set("0" + str(j))

            else:
                buff_sec.set(str(j))


def time(i=0):
    global buff_min, buff_sec
    for i in range(11):
        if i == 10:
            print("end")
            buff_min.set("end")
        else:
            print(i)
            buff_sec.set(str(i))
        i += 1
        app.after(1000, time)


text_start_stop = tk.StringVar()
text_start_stop.set("START")

start = True
check = True
stop = False


def start():
    global start, check, text_min, text_sec, start, check, stop, value_time
    start = False
    if check == True and stop == True:
        start = True
        text_start_stop.set("STOP")
        timer()

    elif check == False and stop == True:
        count_min = int(buff_min.get())
        count_sec = int(buff_sec.get())
        buff_min.set("0")
        buff_sec.set("0")
        buff_min.set(count_min)
        buff_sec.set(count_sec)
        check = True
        text_start_stop.set("START")

    else:
        start = True
        stop = True
        text_start_stop.set("STOP")
        buff_min.set(int(text_min.get()))
        buff_sec.set(int(text_sec.get()))
        timer()


def timer():
    global start, buff_min, buff_sec, text_min, text_sec, check, value_time, div_time
    if start == True:
        if int(buff_min.get()) == 0 and int(buff_sec.get()) == 0:

            pass
        else:
            check = False
            time_min = int(buff_min.get())
            time_sec = int(buff_sec.get())
            if time_min >= 0:
                time_sec -= 1
                buff_sec.set(str(time_sec))
                app.after(1000, timer)
                if time_sec == -1:
                    time_min -= 1
                    buff_min.set(str(time_min))
                    buff_sec.set("59")
            if int(buff_min.get()) == 0 and int(buff_sec.get()) == 0:
                start = False
                time_min = 0
                time_sec = 0
                buff_sec.set(str(time_sec))
                buff_min.set(str(time_min))

                playsound("bacs.MP3")


def stop():
    global start, check, stop
    start = True
    check = True
    stop = False
    time_min = 0
    time_sec = 0
    buff_sec.set(str(time_sec))
    buff_min.set(str(time_min))


label = tk.Label(frm, text="ENTER : ").grid(column=0, row=0)
entry1 = tk.Entry(frm, textvariable=text_min).grid(column=1, row=0)
label_min = tk.Label(frm, text="m").grid(column=2, row=0)
entry2 = tk.Entry(frm, textvariable=text_sec).grid(column=3, row=0)
label_sec = tk.Label(frm, text="s").grid(column=4, row=0)

label = tk.Label(frm, textvariable=buff_min, font=font.Font(size=20)).grid(column=0, row=1, columnspan=2, rowspan=4)
label = tk.Label(frm, text=":").grid(column=2, row=2)
label = tk.Label(frm, textvariable=buff_sec, font=font.Font(size=20)).grid(column=3, row=1, columnspan=2, rowspan=5)
button = tk.Button(frm, textvariable=text_start_stop, command=start)
button.grid(column=6, row=1)
button = tk.Button(frm, text="reset", command=stop).grid(column=6, row=3)

app.mainloop()
