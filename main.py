import gi

gi.require_version("Gtk", "3.0")

from buttons import *
from calculations import do_math

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
                grid.attach(button, index-3, 2, 1, 1)
            elif 5 < index < 9:
                grid.attach(button, index-6, 3, 1, 1)
            button.connect("clicked", self.clicked_button, index)
            index += 1

        button_dot.connect("clicked", self.clicked_dot)
        button0.connect("clicked", self.clicked_0)
        button_eq.connect("clicked", self.clicked_eq)
        button_c.connect("clicked", self.clicked_c)
        button_plus.connect("clicked", self.clicked_plus)
        button_minus.connect("clicked", self.clicked_minus)
        button_mult.connect("clicked", self.clicked_mult)
        button_div.connect("clicked", self.clicked_div)

        self.add(grid)

    def clicked_button(self, entry, number):
        add_text = self.entry.props.text + str(number+1)
        return self.entry.set_text(add_text)

    def clicked_dot(self, entry):
        add_text = self.entry.props.text + "."
        self.entry.set_text(add_text)

    def clicked_0(self, entry):
        add_text = self.entry.props.text + "0"
        self.entry.set_text(add_text)

    def clicked_eq(self, entry):
        content = self.entry.props.text
        answer = do_math(content)
        self.entry.set_text("")
        add_text = self.entry.props.text + answer
        self.entry.set_text(add_text)

    def clicked_c(self, entry):
        self.entry.set_text("")

    def clicked_plus(self, entry):
        add_text = self.entry.props.text + "+"
        self.entry.set_text(add_text)

    def clicked_minus(self, entry):
        add_text = self.entry.props.text + "-"
        self.entry.set_text(add_text)

    def clicked_mult(self, entry):
        add_text = self.entry.props.text + "x"
        self.entry.set_text(add_text)

    def clicked_div(self, entry):
        add_text = self.entry.props.text + "/"
        self.entry.set_text(add_text)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
