import tkinter as tk
from oneplayer import OnePlayer
from twoplayer import TwoPlayer
from style import TEXT_FONT, HEADER_FONT, INST_TEXT, WINDOW
from ui.leaderboard import leaderboard_text

class Ui:
    """ Ui class for tkinter interface

    Attributes:
    root: tkinter.Tk object
    header: tkinter.Label object for header text
    singleplayer_button: tkinter.Button object for button to open single player game configuration window
    twoplayer_button: tkinter.Button object for button to open multiplayer game configuration window
    standings_button: tkinter.Button object for button to open standings
    instructions_button: tkinter.Button object for button to open instructions
    footer: tkinter.Label object for footer text
    start_button: tkinter.Button object for button to start game
    back_button: tkinter.Button object for button to return to main menu
    standings_header: tkinter.Label object for standings header text
    instructions_header: tkinter.Label object for instructions header text
    instructions_text: tkinter.Text object to initialize instructions text. The actual text gets inserted inside the open_standings() -function

    Methods:
    configure_window(self): Center tkinter window, set title and background color
    forget_mainmenu(self): Remove all widgets except footer from main menu
    open_mainmenu(self, first_opening): Add main menu widgets. Add footer only first time opening menu
    start_oneplayer(self): Open single player game configuration window 
    start_twoplayer(self): Open multiplayer game configuration window
    open_standings(self): Open standings
    open_instructions(self): Open instructions
    init_window(self): Initialize interface, configure window, open main menu and start tkinter loop
    """
    def __init__(self):
        self.root = tk.Tk()
        self._screen_width = self.root.winfo_screenwidth()
        self._screen_height = self.root.winfo_screenheight()
        self.header = tk.Label(self.root, text="Pong", font=HEADER_FONT, fg="white", bg="#1D3557")
        self.singleplayer_button = tk.Button(self.root, text="Yksinpeli", font=TEXT_FONT, width=20, height=2, command=self.start_oneplayer,
                                             bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        self.twoplayer_button = tk.Button(self.root, text="Kaksinpeli", font=TEXT_FONT, width=20, height=2, command=self.start_twoplayer,
                                          bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        self.standings_button = tk.Button(self.root, text="Tulostaulu", font=TEXT_FONT, width=20, height=2, command=self.open_standings,
                                          bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        self.instructions_button = tk.Button(self.root, text="Ohjeet", font=TEXT_FONT, width=20, height=2, command=self.open_instructions,
                                             bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        self.footer = tk.Label(self.root, text="Ohjelmistotekniikka 2023", font=("Helvetica", 10), fg="white", bg="#1D3557")
        self.start_button = tk.Button(self.root, text="Aloita peli", font=TEXT_FONT, width=20, height=2,
                                      bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        self.back_button = tk.Button(self.root, text="Takaisin", font=TEXT_FONT, width=20, height=2,
                                     bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        self.standings_header = tk.Label(self.root, text="Tulostaulu", font=HEADER_FONT, fg="white", bg="#1D3557")
        self.instructions_header = tk.Label(self.root, text="Ohjeet", font=HEADER_FONT, fg="white", bg="#1D3557")
        self.instructions_text = tk.Text(self.root, bg="#1D3557", fg="white", relief=tk.FLAT, highlightthickness=0, selectborderwidth=0,
                                         selectbackground="#1D3557", selectforeground="white")

    def configure_window(self):
        x_coordinate = int((self._screen_width/2) - (WINDOW[0]/2))
        y_coordinate = int((self._screen_height/2) - (WINDOW[0]/2))

        self.root.geometry(f"400x400+{x_coordinate}+{y_coordinate}")
        self.root.title("Pong")
        self.root.configure(bg="#1D3557")

    def forget_mainmenu(self):
        self.header.pack_forget()
        self.singleplayer_button.pack_forget()
        self.twoplayer_button.pack_forget()
        self.standings_button.pack_forget()
        self.instructions_button.pack_forget()
    
    def open_mainmenu(self, first_opening):
        self.header.pack(pady=(20,10))
        self.singleplayer_button.pack(pady=10)
        self.twoplayer_button.pack(pady=10)
        self.standings_button.pack(pady=10)
        self.instructions_button.pack(pady=10)
        if first_opening:
            self.footer.pack(side="bottom", pady=10)

    def start_oneplayer(self):
        self.forget_mainmenu()

        player1_label = tk.Label(self.root, text="Pelaajan nimi:", font=TEXT_FONT, fg="white", bg="#1D3557")
        player1_label.pack(pady=(30,10))
        player1_entry = tk.Entry(self.root, font=TEXT_FONT)
        player1_entry.pack(pady=10)

        def start_game():
            player1_name = player1_entry.get()
            player2_name = "Pong-botti"
            self.root.destroy()
            oneplayer = OnePlayer(player1_name, player2_name)
            oneplayer.start()
            init_window()

        self.start_button.config(command=start_game)
        self.start_button.pack(pady=(120,5))

        def reopen_menu():
            self.open_mainmenu(False)
            player1_label.pack_forget()
            player1_entry.pack_forget()
            self.start_button.pack_forget()
            self.back_button.pack_forget()

        self.back_button.config(command=reopen_menu)
        self.back_button.pack(pady=10)

        self.root.mainloop()

    def start_twoplayer(self):
        self.forget_mainmenu()

        player1_label = tk.Label(self.root, text="Pelaajan 1 nimi:", font=TEXT_FONT, fg="white", bg="#1D3557")
        player1_label.pack(pady=(20, 5))
        player1_entry = tk.Entry(self.root, font=TEXT_FONT)
        player1_entry.pack(pady=(3, 5))

        player2_label = tk.Label(self.root, text="Pelaajan 2 nimi:", font=TEXT_FONT, fg="white", bg="#1D3557")
        player2_label.pack(pady=5)
        player2_entry = tk.Entry(self.root, font=TEXT_FONT)
        player2_entry.pack(pady=(3, 5))

        length_var = tk.StringVar(value="5")
        length_label = tk.Label(self.root, text="Pelin pituus (pisteinä):", font=TEXT_FONT, fg="white", bg="#1D3557")
        length_label.pack(pady=(10, 0))
        length_frame = tk.Frame(self.root, bg="#1D3557")
        length_frame.pack()
        length3_button = tk.Radiobutton(length_frame, text="3", variable=length_var, value="3", font=TEXT_FONT, bg="#1D3557", fg="white", activebackground="#1D3557", activeforeground="white", selectcolor="#E63946", highlightthickness=0)
        length3_button.pack(side="left", pady=(0,10))
        length5_button = tk.Radiobutton(length_frame, text="5", variable=length_var, value="5", font=TEXT_FONT, bg="#1D3557", fg="white", activebackground="#1D3557", activeforeground="white", selectcolor="#E63946", highlightthickness=0)
        length5_button.pack(side="left", pady=(0,10))
        length10_button = tk.Radiobutton(length_frame, text="10", variable=length_var, value="10", font=TEXT_FONT, bg="#1D3557", fg="white", activebackground="#1D3557", activeforeground="white", selectcolor="#E63946", highlightthickness=0)
        length10_button.pack(side="left", pady=(0,10))

        def start_game():
            player1_name = player1_entry.get()
            player2_name = player2_entry.get()
            self.root.destroy()
            twoplayer = TwoPlayer(player1_name, player2_name, length=int(length_var.get()))
            twoplayer.start()
            init_window()

        self.start_button.config(command=start_game)
        self.start_button.pack(pady=(5, 0))

        def reopen_menu():
            self.open_mainmenu(False)
            player1_label.pack_forget()
            player1_entry.pack_forget()
            player2_label.pack_forget()
            player2_entry.pack_forget()
            length_label.pack_forget()
            length_frame.pack_forget()
            self.start_button.pack_forget()
            self.back_button.pack_forget()

        self.back_button.config(command=reopen_menu)
        self.back_button.pack(pady=(5, 10), side="bottom")

        self.root.mainloop()

    def open_standings(self):
        self.forget_mainmenu()
        self.standings_header.pack(pady=(20,10))

        scores_text = leaderboard_text()
        highscore_text = tk.Text(self.root, bg="#1D3557", fg="white", relief=tk.FLAT, highlightthickness=0, selectborderwidth=0,
                                 selectbackground="#1D3557", selectforeground="white", font=("Helvetica", 18))
        highscore_text.insert("end", scores_text)
        highscore_text.config(state="disabled")

        highscore_text.pack(pady=5)

        def reopen_menu():
            self.open_mainmenu(False)
            self.standings_header.pack_forget()
            highscore_text.forget()
            back_button.destroy()

        back_button = tk.Button(self.root, text="Takaisin", font=TEXT_FONT, width=20, height=2, command=reopen_menu,
                                bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        back_button.place(x=85, y=300)


    def open_instructions(self):
        self.forget_mainmenu()
 
        self.instructions_header.pack(pady=(20, 10))

        self.instructions_text.insert("end", INST_TEXT)
        self.instructions_text.config(state="disabled")
                                    
        self.instructions_text.pack(pady=(5))

        def reopen_menu():
            self.open_mainmenu(False)
            self.instructions_header.pack_forget()
            self.instructions_text.pack_forget()
            back_button.destroy()

        back_button = tk.Button(self.root, text="Takaisin", font=TEXT_FONT, width=20, height=2, command=reopen_menu,
                                bg="#E63946", fg="white", activebackground="#E07178", activeforeground="white", relief=tk.RAISED)
        back_button.place(x=85, y=300)

def init_window():
    ui = Ui()
    ui.configure_window()
    ui.open_mainmenu(True)
    ui.root.mainloop()
