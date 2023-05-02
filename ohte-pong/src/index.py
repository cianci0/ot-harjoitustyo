import tkinter as tk
import oneplayer
import twoplayer
from style import ui_text_font, ui_header_font, inst_text

def main():

    def forget_mainmenu():
        header.pack_forget()
        singleplayer_button.pack_forget()
        twoplayer_button.pack_forget()
        standings_button.pack_forget()
        instructions_button.pack_forget()
    
    def reopen_mainmenu():
        header.pack(pady=(20,10))
        singleplayer_button.pack(pady=10)
        twoplayer_button.pack(pady=10)
        standings_button.pack(pady=10)
        instructions_button.pack(pady=10)

    def start_oneplayer():
        forget_mainmenu()

        player1_label = tk.Label(root, text="Pelaajan nimi:", font=ui_text_font, fg="white", bg="#1D3557")
        player1_label.pack(pady=(30,10))
        player1_entry = tk.Entry(root, font=ui_text_font)
        player1_entry.pack(pady=10)

        def start_game():
            player1_name = player1_entry.get()
            player2_name = "Pong-botti"
            root.destroy()
            oneplayer.start(player1_name, player2_name, length=10)
            main()

        start_button = tk.Button(root, text="Aloita peli", font=ui_text_font, width=20, height=2, command=start_game, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        start_button.pack(pady=(30,10))

        def reopen_menu():
            reopen_mainmenu()
            player1_label.pack_forget()
            player1_entry.pack_forget()
            start_button.pack_forget()
            back_button.pack_forget()

        back_button = tk.Button(root, text="Takaisin", font=ui_text_font, width=20, height=2, command=reopen_menu, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        back_button.pack(pady=10)

        root.mainloop()

    def start_twoplayer():
        forget_mainmenu()

        player1_label = tk.Label(root, text="Pelaajan 1 nimi:", font=ui_text_font, fg="white", bg="#1D3557")
        player1_label.pack(pady=(30,10))
        player1_entry = tk.Entry(root, font=ui_text_font)
        player1_entry.pack(pady=10)

        player2_label = tk.Label(root, text="Pelaajan 2 nimi:", font=ui_text_font, fg="white", bg="#1D3557")
        player2_label.pack(pady=10)
        player2_entry = tk.Entry(root, font=ui_text_font)
        player2_entry.pack(pady=10)

        def start_game():
            player1_name = player1_entry.get()
            player2_name = player2_entry.get()
            root.destroy()
            twoplayer.start(player1_name, player2_name, length=10)
            main()

        start_button = tk.Button(root, text="Aloita peli", font=ui_text_font, width=20, height=2, command=start_game, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        start_button.pack(pady=(30,10))

        def reopen_menu():
            reopen_mainmenu()
            player1_label.pack_forget()
            player1_entry.pack_forget()
            player2_label.pack_forget()
            player2_entry.pack_forget()
            start_button.pack_forget()
            back_button.pack_forget()

        back_button = tk.Button(root, text="Takaisin", font=ui_text_font, width=20, height=2, command=reopen_menu, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        back_button.pack(pady=10)

        root.mainloop()

    def open_standings():
        pass

    def open_instructions():
        forget_mainmenu()
 
        instructions_header = tk.Label(root, text="Ohjeet", font=ui_header_font, fg="white", bg="#1D3557")
        instructions_header.pack(pady=(20, 10))

        instructions_text = tk.Text(root, bg="#1D3557", fg="white", relief=tk.FLAT, highlightthickness=0, selectborderwidth=0, selectbackground="#1D3557", selectforeground="white")
        instructions_text.insert("end", inst_text)
        instructions_text.config(state="disabled")
                                    
        instructions_text.pack(pady=(5))

        instructions_footer = tk.Label(root, text="Ohjelmistotekniikka 2023", font=("Helvetica", 10), fg="white", bg="#1D3557")
        instructions_footer.pack(side="bottom", pady=10)

        def reopen_menu():
            reopen_mainmenu()

            instructions_header.pack_forget()
            instructions_text.pack_forget()
            instructions_footer.pack_forget()
            back_button.destroy()

        back_button = tk.Button(root, text="Takaisin", font=ui_text_font, width=20, height=2, command=reopen_menu, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        back_button.place(x=85, y=300)

    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates to center the window (from ChatGPT)
    x = int((screen_width/2) - (400/2))
    y = int((screen_height/2) - (400/2))

    root.geometry(f"400x400+{x}+{y}")
    root.title("Pong")
    root.configure(bg="#1D3557")


    header = tk.Label(root, text="Pong", font=ui_header_font, fg="white", bg="#1D3557")
    header.pack(pady=(20, 10))

    singleplayer_button = tk.Button(root, text="Yksinpeli", font=ui_text_font, width=20, height=2, command=start_oneplayer, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
    singleplayer_button.pack(pady=10)

    twoplayer_button = tk.Button(root, text="Kaksinpeli", font=ui_text_font, width=20, height=2, command=start_twoplayer, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
    twoplayer_button.pack(pady=10)

    standings_button = tk.Button(root, text="Tulostaulu", font=ui_text_font, width=20, height=2, command=open_standings, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
    standings_button.pack(pady=10)

    instructions_button = tk.Button(root, text="Ohjeet", font=ui_text_font, width=20, height=2, command=open_instructions, bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
    instructions_button.pack(pady=10)

    footer = tk.Label(root, text="Ohjelmistotekniikka 2023", font=("Helvetica", 10), fg="white", bg="#1D3557")
    footer.pack(side="bottom", pady=10)

    root.mainloop()

main()
