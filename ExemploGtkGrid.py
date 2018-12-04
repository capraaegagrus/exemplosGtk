import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.Grid")

        grid = Gtk.Grid()
        self.add(grid)

        boton1 = Gtk.Button(label = "Boton1")
        boton2 = Gtk.Button(label = "Boton2")
        boton3 = Gtk.Button(label = "Boton3")
        boton4 = Gtk.Button(label = "Boton4")
        boton5 = Gtk.Button(label = "Boton5")
        boton6 = Gtk.Button(label = "Boton6")

        grid.attach (boton1, 0, 0, 1,1)
        grid.attach (boton2, 1, 0, 2, 1) # control, columna, fila , ancho, alto
        grid.attach_next_to (boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to (boton4, boton3, Gtk.PositionType.RIGHT, 2, 1)
        #grid.attach_next_to (boton4, boton2, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach (boton6, 2, 2, 1, 1)

        self.connect ("destroy", Gtk.main_quit)
        self.show_all()




if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()