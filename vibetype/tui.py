from textual.app import App

from pathlib import Path
import sqlite3

from .screens.menu import MenuScreen

class VibeType(App):
    ENABLE_COMMAND_PALETTE=False
    TITLE = "VibeType"

    def on_mount(self) -> None:
        self.theme = "catppuccin-mocha"

        self.conn_data=sqlite3.connect(Path(__file__).parent / 'data' / 'vibetype_data.db')
        self.conn_stats=sqlite3.connect(Path(__file__).parent / 'data' / 'vibetype_stats.db')

        self.current_sesh_rows=None

        self.push_screen(MenuScreen())

    CSS_PATH='typelearn.tcss'

def main():
    app = VibeType()
    app.run()

if __name__=="__main__":
    raise SystemExit(main())