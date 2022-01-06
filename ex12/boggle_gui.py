import sys
import tkinter as tki
from boggle_board_randomizer import randomize_board
from typing import Callable, Dict, List, Any

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



class BoggleGUI:
    _buttons: Dict[str, tuple[tki.Button, [int, int]]] = {}

    def __init__(self, board):
        self._score = 0
        self._board = board
        self.all_words = list()
        self.game_started = False

        root = tki.Tk()
        root.title("Boggle")
        root.resizable(False, False)

        self._main_window = root
        self.create_all_displays()
        self._create_buttons_in_lower_frame()
        self.countdown(45)
        self._main_window.bind("<Key>", self._key_pressed)

        # self.start_game_pop_up()


    def create_all_displays(self):
        self.left_side_frame = tki.Frame(self._main_window, bg=REGULAR_COLOR, highlightbackground=REGULAR_COLOR,
                                         highlightthickness=5)
        self.left_side_frame.pack(side=tki.LEFT, fill=tki.BOTH, expand=True)

        self.setting_frame = tki.Frame(self.left_side_frame, bg=REGULAR_COLOR, highlightbackground=REGULAR_COLOR)
        self.setting_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self.timer_label = tki.Label(self.setting_frame, bg=REGULAR_COLOR, relief="ridge",
                                     highlightbackground=REGULAR_COLOR, text="time:")
        self.timer_label.pack(side=tki.TOP, fill=tki.BOTH)

        self.score_label = tki.Label(self.setting_frame, bg=REGULAR_COLOR, relief="ridge", text=f'score: {self._score}')
        self.score_label.pack(side=tki.TOP, fill=tki.BOTH)

        self._words_lable = tki.Label(self.left_side_frame, font=("Courier", 15), bg=REGULAR_COLOR, width=23, text="")
        self._words_lable.pack(side=tki.TOP, fill=tki.BOTH)

        self._outer_frame = tki.Frame(self._main_window, bg=REGULAR_COLOR, highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._display_label = tki.Label(self._outer_frame, font=("Courier", 30),
                                        bg=REGULAR_COLOR, width=23, relief="ridge")
        self._display_label.pack(side=tki.TOP, fill=tki.BOTH)

        self._lower_frame = tki.Frame(self._outer_frame)
        self._lower_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)




    def end_game_pop_up(self):
        self._main_window.destroy()
        self.root = tki.Tk()
        self.root.title("GAME OVER")
        end_frame = tki.Frame(self.root, bg=REGULAR_COLOR, highlightbackground=REGULAR_COLOR, highlightthickness=5)
        end_frame.pack(fill=tki.BOTH, expand=True)

        score_display = tki.Label(end_frame, font=("Courier", 20), bg=REGULAR_COLOR, width=30, height=10,
                                  relief="ridge",
                                  text=f"Your final \nscore is: {self._score}")
        all_words_end = ""
        for word in self.all_words:
            all_words_end += word + '\n'
        words_display = tki.Label(end_frame, font=("Courier", 20), bg=REGULAR_COLOR, width=30, height=10,
                                  relief="ridge",
                                  text=f"The words you \nfound are: \n{all_words_end}")

        words_display.pack(side=tki.LEFT, fill=tki.BOTH)
        score_display.pack(side=tki.LEFT, fill=tki.BOTH)
        self.root.mainloop()

    def countdown(self, count):
        sec = str(count % 60)
        minute = str(count // 60 if count >= 60 else 0)

        sec = ('0' + sec) if len(sec) == 1 else sec
        minute = ('0' + minute) if len(minute) == 1 else minute

        self.timer_label['text'] = f'time left: {minute}:{sec}'

        if count > 0:
            # call countdown again after 1000ms (1s)
            self._main_window.after(1000, self.countdown, count - 1)

        else:
            self.end_game_pop_up()

    def run(self) -> None:
        self._main_window.mainloop()

    def update_display(self, display_text: str) -> None:
        if display_text in ['clear', 'choose']:
            self._display_label["text"] = ""
        else:
            self._display_label["text"] += display_text

    def update_words_display(self, word: str, score: int) -> None:
        # self._words_frame["text"] += word + '\n'
        if word not in self.all_words:
            self.all_words.append(word)
            self._words_lable["text"] += word + '\n'
        self._score = score
        self.score_label["text"] = f'score: {self._score}'

    def set_button_command(self, button_name: str, cmd: Callable[[], None]) -> None:
        self._buttons[button_name][0].configure(command=cmd)

    def _create_buttons_in_lower_frame(self) -> None:
        for i in range(4):
            tki.Grid.columnconfigure(self._lower_frame, i, weight=1)  # type: ignore

        for i in range(5):
            tki.Grid.rowconfigure(self._lower_frame, i, weight=1)  # type: ignore

        for i in range(4):
            for j in range(4):
                self._make_button(self._board[i][j], i, j)

        self._make_button("clear", 4, 0, columnspan=2)
        self._make_button("choose", 4, 2, columnspan=2)

    def _make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1) -> tki.Button:

        button = tki.Button(self._lower_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._buttons[f'{row},{col}'] = (button, (row, col))
        self.last_button_pressed = None

        def _on_press(event: Any) -> None:
            if button['background'] == REGULAR_COLOR:
                button['background'] = BUTTON_ACTIVE_COLOR
            else:
                button['background'] = REGULAR_COLOR

            if button_char in {"clear", "choose"}:
                button['background'] = REGULAR_COLOR
                self.__clear_buttons()


        button.bind("<Button-1>", _on_press)
        return button

    def get_button_chars(self):
        return self._buttons

    def __clear_buttons(self):
        self.update_display("")
        for button in self._buttons.values():
            button[0]["background"] = REGULAR_COLOR

    def _key_pressed(self, event: Any) -> None:
        """the callback method for when a key is pressed.
        It'll simulate a button press on the right button."""
        if event.char in self._buttons:
            self._simulate_button_press(event.char)

    def _simulate_button_press(self, button_char: str) -> None:
        """make a button light up as if it is pressed,
        and then return to normal"""
        button = self._buttons[button_char]
        button[0]["bg"] = BUTTON_ACTIVE_COLOR

        # def return_button_to_normal() -> None:
        #     if button_char in ["choose","clear"]:
        #         button["bg"] = REGULAR_COLOR
        #
        # button.invoke()  # type: ignore
        # button.after(100, func=return_button_to_normal)


