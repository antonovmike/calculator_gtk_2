import gi
gi.require_version("Gtk", "3.0")

from buttons import buttons, Gtk, grid
from calculations import do_math


def update_entry(self, new_text):
    current_text = self.entry.props.text
    self.entry.set_text(current_text + new_text)
    # Get text from Entry:
    # a = self.entry.props.text


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
            button.connect("clicked", self.clicked_num_button, index + 1)
            index += 1

        button_functions = {
            "dot": self.clicked_dot,
            "0": self.clicked_0,
            "eq": self.clicked_eq,
            "c": self.clicked_c,
            "plus": self.clicked_plus,
            "minus": self.clicked_minus,
            "mult": self.clicked_mult,
            "div": self.clicked_div
        }

        for button_name, function in button_functions.items():
            buttons[button_name].connect("clicked", function)

        self.add(grid)

    def clicked_num_button(self, entry, number):
        return update_entry(self, str(number))

    def clicked_dot(self, entry):
        return update_entry(self, ".")

    def clicked_0(self, entry):
        return update_entry(self, "0")

    def clicked_eq(self, entry):
        content = self.entry.props.text
        answer = do_math(content)
        self.entry.set_text("")
        add_text = self.entry.props.text + answer
        return update_entry(self, str(add_text))

    def clicked_c(self, entry):
        self.entry.set_text("")

    def clicked_plus(self, entry):
        return update_entry(self, "+")

    def clicked_minus(self, entry):
        return update_entry(self, "-")

    def clicked_mult(self, entry):
        return update_entry(self, "x")

    def clicked_div(self, entry):
        return update_entry(self, "/")


if __name__ == "__main__":
    win = GridWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
