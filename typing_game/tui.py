from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import CenterMiddle,Vertical
from textual.widgets import Footer, Header, OptionList
from textual.widgets.option_list import Option

from .show_stat import ShowStat

from pathlib import Path
import sqlite3

class MenuScreen(Screen):

    def action_show_stat(self):
        self.app.push_screen(ShowStat())

    def action_add_custom(self):
        self.app.push_screen(AddCustom())

    def action_start_type(self):
        self.app.push_screen(StartType())

    def action_close_app(self):
        self.app.conn.close()
        self.app.exit()

    BINDINGS=[
        ('escape','close_app','Exit'),
    ]

    def on_option_list_option_selected(self,event: OptionList.OptionSelected):
        option_id=event.option.id
        if option_id=='exit_app':
            self.action_close_app()
        elif option_id=='add_custom':
            self.action_add_custom()
        elif option_id=='show_stat':
            self.action_show_stat()
        elif option_id=='start_type':
            self.action_start_type()

    def compose(self) -> ComposeResult:
        yield Header()
        with CenterMiddle():
            with Vertical(id="menu"):
                yield OptionList(
                    Option('Start',id='start_type'),
                    None,
                    Option('Statistics',id='show_stat'),
                    None,
                    Option('Add Custom',id='add_custom'),
                    None,
                    Option('Exit',id='exit_app'),
                )
        yield Footer()

class TypeLearn(App):

    def on_mount(self) -> None:
        self.theme = "catppuccin-mocha"
        self.conn=sqlite3.connect(Path(__file__).parent.parent / 'data' / 'type_stats.db')
        self.push_screen(MenuScreen())

    CSS_PATH='typelearn.tcss'

def main():
    app = TypeLearn()
    app.run()

if __name__=="__main__":
    raise SystemExit(main())