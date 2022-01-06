from boggle_gui import BoggleGUI
from boggle_model import BoogleModel
from start_gui import StartGUI
from typing import Callable


class BoggleGame:
    def __init__(self):
        self.welcome_page = StartGUI()
        self._boggle_model = BoogleModel()
        self._board = self._boggle_model.board
        self._boggle_gui = BoggleGUI(self._board)

        buttons = self._boggle_gui.get_button_chars()
        for button_text in buttons:
            action = self.create_button_action(buttons[button_text])
            self._boggle_gui.set_button_command(button_text, action)
        self._boggle_gui.update_display("")


    def create_button_action(self, button) -> Callable[[], None]:
        def fun() -> None:
            # self._boggle_model.type_in(button_text)
            if button[0]["text"] == 'choose':
                word = self._boggle_model.choose_word()
                if word:
                    self._boggle_gui.update_words_display(word, self._boggle_model.score)
            else:
                cord = (button[1][0], button[1][1])
                if self.is_valid_press(cord):
                    self._boggle_model.update_current_path(cord)
            self._boggle_gui.update_display(button[0]["text"])

        return fun

    def is_valid_press(self, cord):
        is_valid = True
        if len(self._boggle_model.current_path) != 0:
            y_distance = abs(self._boggle_model.current_path[-1][0] - cord[0])
            x_distance = abs(self._boggle_model.current_path[-1][1] - cord[1])
            is_valid = y_distance in [0, 1] and x_distance in [0, 1] and cord not in self._boggle_model.current_path
        return is_valid

    def run(self) -> None:
        self._boggle_gui.run()


if __name__ == '__main__':
    B = BoggleGame()
    if B.welcome_page.game_started:
        B.run()


# if button_char in {"clear", "choose"}:
#     if button_char == "choose":
#         # do logic
#         pass
#     self.__clear_buttons()
# else:
#     self._display_label["text"] += button_char