from tkinter import *
from tkinter import messagebox
from keyboard import on_press_key
from random import *
from tkinter import ttk 

window = Tk()
window.title("Color Game")
window.geometry("600x330")
window.iconbitmap("Icon.ico")

score = 0
time_remaining = 60

colors = ["black", "pink", "brown", "green", "yellow", "blue", "purple", "red", "orange"]

def color_game_title():

	shuffle(colors)

	c_label = Label(title_frame, text="C", fg=colors[0], font = ("Arial Bold",15,'underline')).pack(side = LEFT)
	o_label = Label(title_frame, text="O", fg=colors[1], font = ("Arial Bold",15)).pack(side = LEFT)
	l_label = Label(title_frame, text="L", fg=colors[2], font = ("Arial Bold",15,'underline')).pack(side = LEFT)
	o_label = Label(title_frame, text="O", fg=colors[3], font = ("Arial Bold",15)).pack(side = LEFT)
	r_label = Label(title_frame, text="R", fg=colors[4], font = ("Arial Bold",15,'underline')).pack(side = LEFT)
	space_label = Label(title_frame, text=" ").pack(side = LEFT)
	g_label = Label(title_frame, text="G", fg=colors[5], font = ("Arial Bold",15,'underline')).pack(side = LEFT)
	a_label = Label(title_frame, text="A", fg=colors[6], font = ("Arial Bold",15)).pack(side = LEFT)
	m_label = Label(title_frame, text="M", fg=colors[7], font = ("Arial Bold",15,'underline')).pack(side = LEFT)
	e_label = Label(title_frame, text="E", fg=colors[8], font = ("Arial Bold",15)).pack(side = LEFT)
	
def playgame():
	for widget in play_frame.winfo_children():
		if "button" in str(widget):
			widget.destroy()

	try:
		user_entry
	except:
		create_entry_field()

	if time_remaining == 60:
		start_countdown()
	
	start_game()

def create_entry_field():
	global user_entry
	user_entry = Entry(play_frame, relief = GROOVE, bd = 3, highlightthickness=1)
	user_entry.pack(pady = 10)
	user_entry.focus_set()

def start_game():
	global user_entry, score, time_remaining

	if time_remaining > 0:

		user_entry.focus_set()

		if user_entry.get().lower() == colors[0]:
			score += 1 

		user_entry.delete(0,END)

		shuffle(colors)

		guess_color_label.config(fg = colors[0], text = choice(colors).title())

		score_label.config(text = "Your Score : " + str(score))

def start_countdown():
	global time_remaining

	if time_remaining > 0:
		time_remaining -= 1 
		time_label.config(text = "Time : %d"%(time_remaining))
		time_label.after(1000,start_countdown)
	else:
		messagebox.showinfo("Time Over", "Sorry, Time Over.. You Played Well... Your Score : %d"%(score))
		window.destroy()


title_frame = LabelFrame(window, relief = GROOVE)
title_frame.pack(pady = 5)

instructions_frame = LabelFrame(window, text = "Instructions", relief = SUNKEN, font = "Arial 12 bold")
instructions_frame.pack(pady = 15)

score_time_frame = Frame(window)
score_time_frame.pack(fill = X, pady = 15)

play_frame = Frame(window)
play_frame.pack(pady = 15, fill = X)

color_game_title()

score_label = Label(score_time_frame, text = "Your Score : %d"%(score), font = ("Arial Bold",15))
score_label.pack(side=LEFT, padx = 10)

time_label = Label(score_time_frame, text = "Time : %d"%(time_remaining), font = ("Arial Bold",15))
time_label.pack(side=RIGHT, padx = 10)

instructions_1 = Label(instructions_frame, text = "* The Game will start after pressing the 'Play Game' Button or 'Enter' key.", font = ("Arial Bold",10))
instructions_1.pack(anchor = W)

instructions_2 = Label(instructions_frame, text = "* Type the color of the word and not the word ", font = ("Arial Bold",10))
instructions_2.pack(anchor = W)

guess_color_label = Label(play_frame, text = "Click here to Start the game", font = ("Arial Bold",15), relief = RAISED)
guess_color_label.pack(pady = 10)

start_button = ttk.Button(play_frame, text = "Play Game",command = playgame, cursor = "hand2")
start_button.pack(pady = 10)

on_press_key("enter", lambda _ : playgame())

window.mainloop()