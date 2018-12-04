import gi
gi.require_version ('Gtk','3.0')
from gi.repository import Gtk

class FiestraPrincipal ():

    def __init__(self):

        builder = Gtk.Builder()
        builder.add_from_file ("fiestraSaudo.glade")

        fiestra = builder.get_object("FiestraPrincipal")
        self.txtEntry = builder.get_object ("txtEntry")
        self.btnBoton = builder.get_object ("btnSaudo")
        self.lblEtiqueta = builder.get_object ("lblEtiqueta")

        sinais = {
            "on_btnSaudo_clicked": self.on_btnSaudo_clicked,
            "on_txtEntry_activate": self.on_btnSaudo_clicked, #"on_txtEntry_activate": self.on_txtEntry_activate,
            "on_FiestraPrincipal_destroy": Gtk.main_quit
        }
        builder.connect_signals (sinais)

        fiestra.show_all()


    def on_btnSaudo_clicked (self, boton):
      nome = self.txtEntry.get_text()
      self.lblEtiqueta.set_text("Ola " + nome)


    def on_txtEntry_activate (self, cadroTexto):
      self.on_btnSaudo_clicked (cadroTexto)


if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()


