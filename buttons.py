from gi.repository import Gtk

grid = Gtk.Grid()


def create_button(grid, label, pos_x, pos_y):
    button = Gtk.Button(label=label)
    grid.attach(button, pos_x, pos_y, 1, 1)
    return button


buttons = {
    "dot": create_button(grid, ".", 0, 4),
    "0": create_button(grid, "0", 1, 4),
    "plus": create_button(grid, "+", 4, 1),
    "minus": create_button(grid, "-", 4, 2),
    "mult": create_button(grid, "×", 4, 3),
    "div": create_button(grid, "÷", 4, 4),
    "eq": create_button(grid, "=", 2, 4),
    "c": create_button(grid, "C", 4, 0),
}
