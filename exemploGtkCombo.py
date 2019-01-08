import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.Combo")

        caixaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL)

        modelo = Gtk.ListStore (str, str)
        modelo.append (["36111111j", "Alba Torre"])
        modelo.append(["3611222j", "Alberto Torres"])
        modelo.append(["36111333j", "Toño Abril"])

        cmbPersoa = Gtk.ComboBox.new_with_model_and_entry (modelo)
        cmbPersoa.connect ("changed", self.on_cmbPersoa_changed)
        cmbPersoa.set_entry_text_column (1)
        caixaV.pack_start (cmbPersoa, False, False,0)
        txtCadroNome = cmbPersoa.get_child()
        txtCadroNome.connect ("activate", self.on_txtCadroNome_activate, modelo)

        self.add (caixaV)


        self.connect ("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmbPersoa_changed(self, combo):
        punteiro = combo.get_active_iter()
        modelo = combo.get_model()
        if punteiro is not None:
            dni, nome = modelo[punteiro][:2]
            print ("Foi seleccionado: "+ nome + " con dni " + dni)
      
    def on_txtCadroNome_activate(self, control, modelo):
        cadea = control.get_text()
        palabras = cadea.split (',')
        modelo.append (palabras )





if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()