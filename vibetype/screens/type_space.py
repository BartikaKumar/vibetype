from vibetype.base import BaseScreen

from textual.containers import Vertical, CenterMiddle
from textual.widgets import Static
from rich.text import Text

import random
import time

class StartType(BaseScreen):

    def action_close_screen(self):
        self.app.sesh_max=None
        self.app.sesh_min=None
        super().action_close_screen()

    def load_screen(self,wpm=None,raw_wpm=None,accuracy=None):
        self.curr=''
        self.word=Text()

        cursor=self.app.conn_data.cursor()
        if self.app.sesh_min is None:
            self.app.sesh_min,self.app.sesh_max= cursor.execute(f"SELECT MIN(id), MAX(id) FROM {self.mode}").fetchone()

        if self.mode=='random':
            ids=random.sample(range(self.app.sesh_min,self.app.sesh_max+1),self.app.random_words)
            placeholders=",".join("?"*len(ids))
            rows=cursor.execute(f"SELECT word FROM {self.mode} WHERE id IN ({placeholders})",ids).fetchall()
            self.sentence=" ".join(row[0] for row in rows)
            self.details=""

        else:  
            id=random.randint(self.app.sesh_min,self.app.sesh_max)
            row=cursor.execute(f"SELECT * FROM {self.mode} WHERE id={id}").fetchone()
            self.sentence=row[1]
            self.details=row[2]

        self.target=self.sentence.split(' ')
        self.typed=[None]*len(self.target)
        self.typed_str=['']*len(self.target)
            
        self.at_word=0

        self.correct=0
        self.incorrect=0

        self.start_time=None

        if wpm is not None:
            self.query_one(".header").update(f"VibeType | WPM: {wpm} | Raw WPM: {raw_wpm} | Accuracy: {accuracy}")

        self.target_widget.update(Text(self.sentence+' ',style=str(self.app.theme_variables['primary-muted'])))

    def __init__(self, mode='random'): # runs before compose
            super().__init__()
            self.mode=mode

    def on_mount(self): # runs after compose
        self.target_widget=self.query_one("#target")
        self.load_screen()

    def render_text(self):

        full=Text()
        to_match=self.target[self.at_word]

        pword=0

        while(pword<len(self.target)):

            if pword<self.at_word:
                full.append_text(self.typed[pword])
                    
            elif pword==self.at_word:

                p=0
                self.word=Text()

                while(p<len(self.curr)):
                    if(p<len(to_match)):
                        if(self.curr[p]!=self.target[self.at_word][p]):
                            self.word.append(self.curr[p],style=str(self.app.theme_variables['error']))
                
                        else:
                            self.word.append(self.curr[p],style=str(self.app.theme_variables['primary']))

                    else:
                        self.word.append(self.curr[p],style=str(self.app.theme_variables['error-muted']))

                    p+=1

                while(p<len(to_match)):
                    self.word.append(to_match[p],style=str(self.app.theme_variables['primary-muted']))
                    p+=1
                
                full.append_text(self.word)

            else:
                full.append(self.target[pword],style=str(self.app.theme_variables['primary-muted']))
            
            full.append(' ')
            pword+=1

        self.target_widget.update(full)



    def on_key(self,event):

        modified=False

        if event.key=='backspace':
            if len(self.curr)>0:
                self.curr = self.curr[:-1]
                modified=True

            elif len(self.curr)==0 and self.at_word>0:

                self.at_word-=1

                self.word=self.typed[self.at_word].copy()
                self.curr=self.typed_str[self.at_word]

                modified=True

        elif event.key=='space':
            if self.curr and self.at_word<len(self.target)-1:

                if len(self.curr)>=len(self.target[self.at_word]):
                    self.correct+=1
                else:
                    self.incorrect+=1

                self.typed[self.at_word]=self.word.copy()
                self.typed_str[self.at_word]=self.curr

                self.curr=''

                self.word=Text()
                self.at_word+=1

                modified=True
                
        elif event.character and event.character.isprintable():
            self.curr=self.curr+event.character

            if len(self.curr)<=len(self.target[self.at_word]) and event.character==self.target[self.at_word][len(self.curr)-1]:
                self.correct+=1
            else:
                self.incorrect+=1
        
            modified=True

        self.render_text()

        if modified and self.start_time is None:
            self.start_time=time.perf_counter()

        if self.at_word==len(self.target)-1 and self.curr==self.target[-1]:

            duration=time.perf_counter()-self.start_time

            raw_wpm=round((self.correct+self.incorrect)*12/duration,2)
            wpm=round(self.correct*12/duration,2)
            accuracy=round(self.correct*100/(self.correct+self.incorrect),2)

            self.typed[self.at_word] = self.word.copy()
            self.typed_str[self.at_word]=self.curr

            if(self.mode=="random"):
                self.load_screen(wpm,raw_wpm,accuracy)
            else:
                from .results import ResultScreen # lazy import to prevent circular import issue
                self.app.switch_screen(ResultScreen(self.mode,self.sentence,self.details,raw_wpm=raw_wpm,wpm=wpm,accuracy=accuracy))

    def compose_body(self):
        with CenterMiddle():
            with Vertical(classes='cont'):
                    yield Static('',id='target')