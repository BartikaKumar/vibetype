from vibetype.base import BaseScreen

from textual.containers import Vertical, CenterMiddle
from textual.widgets import Label
from rich.text import Text

class StartType(BaseScreen):

    def __init__(self, mode='random'):
            super().__init__()
            self.mode=mode

            self.curr=''

            self.target=['the','quick','brown','fox']
            self.typed=['']*len(self.target)
            
            self.at_word=0

    def render_text(self):

        full=Text()
        to_match=self.target[self.at_word]

        pword=0

        while(pword<len(self.target)):

            if pword<self.at_word:
                if(self.typed[pword]==self.target[pword]):
                    full.append(self.target[pword],style=str(self.app.theme_variables['primary']))
                else:
                    full.append(self.target[pword],style=f"{self.app.theme_variables['error']} underline")
            elif pword==self.at_word:
                p=0
                while(p<len(self.curr)):
                    if(p<len(to_match)):
                        if(self.curr[p]!=self.target[self.at_word][p]):
                            full.append(self.curr[p],style=str(self.app.theme_variables['error']))
                        else:
                            full.append(self.curr[p],style=str(self.app.theme_variables['primary']))
                    else:
                        full.append(self.curr[p],style=str(self.app.theme_variables['error-muted']))
                    p+=1
                while(p<len(to_match)):
                    full.append(to_match[p],style=str(self.app.theme_variables['primary-muted']))
                    p+=1
            else:
                full.append(self.target[pword],style=str(self.app.theme_variables['primary-muted']))
            
            full.append(' ')
            pword+=1

        self.query_one("#target").update(full)



    def on_key(self,event):
        if event.key=='backspace':
            if len(self.curr)>0:
                self.curr = self.curr[:-1]

            elif len(self.curr)==0 and self.at_word>0:
                self.at_word-=1
                self.curr=self.typed[self.at_word]
                self.typed[self.at_word] = ""

        elif event.key=='space':
            if self.curr and self.at_word<len(self.target)-1:
                self.typed[self.at_word]=self.curr
                self.curr=''
                self.at_word+=1
                
        elif event.character:
            self.curr=self.curr+event.character

        self.render_text()

        if self.at_word==len(self.target)-1 and self.curr==self.target[-1]:
            self.typed[self.at_word] = self.curr
            self.app.pop_screen()

    def compose_body(self):
        with CenterMiddle():
            with Vertical(classes='cont'):
                    yield Label(Text(' '.join(self.target)+' ',style=str(self.app.theme_variables['primary-muted'])),id='target')