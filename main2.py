from __future__ import annotations

from foolib.core import *
from foolib.types import BAR


class Bar:
    def __init__(self, bar: BAR):  # pyright error on this line
        self.foo = Foo(bar)  # okay
        self.bar: BAR = bar  # pyright error on this line


def make_bar(bar: BAR) -> Bar:  # pyright error on this line
    return Bar(bar)  # okay


another_bar: BAR = "bar"  # pyright error on this line
