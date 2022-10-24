from tkinter import *
import tkinter.messagebox
from random_word import RandomWords
from word_bank import word_bank
import random

# Constants
MIN = 1
a_timer = None
FONT_NAME = "Arial"
STARTING = 5
SECONDS = 60
r = RandomWords()
words = word_bank
word_check = []


# Timer Mechanism
def countdown(seconds):
    min_rem = int(seconds / 60)
    sec_rem = (seconds % 60)
    if min_rem > 0:
        timer_canvas.itemconfig(timer, text=f"0{min_rem}:0{sec_rem}")
        window.after(1000, countdown, seconds - 1)
    elif sec_rem >= 10:
        timer_canvas.itemconfig(timer, text=f"0{min_rem}:{sec_rem}")
        window.after(1000, countdown, seconds - 1)
    elif 10 > sec_rem > 0:
        timer_canvas.itemconfig(timer, text=f"0{min_rem}:0{sec_rem}")
        window.after(1000, countdown, seconds - 1)
    if sec_rem == 0 and min_rem == 0:
        timer_canvas.itemconfig(timer, text=f"0{min_rem}:0{sec_rem}")
        game_end()


# instruction button
def instructions():
    tkinter.messagebox.showinfo(title='Instructions', message="To begin, click start. There will be a five second "
                                                              "countdown before the bottom entry box appears. "
                                                              "Begin typing, and program will automatically end "
                                                              "after 60 seconds.\n\n"
                                                              "FYI, the prompt is 260 words long, if you type the whole"
                                                              " prompt in less than 60 seconds, "
                                                              "go enter the Guinness World Records")


def show_time(time):
    timer_canvas.itemconfig(timer, text=f"00:0{time}")
    if time > 0:
        window.after(1000, show_time, time - 1)
    if time == 0:
        global words, word_check
        challenge_words = []
        for i in range(260):
            challenge_words.append(random.choice(words).lower())
        word_check = challenge_words
        text = " ".join(challenge_words)
        prompt_text.tag_configure("center", justify='center')
        prompt_text.insert(END, text)
        countdown(SECONDS)


def start_timer():
    global initializing
    show_time(STARTING)
    initializing.config(text="Initializing Word List, Program may freeze momentarily.")
    entry_text.focus_set()


def game_end():
    user_entry = entry_text.get().lower().split(" ")
    total_typed = len(user_entry)
    total_correct = 0
    for k in range(260):
        try:
            if word_check[k] == user_entry[k]:
                total_correct += 1
        except IndexError:
            pass
    tkinter.messagebox.showinfo(title='Instructions', message=f"Your Typed WPM is {total_correct}. Your total would "
                                                              f"have been {total_typed} without the typos found in"
                                                              f"the words you typed.")


def reset():
    prompt_text.delete("1.0", "end")
    entry_text.delete(0, END)
    initializing.destroy()


# UI

window = Tk()
window.title('Typing Speed Test')
window.geometry("705x600")
window.config(padx=70, pady=30)
timer_canvas = Canvas(width=131, height=40)
timer = timer_canvas.create_text(70, 20, text="00:00", font=(FONT_NAME, 22, "bold"))
timer_canvas.grid(column=1, row=0)

# prompt display
prompt_text = Text(width=80, height=20, font=(FONT_NAME, 10, "bold"), wrap=WORD)
prompt_text.grid(column=1, row=2)

# start button
start = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start.grid(column=1, row=3, pady=10, padx=20)

# instructions
instructions = Button(text='Instructions', font=(FONT_NAME, 12, "bold"), command=instructions)
instructions.grid(column=1, row=5, pady=10)

# entry
entry_text = Entry(width=40, font=(FONT_NAME, 12, "bold"))
entry_text.grid(column=1, row=4)

# reset
resets = Button(text='Reset', font=(FONT_NAME, 12, "bold"), command=reset)
resets.grid(column=1, row=7, pady=10)

# initializing
initializing = Label(window, text="")
initializing.grid(column=1, row=8)
window.mainloop()
