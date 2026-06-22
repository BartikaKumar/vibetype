from vibetype.base import BaseScreen

from textual.containers import Vertical, CenterMiddle
from textual.widgets import OptionList
from textual.widgets.option_list import Option

from .add_cust import AddCustom
from .about import ShowAbout
from .mode import ChooseMode

class MenuScreen(BaseScreen):

    def action_show_about(self):
        self.app.push_screen(ShowAbout())

    def action_show_stat(self):
        self.app.push_screen(ChooseMode())

    def action_add_custom(self):
        self.app.push_screen(AddCustom())

    def action_start_type(self):
        self.app.push_screen(ChooseMode())

    def action_close_app(self):
        self.app.conn.close()
        self.app.exit()

    BINDINGS=[
        ('a','add_custom','Add Custom Fact'),
        ('escape','close_app','Exit'),
    ]

    def on_option_list_option_selected(self,event: OptionList.OptionSelected):
        option_id=event.option.id
        if option_id=='exit_app':
            self.action_close_app()
        elif option_id=='show_about':
            self.action_show_about()
        elif option_id=='show_stat':
            self.action_show_stat()
        elif option_id=='start_type':
            self.action_start_type()

    def compose_body(self):
        with CenterMiddle():
            with Vertical(classes='cont'):
                yield OptionList(
                    Option('About',id='show_about'),
                    None,
                    Option('Start',id='start_type'),
                    None,
                    Option('Statistics',id='show_stat'),
                    None,
                    Option('Exit',id='exit_app'),
                )