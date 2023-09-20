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

        index = 0
        while index < 10:
            button = Gtk.Button(label=f"{index + 1}")
            if index < 3:
                grid.attach(button, index, 1, 1, 1)
            elif 2 < index < 6:
                grid.attach(button, index - 3, 2, 1, 1)
            elif 5 < index < 9:
                grid.attach(button, index - 6, 3, 1, 1)
            button.connect("clicked", self.clicked_button, str(index + 1))
            index += 1

        button_functions = {
            "0": self.clicked_button,
            "dot": self.clicked_button,
            "plus": self.clicked_button,
            "minus": self.clicked_button,
            "mult": self.clicked_button,
            "div": self.clicked_button,
            "eq": self.clicked_button,
            "c": self.clicked_button,
        }

        for button_name, function in button_functions.items():
            buttons[button_name].connect("clicked", function, button_name)

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
