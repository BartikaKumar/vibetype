from vibetype.base import BaseScreen

class StartType(BaseScreen):

    def __init__(self, mode='random'):
            super().__init__()
            self.mode=mode

    def compose_body(self):
        pass