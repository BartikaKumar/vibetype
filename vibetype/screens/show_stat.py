from vibetype.base import BaseScreen

from textual.containers import VerticalScroll, Vertical, CenterMiddle, HorizontalScroll
from textual.widgets import Static, Select

from rich.table import Table

class ShowStat(BaseScreen):

    def load_stats(self,mode=None):
        cursor=self.app.conn_stats.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stats (
                id INTEGER PRIMARY KEY,
                mode TEXT NOT NULL,
                wpm REAL NOT NULL,
                raw_wpm REAL NOT NULL,
                accuracy REAL NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.app.conn_stats.commit()
        if mode is None or mode=="all":
            all_stats=cursor.execute("""
                SELECT
                    ROUND(AVG(wpm),2),
                    MAX(wpm),
                    ROUND(AVG(raw_wpm),2),
                    MAX(raw_wpm),
                    ROUND(AVG(accuracy),2),
                    MAX(accuracy),
                    COUNT(*)
                FROM stats;
            """).fetchone()
            latest_stats=cursor.execute("""
                SELECT
                    ROUND(AVG(wpm),2),
                    MAX(wpm),
                    ROUND(AVG(raw_wpm),2),
                    MAX(raw_wpm),
                    ROUND(AVG(accuracy),2),
                    MAX(accuracy),
                    COUNT(*)
                FROM(
                    SELECT *
                    FROM stats
                    ORDER BY created_at DESC
                    LIMIT 10
                );
            """).fetchone()
        else:
            all_stats=cursor.execute("""
                SELECT
                    ROUND(AVG(wpm),2),
                    MAX(wpm),
                    ROUND(AVG(raw_wpm),2),
                    MAX(raw_wpm),
                    ROUND(AVG(accuracy),2),
                    MAX(accuracy),
                    COUNT(*)
                FROM stats
                WHERE mode=?;
            """,(mode,)).fetchone()
            latest_stats=cursor.execute("""
                SELECT
                    ROUND(AVG(wpm),2),
                    MAX(wpm),
                    ROUND(AVG(raw_wpm),2),
                    MAX(raw_wpm),
                    ROUND(AVG(accuracy),2),
                    MAX(accuracy),
                    COUNT(*)
                FROM(
                    SELECT *
                    FROM stats
                    WHERE mode=?
                    ORDER BY created_at DESC
                    LIMIT 10
                );
            """,(mode,)).fetchone()

        self.count.update(f"Tests: {all_stats[6]}")

        all_table = Table(title="All-time")
        all_table.add_column("Metric", justify="left")
        all_table.add_column("Avg", justify="right")
        all_table.add_column("Max", justify="right")

        l_table = Table(title="Latest 10")
        l_table.add_column("Metric", justify="left")
        l_table.add_column("Avg", justify="right")
        l_table.add_column("Max", justify="right")

        all_table.add_row("WPM",str(all_stats[0]),str(all_stats[1]))
        all_table.add_row("Raw WPM",str(all_stats[2]),str(all_stats[3]))
        all_table.add_row("Accuracy",str(all_stats[4]),str(all_stats[5]))

        l_table.add_row("WPM",str(latest_stats[0]),str(latest_stats[1]))
        l_table.add_row("Raw WPM",str(latest_stats[2]),str(latest_stats[3]))
        l_table.add_row("Accuracy",str(latest_stats[4]),str(latest_stats[5]))

        self.all_time.update(all_table)
        self.latest.update(l_table)

    def on_mount(self) -> None:
        self.count=self.query_one("#count")
        self.all_time=self.query_one("#all_time")
        self.latest=self.query_one("#latest")
        self.load_stats()

    def on_select_changed(self,event:Select.Changed):
        self.load_stats(event.value)

    def compose_body(self):
        with CenterMiddle():
            with VerticalScroll(classes='stats cont'):
                with Vertical():
                    yield Select([
                        ("All modes","all"),
                        ("Random","random"),
                        ("DSA","dsa"),
                        ("Pokemon","pokemon"),
                        ("Anime","anime")
                    ],value="all",allow_blank=False,classes="dropdown",compact=True)
                yield Static("",id="count")
                with HorizontalScroll(classes="horizontal"):
                    yield Static("",id="all_time")
                    yield Static("",id="latest")