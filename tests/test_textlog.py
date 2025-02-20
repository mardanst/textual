from rich.text import Text

from textual.widgets import TextLog


def test_make_renderable_expand_tabs():
    # Regression test for https://github.com/Textualize/textual/issues/3007
    text_log = TextLog()
    renderable = text_log._make_renderable("\tfoo")
    assert isinstance(renderable, Text)
    assert renderable.plain == "        foo"
