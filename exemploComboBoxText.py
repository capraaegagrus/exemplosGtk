import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.ComboBoxText")

        caixaV= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add (caixaV)

        nomes = ["Manuel", "Alejandro", "David", "Jose", "Alberto"]

        cmbNomes = Gtk.ComboBoxText()
        cmbNomes.set_entry_text_column(0)
        for nome in nomes:
            cmbNomes.append_text(nome)
        cmbNomes.connect ("changed",self.on_cmbNomes_changed)


        caixaV.pack_start (cmbNomes, False, False, 0)

        self.txtNomes = Gtk.Entry()
        caixaV.pack_start (self.txtNomes, True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()



    def on_cmbNomes_changed (self, combo):
        texto = combo.get_active_text()
        self.txtNomes.set_text(texto)




if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()