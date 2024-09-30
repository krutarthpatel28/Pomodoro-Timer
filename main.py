import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text='00:00')
    head.config(text='Timer')
    ticks.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        head.config(text='Break', fg=RED)
        count_down(long_break_min)

    elif reps % 2 == 0:
        head.config(text='Break', fg=PINK)
        count_down(short_break_min)
    else:
        head.config(text='Work ')
        count_down(work_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += '✔'
        ticks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
time_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=2, column=2)

#     Main title
head = Label(text='Timer', font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
head.grid(row=1, column=2)

# START button
start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(row=3, column=1)

#  RESET button
reset = Button(text='Reset', highlightthickness=0, command=reset)
reset.grid(row=3, column=3)

# TICK label
ticks = Label(fg=GREEN, bg=YELLOW)
ticks.grid(row=4, column=2)

window.mainloop()
