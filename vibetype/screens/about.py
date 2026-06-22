from vibetype.base import BaseScreen

from textual.containers import Vertical
from textual.widgets import Static

class ShowAbout(BaseScreen):

    def compose_body(self):
        with Vertical(classes='cont'):
                yield Static(
                    "Welcome to VibeType!\n\n"
                    "Here you can type away with themed sentence packs, or just random words that make no sense. This is an offline, keyboard-first space that's entirely yours.\n\n"
                    "P.S. For learning-based themes, typing is not enough! Read and sit with the sentence and its related fact before moving on to the next one :)",
                    classes='welcome'
                )