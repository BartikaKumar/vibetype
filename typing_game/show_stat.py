from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import CenterMiddle,Vertical
from textual.widgets import Header,Footer

class ShowStat(Screen):

    def load_stats(self):
        cursor=self.app.conn.cursor()

    def on_mount(self) -> None:
        self.load_stats()

    def action_close_screen(self):
        self.app.pop_screen()

    BINDINGS=[
        ('escape','close_screen','Return to Menu'),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()