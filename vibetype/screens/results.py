from vibetype.base import BaseScreen

from textual.containers import Vertical, CenterMiddle
from textual.widgets import Static
from .type_space import StartType

class ResultScreen(BaseScreen):

    def action_close_screen(self):
        self.app.sesh_max=None
        self.app.sesh_min=None
        super().action_close_screen()

    def action_next(self):
        from .type_space import StartType # lazy import
        self.app.switch_screen(StartType(self.mode))

    BINDINGS=[
        ('enter','next','Next Sentence'),
    ]

    def __init__(self,mode,sentence='',details='',*,raw_wpm,wpm,accuracy):
        super().__init__()
        self.mode=mode

        self.sentence=sentence
        self.details=details
        self.raw_wpm=raw_wpm
        self.wpm=wpm
        self.accuracy=accuracy

    def compose_body(self):
        with CenterMiddle():
            with Vertical(classes='cont results'):
                yield Static(self.sentence)
                if(self.details):
                    yield Static(self.details)
                yield Static(f'WPM: {self.wpm}\nRaw WPM: {self.raw_wpm}\nAccuracy: {self.accuracy}%')