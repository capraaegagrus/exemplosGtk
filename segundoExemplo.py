import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Segundo exemplo")

        self.caixa = Gtk.Box(spacing=6, orientation=Gtk.Orientation.HORIZONTAL)
        self.add(self.caixa)

        self.lblEtiqueta = Gtk.Label(label="Escribe o teu nome")
        self.caixa.pack_start(self.lblEtiqueta, True, True, 10)

        self.txtNome = Gtk.Entry()
        self.caixa.pack_start(self.txtNome, True, True, 10)

        self.btnSaudo = Gtk.Button(label="Saudo")
        self.btnSaudo.connect("clicked", self.on_btnSaudo_clicked)
        self.caixa.pack_start(self.btnSaudo, True, True, 0)

        self.connect ("destroy", Gtk.main_quit)
        self.show_all()

    def on_btnSaudo_clicked(self, widget):
        self.lblEtiqueta.set_text("Ola " + self.txtNome.get_text())



fiestra = FiestraPrincipal()

Gtk.main()
