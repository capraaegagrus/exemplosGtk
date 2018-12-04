import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.Notebook")

        notebook = Gtk.Notebook()
        self.add (notebook)

        paxina1 = Gtk.Box ()
        paxina1.set_border_width (8)
        caixa = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing =3)

        caixa.pack_start (Gtk.Label ("Páxina por defecto"), True, True,0)
        caixa.pack_start (Gtk.Button (label="Pulsalme"), True, False, 0)
        paxina1.add(caixa)
        notebook.append_page (paxina1, Gtk.Label ("Título"))

        paxina2 = Gtk.Box ()
        paxina2.set_border_width(8)
        paxina2.add (Gtk.Label ("Páxina con unha imaxe como título"))
        notebook.append_page(paxina2,
                             Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))







        self.connect ("destroy", Gtk.main_quit)
        self.show_all()




if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()