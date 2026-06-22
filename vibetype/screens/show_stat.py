from vibetype.base import BaseScreen

class ShowStat(BaseScreen):

    def load_stats(self):
        cursor=self.app.conn.cursor()

    def on_mount(self) -> None:
        self.load_stats()

    def compose_body(self):
        pass