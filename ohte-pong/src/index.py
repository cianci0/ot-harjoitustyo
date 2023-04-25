import tkinter as tk
import oneplayer
import twoplayer

def main():
    def start_oneplayer():
        # Remove widgets from the menu window
        header.pack_forget()
        singleplayer_button.pack_forget()
        twoplayer_button.pack_forget()
        standings_button.pack_forget()
        instructions_button.pack_forget()
        footer.pack_forget()

        # Add text boxes for player names
        player1_label = tk.Label(root, text="Pelaajan nimi:", font=("Helvetica", 14), fg="white", bg="#1D3557")
        player1_label.pack(pady=(30,10))
        player1_entry = tk.Entry(root, font=("Helvetica", 14))
        player1_entry.pack(pady=10)

        # Function to start the game
        def start_game():
            # Get player name from text box
            player1_name = player1_entry.get()
            player2_name = "Pong-botti"

            # Close tkinter window, start game
            root.destroy()
            oneplayer.start(player1_name, player2_name, length=10)

            main()

        # Button to start the game
        start_button = tk.Button(root, text="Aloita peli", font=("Helvetica", 14), width=20, height=2, command=start_game, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        start_button.pack(pady=(30,10))

        # Function to reopen the main menu
        def reopen_menu():
            # Add back the widgets that were removed
            header.pack(pady=(20,10))
            singleplayer_button.pack(pady=10)
            twoplayer_button.pack(pady=10)
            standings_button.pack(pady=10)
            instructions_button.pack(pady=10)
            footer.pack(side="bottom", pady=10)

            # Remove widgets
            player1_label.pack_forget()
            player1_entry.pack_forget()
            start_button.pack_forget()
            back_button.pack_forget()

        # Button to reopen the main menu
        back_button = tk.Button(root, text="Takaisin", font=("Helvetica", 14), width=20, height=2, command=reopen_menu, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        back_button.pack(pady=10)

        # Call mainloop to refresh the window
        root.mainloop()

    def start_twoplayer():
        # Remove widgets from the menu window
        header.pack_forget()
        singleplayer_button.pack_forget()
        twoplayer_button.pack_forget()
        standings_button.pack_forget()
        instructions_button.pack_forget()
        footer.pack_forget()

        # Add text boxes for player names
        player1_label = tk.Label(root, text="Pelaajan 1 nimi:", font=("Helvetica", 14), fg="white", bg="#1D3557")
        player1_label.pack(pady=(30,10))
        player1_entry = tk.Entry(root, font=("Helvetica", 14))
        player1_entry.pack(pady=10)

        player2_label = tk.Label(root, text="Pelaajan 2 nimi:", font=("Helvetica", 14), fg="white", bg="#1D3557")
        player2_label.pack(pady=10)
        player2_entry = tk.Entry(root, font=("Helvetica", 14))
        player2_entry.pack(pady=10)

        # Function to start the game
        def start_game():
            # Get player names from text boxes
            player1_name = player1_entry.get()
            player2_name = player2_entry.get()

            # Close tkinter window, start game
            root.destroy()
            twoplayer.start(player1_name, player2_name, length=10)

            main()

        # Button to start the game
        start_button = tk.Button(root, text="Aloita peli", font=("Helvetica", 14), width=20, height=2, command=start_game, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        start_button.pack(pady=(30,10))

        # Function to reopen the main menu window
        def reopen_menu():
            # Add back the widgets that were removed
            header.pack(pady=(20,10))
            singleplayer_button.pack(pady=10)
            twoplayer_button.pack(pady=10)
            standings_button.pack(pady=10)
            instructions_button.pack(pady=10)
            footer.pack(side="bottom", pady=10)

            # Remove the widgets from view1()
            player1_label.pack_forget()
            player1_entry.pack_forget()
            player2_label.pack_forget()
            player2_entry.pack_forget()
            start_button.pack_forget()
            back_button.pack_forget()

        # Button to reopen the main menu
        back_button = tk.Button(root, text="Takaisin", font=("Helvetica", 14), width=20, height=2, command=reopen_menu, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        back_button.pack(pady=10)

        # Call mainloop again to refresh the window
        root.mainloop()

    def open_standings():
        pass

    def open_instructions():
        pass

    # Initiate tkinter, set title
    root = tk.Tk()

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates to center the window
    x = int((screen_width/2) - (400/2))
    y = int((screen_height/2) - (400/2))

    # Set window size and background color
    root.geometry(f"400x400+{x}+{y}")
    root.title("Pong")
    root.configure(bg="#1D3557")


    # Create header
    header = tk.Label(root, text="Pong", font=("Helvetica", 24), fg="white", bg="#1D3557")
    header.pack(pady=(20, 10))

    # Create buttons
    singleplayer_button = tk.Button(root, text="Yksinpeli", font=("Helvetica", 14), width=20, height=2, command=start_oneplayer, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
    singleplayer_button.pack(pady=10)

    twoplayer_button = tk.Button(root, text="Kaksinpeli", font=("Helvetica", 14), width=20, height=2, command=start_twoplayer, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
    twoplayer_button.pack(pady=10)

    standings_button = tk.Button(root, text="Tulostaulu", font=("Helvetica", 14), width=20, height=2, command=open_standings, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
    standings_button.pack(pady=10)

    instructions_button = tk.Button(root, text="Ohjeet", font=("Helvetica", 14), width=20, height=2, command=open_instructions, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
    instructions_button.pack(pady=10)


    # Create footer
    footer = tk.Label(root, text="Ohjelmistotekniikka 2023", font=("Helvetica", 10), fg="white", bg="#1D3557")
    footer.pack(side="bottom", pady=10)


    root.mainloop()

main()
