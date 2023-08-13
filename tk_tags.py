import tkinter as tk
from tkinter import ttk

YELLOW = "#E57C23"
LIGHT_YELLOW = "#E8AA42"
GREEN = "#025464"
WHITE = "#F8F1F1"

root = tk.Tk()

def show_key(event):
    key = f"Keysym {event.keysym}   Keycode {event.keycode}"
    keypress_label.config(text=f"{key}")

def button1_clicked(event):
    button_clicked_at = f"<Button-1>: X: {event.x} Y: {event.y}"
    mouse_label.config(text=f"{button_clicked_at}")
    #print(button_clicked_at)

def button2_clicked(event):
    button_clicked_at = f"<Button-2>: X: {event.x} Y: {event.y}"
    mouse_label.config(text=f"{button_clicked_at}")
    #print(button_clicked_at)

def button_clicked(event):
    button_clicked_at = f"<Button>: X: {event.x} Y: {event.y}"
    mouse_label.config(text=f"{button_clicked_at}")
    #print(button_clicked_at)

def widget_event(event):
    enter_event.config(text=f"{event}")
    #print(event)


root.geometry("1000x500")
root.title("Tkintet Events Helper")
#root.config(bg="#025464", padx=10, pady=10)
root.resizable(False, False)

top_frame = ttk.Frame(root)
top_frame.pack(side="top", fill="both")
mid_frame = ttk.Frame(root)
mid_frame.pack(side="top", fill="both", expand=True)
bottom_frame = ttk.Frame(root)
bottom_frame.pack(side="top", fill="both", expand=True)

title_label = ttk.Label(top_frame, text="Tkinter Event Tags", font=("Tahoma", 30), background=WHITE, foreground=YELLOW, padding=(300, 10, 50, 10))
title_label.pack(side="top", fill="x", expand=True)

keypress_label = ttk.Label(mid_frame, text="Press any key", font=("Tahoma", 20), background=YELLOW, foreground=WHITE, padding=(80, 10, 80, 10))
keypress_label.pack(side="left", fill="both", expand=True)

mouse_label = ttk.Label(mid_frame, text="Or Click mouse buttons", font=("Tahoma", 20), background=LIGHT_YELLOW, foreground=WHITE, padding=(80, 10, 80, 10))
mouse_label.pack(side="left", fill="both", expand=True)

enter_event = ttk.Label(bottom_frame, text="Events", font=("Tahoma", 20), background=GREEN, foreground=WHITE, padding=(200, 10, 80, 10))
enter_event.pack(side="top", fill="both", expand=True)


root.bind("<Button-1>", button1_clicked, add="+")
root.bind("<Button-2>", button2_clicked, add="+")
root.bind("<Button>", button_clicked, add="+")
root.bind("<Enter>", widget_event, add="+")
root.bind("<Leave>", widget_event, add="+")
root.bind("<KeyPress>", show_key, add="+")
root.mainloop()