from textual.screen import Screen
from textual.widgets import Footer, Static



class BaseScreen(Screen):

    def action_close_screen(self):
        self.app.pop_screen()

    BINDINGS=[
        ('escape','close_screen','Return to Menu'),
    ]

    def compose(self):
        yield Static("VibeType",classes='header')
        yield from self.compose_body()
        yield Footer()

    def compose_body(self):
        pass