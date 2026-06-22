from vibetype.base import BaseScreen

from textual.containers import Vertical, CenterMiddle
from textual.widgets import OptionList
from textual.widgets.option_list import Option

from .type_space import StartType

class ChooseMode(BaseScreen):

    def opentype(self,mode='random'):
        self.app.switch_screen(StartType(mode))

    def on_option_list_option_selected(self,event: OptionList.OptionSelected):
        list_id=event.option_list.id
        option_id=event.option.id

        if list_id=='main_modes':
            if option_id=='mode_random':
                self.opentype('random')
            elif option_id=='mode_themed':
                event.option_list.add_class('hidden')
                self.query_one('#theme_modes').remove_class('hidden')
        
        elif list_id=='theme_modes':
            if option_id=='mode_dsa':
                self.opentype('dsa')
            elif option_id=='mode_pokemon':
                self.opentype('pokemon')
            elif option_id=='mode_shakey':
                self.opentype('shakey')

    def compose_body(self):
        with CenterMiddle():
            with Vertical(classes='cont'):
                yield OptionList(
                    Option('Random Words',id='mode_random'),
                    None,
                    Option('Themed Sentence Packs',id='mode_themed'),
                id='main_modes')

                yield OptionList(
                    Option('DSA',id='mode_dsa'),
                    None,
                    Option('Pokemon',id='mode_pokemon'),
                    None,
                    Option('Shakespeare',id='mode_shakey'),
                id='theme_modes',classes='hidden')