from gi.repository import Gtk

grid = Gtk.Grid()

button_dot = Gtk.Button(label=".")
button0 = Gtk.Button(label="0")
button_eq = Gtk.Button(label="=")

button_c = Gtk.Button(label="C")
button_plus = Gtk.Button(label="+")
button_minus = Gtk.Button(label="-")
button_mult = Gtk.Button(label="×")
button_div = Gtk.Button(label="÷")

grid.attach(button_dot, 0, 4, 1, 1)
grid.attach(button0, 1, 4, 1, 1)
grid.attach(button_eq, 2, 4, 1, 1)
grid.attach(button_c, 4, 0, 1, 1)
grid.attach(button_plus, 4, 1, 1, 1)
grid.attach(button_minus, 4, 2, 1, 1)
grid.attach(button_mult, 4, 3, 1, 1)
grid.attach(button_div, 4, 4, 1, 1)
