from tkinter import *

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Language Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526,width=800)
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_image)
canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic"), fill="black")
canvas.create_text(400,263, text="word", font=("Ariel",60,"bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, borderwidth=0)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0)
wrong_button.grid(row=1, column=1)

window.mainloop()