from textual.app import App
from textual.containers import Vertical
from textual.widgets import Static

TEXT = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain.
"""


class ScrollbarApp(App):
    def compose(self):
        yield Vertical(Static(TEXT * 5), classes="panel1")
        yield Vertical(Static(TEXT * 5), classes="panel2")


app = ScrollbarApp(css_path="scrollbars.css")
