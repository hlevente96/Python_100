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
def reset_timer():
    global reps
    window.after_cancel(timer)
    checkmark.config(text="")
    label.config(fg=GREEN, text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label.config(fg=RED, text="BREAK")
        count_down(long_break)
    elif reps % 2 == 0:
        label.config(fg=PINK, text="BREAK")
        count_down(short_break)
    else:
        label.config(fg=GREEN, text="WORK")
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if 0 < count:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checkmark.config(text="✔"*(reps//2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME,50))
label.config(fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


button_start = Button(text="Start", highlightthickness=0, command = start_timer)
button_start.grid(column=0, row=2)

button_stop = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_stop.grid(column=2, row=2)

checkmark = Label(font=(FONT_NAME,40,"bold"))
checkmark.config(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


window.mainloop()
