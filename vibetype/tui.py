from textual.app import App

from pathlib import Path
import sqlite3

from .screens.menu import MenuScreen

class VibeType(App):
    ENABLE_COMMAND_PALETTE=False
    TITLE = "VibeType"

    def on_mount(self) -> None:
        self.theme = "catppuccin-mocha"
        self.conn=sqlite3.connect(Path(__file__).parent.parent / 'data' / 'type_stats.db')
        self.push_screen(MenuScreen())

    CSS_PATH='typelearn.tcss'

def main():
    app = VibeType()
    app.run()

if __name__=="__main__":
    raise SystemExit(main())