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


class BoogleGUI:
    _buttons: Dict[str, tki.Button] = {}

    def __init__(self, board):
        self._score = 0
        self._board = board
        root = tki.Tk()
        root.title("Boggle")
        root.resizable(False, False)
        self._main_window = root

        self.left_frame = tki.Frame(root,
                                    bg=REGULAR_COLOR,
                                    highlightbackground=REGULAR_COLOR,
                                    highlightthickness=5)

        self.left_frame.pack(side=tki.LEFT, fill=tki.BOTH)
        self.result_label = tki.Label(self.left_frame, font=("Courier", 15), bg=REGULAR_COLOR, width=23, relief="ridge")
        self.result_label.pack(side=tki.LEFT, fill=tki.BOTH)

        self._outer_frame = tki.Frame(root,
                                      bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)

        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self.score_label = tki.Label(self._outer_frame, bg=REGULAR_COLOR, width=23, relief="ridge")
        self.score_label.pack(side=tki.TOP, fill=tki.BOTH)

        self._display_label = tki.Label(self._outer_frame, font=("Courier", 30),
                                        bg=REGULAR_COLOR, width=23, relief="ridge")
        self._display_label.pack(side=tki.TOP, fill=tki.BOTH)

        self._lower_frame = tki.Frame(self._outer_frame)
        self._lower_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._create_buttons_in_lower_frame()
        self._main_window.bind("<Key>", self._key_pressed)

    def run(self) -> None:
        self._main_window.mainloop()

    def set_display(self, display_text: str) -> None:
        self._display_label["text"] = display_text

    def set_button_command(self, button_name: str, cmd: Callable[[], None]) -> None:
        self._buttons[button_name].configure(command=cmd)

    def _create_buttons_in_lower_frame(self) -> None:
        for i in range(4):
            tki.Grid.columnconfigure(self._lower_frame, i, weight=1)  # type: ignore

        for i in range(5):
            tki.Grid.rowconfigure(self._lower_frame, i, weight=1)  # type: ignore

        self._board = randomize_board()
        for i in range(4):
            for j in range(4):
                self._make_button(self._board[i][j], i, j)

        self._make_button("clear", 4, 0, columnspan=2)
        self._make_button("choose", 4, 2, columnspan=2)

    def _make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1) -> tki.Button:
        button = tki.Button(self._lower_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._buttons[f'{button_char}-{row},{col}'] = button

        def _on_press(event: Any) -> None:
            if button['background'] == REGULAR_COLOR:
                button['background'] = BUTTON_ACTIVE_COLOR
            else:
                button['background'] = REGULAR_COLOR
            if button_char in {"clear", "choose"}:
                button['background'] = REGULAR_COLOR

        button.bind("<Button-1>", _on_press)
        return button

    def __clear_buttons(self):
        self.set_display("")
        for button in self._buttons.values():
            button["background"] = REGULAR_COLOR

    def _key_pressed(self, event: Any) -> None:
        """the callback method for when a key is pressed.
        It'll simulate a button press on the right button."""
        if event.char in self._buttons:
            self._simulate_button_press(event.char)

    def _simulate_button_press(self, button_char: str) -> None:
        """make a button light up as if it is pressed,
        and then return to normal"""
        button = self._buttons[button_char]
        button["bg"] = BUTTON_ACTIVE_COLOR

        # def return_button_to_normal() -> None:
        #     if button_char in ["choose","clear"]:
        #         button["bg"] = REGULAR_COLOR
        #
        # button.invoke()  # type: ignore
        # button.after(100, func=return_button_to_normal)


if __name__ == "__main__":
    cg = BoogleGUI()
    cg.set_display("TEST MODE")
    cg.run()
