from textual.app import App
from textual.widgets import Static

class HelloTextualApp(App):
    def compose(self):
        yield Static("Hello, Textual!")

def main():
    app = HelloTextualApp()
    app.run()

if __name__=="__main__":
    raise SystemExit(main())