import gi
gi.require_version("Gtk", "3.0")

from buttons import buttons, Gtk, grid
from calculations import do_math


def update_entry(self, new_text):
    current_text = self.entry.props.text
    self.entry.set_text(current_text + new_text)


class GridWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="GTK calculator")

        self.entry = Gtk.Entry()
        self.entry.set_text("")
        grid.attach(self.entry, 0, 0, 3, 1)
        # Get text from Entry:
        # a = self.entry.props.text

        index = 0
        while index < 10:
            button = Gtk.Button(label=f"{index + 1}")
            if index < 3:
                grid.attach(button, index, 1, 1, 1)
            elif 2 < index < 6:
                grid.attach(button, index - 3, 2, 1, 1)
            elif 5 < index < 9:
                grid.attach(button, index - 6, 3, 1, 1)
            button.connect("clicked", self.clicked_button, index)
            index += 1

        buttons["dot"].connect("clicked", self.clicked_dot)
        buttons["0"].connect("clicked", self.clicked_0)
        buttons["eq"].connect("clicked", self.clicked_eq)
        buttons["c"].connect("clicked", self.clicked_c)
        buttons["plus"].connect("clicked", self.clicked_plus)
        buttons["minus"].connect("clicked", self.clicked_minus)
        buttons["mult"].connect("clicked", self.clicked_mult)
        buttons["div"].connect("clicked", self.clicked_div)

        self.add(grid)

    def clicked_button(self, entry, number):
        return update_entry(self, str(number + 1))

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
