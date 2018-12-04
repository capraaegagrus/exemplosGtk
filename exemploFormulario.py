import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo formulario")

        caixaPrincipal = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 8)
        self.add (caixaPrincipal)
        caixaPrincipal.pack_start (Gtk.Label(label="Información sobre o produto"), True, True, 0)

        Panel = Gtk.Frame (label ="Datos básicos")
        caixaPrincipal.pack_start (Panel, True, True,0)
        caixaAuxV= Gtk.Box (orientation = Gtk.Orientation.Vertical, spacing = 5)
        Panel.add (caixaAuxV)
        caixaAuxV.pack_start ()

        Panel = Gtk.Frame(label="Datos Económicos")
        caixaPrincipal.pack_start(Panel, True, True, 0)


        self.connect("destroy", Gtk.main_quit)
        self.show_all()




if __name__== "__main__":
    FiestraPrincipal()
    Gtk.main()
