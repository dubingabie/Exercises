import tkinter as tki

BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'

BUTTON_STYLE = {
    "font": ("Courier", 30),
    "borderwidth": 1,
    "relief": tki.RAISED,
    "bg": REGULAR_COLOR,
    "activebackground": BUTTON_ACTIVE_COLOR
}


class StartGUI:
    def __init__(self):
        def start():
            self.game_started = True
            self.root.destroy()

        self.root = tki.Tk()
        self.root.title("Boggle")
        self.game_started = False

        start_frame = tki.Frame(self.root, bg=REGULAR_COLOR, highlightbackground=REGULAR_COLOR, highlightthickness=5)
        start_frame.pack(fill=tki.BOTH, expand=True)

        start_label = tki.Label(start_frame, font=("Courier", 20), bg=REGULAR_COLOR,
                                width=30, height=10, relief="ridge", text="Let's start playing!")

        start_label.pack(side=tki.TOP, fill=tki.BOTH)

        play_button = tki.Button(start_frame, text="Play")
        play_button.configure(command=start)
        play_button.pack()
        self.root.mainloop()
