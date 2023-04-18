import tkinter as tk

def start_oneplayer():
    pass

def start_twoplayer():
    root.destroy()
    import twoplayer

def open_standings():
    pass

# Initiate tkinter, set title
root = tk.Tk()
root.title("Pong")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates to center the window
x = int((screen_width/2) - (400/2))
y = int((screen_height/2) - (400/2))

# Set window size and background color
root.geometry(f"400x400+{x}+{y}")
root.configure(bg="#1D3557")

# Create header
title_label = tk.Label(root, text="Pong-peli", font=("Helvetica", 24), fg="white", bg="#1D3557")
title_label.pack(pady=20)

# Create buttons
singleplayer_button = tk.Button(root, text="Yksinpeli", font=("Helvetica", 14), width=20, height=2, command=start_oneplayer, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
singleplayer_button.pack(pady=10)

twoplayer_button = tk.Button(root, text="Kaksinpeli", font=("Helvetica", 14), width=20, height=2, command=start_twoplayer, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
twoplayer_button.pack(pady=10)

scoreboard_button = tk.Button(root, text="Avaa tulostaulu", font=("Helvetica", 14), width=20, height=2, command=open_standings, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
scoreboard_button.pack(pady=10)

# Create footer
footer_label = tk.Label(root, text="Ohjelmistotekniikka 2023", font=("Helvetica", 10), fg="white", bg="#1D3557")
footer_label.pack(side="bottom", pady=10)

root.mainloop()