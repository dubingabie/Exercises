from boggle_gui import BoogleGUI
from boggle_model import BoogleModel


class BoggleGame:
    def __init__(self):
        self._boggle_model = BoogleModel()
        self._boggle_gui = BoogleGUI(self._boggle_model.board)

    def run(self) -> None:
        self._boggle_gui.run()




# if button_char in {"clear", "choose"}:
#     if button_char == "choose":
#         # do logic
#         pass
#     self.__clear_buttons()
# else:
#     self._display_label["text"] += button_char