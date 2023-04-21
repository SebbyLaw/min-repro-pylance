from __future__ import annotations


from footypes import BAR


# everything works fine here
class Foo:
    def __init__(self, bar: BAR) -> None:
        self.bar: BAR = bar

    @staticmethod
    def make_foo(bar: BAR) -> Foo:  # self-referential return type requires future annotations
        return Foo(bar)


# other functions, classes, etc.
