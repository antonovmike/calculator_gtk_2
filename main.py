import gi

gi.require_version("Gtk", "3.0")

from buttons import buttons, Gtk, grid
from calculations import do_math


symbols = {
    "0": "0",
    "dot": ".",
    "plus": "+",
    "minus": "-",
    "mult": "x",
    "div": "/",
}


def update_entry(self, new_text):
    current_text = self.entry.props.text
    self.entry.set_text(current_text + new_text)


class GridWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="GTK calculator")

        self.entry = Gtk.Entry()
        self.entry.set_text("")
        grid.attach(self.entry, 0, 0, 3, 1)

        button_labels = [str(i) for i in range(1, 10)]
        button_positions = [(i % 3, i // 3 + 1) for i in range(9)]

        for label, (x, y) in zip(button_labels, button_positions):
            button = Gtk.Button(label=label)
            grid.attach(button, x, y, 1, 1)
            button.connect("clicked", self.clicked_button, label)

        for button in buttons:
            buttons[button].connect("clicked", self.clicked_button, button)

        self.add(grid)

    def clicked_button(self, button, name):
        if name.isdigit():
            return update_entry(self, name)
        elif name in symbols:
            return update_entry(self, symbols[name])
        elif name == "c":
            self.entry.set_text("")
        elif name == "eq":
            content = self.entry.props.text
            answer = do_math(content)
            self.entry.set_text("")
            add_text = self.entry.props.text + answer
            return update_entry(self, str(add_text))


if __name__ == "__main__":
    win = GridWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
