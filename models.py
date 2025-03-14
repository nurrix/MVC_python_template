from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller import Controller


class Model:
    def __init__(self):
        self.controller: "Controller"

    def set_controller(self, controller: "Controller"):
        self.controller = controller
