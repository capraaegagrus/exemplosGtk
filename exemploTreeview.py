import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.TreeView")

        modelo = Gtk.ListStore (str, str, float,bool,str )

        modelo.append  (["Hotel Melia", "García Barbón 48", 75.38, True, '*'])
        modelo.append  (["Hotel Galeones", "Avda Madrid", 80.88, False, '**'])
        modelo.append  (["Hotel Baiha", "Paseo as avenidas 55", 60.38, True,'*****'])

        self.categoria = Gtk.ListStore (str)
        for estrelas in range (1,4):
            self.categoria.append([estrelas*'*'])


        vista = Gtk.TreeView(model = modelo)

        celdaText = Gtk.CellRendererText()
        columnaHotel = Gtk.TreeViewColumn ('Aloxamento', celdaText, text = 0)
        columnaHotel.set_sort_column_id (0)
        vista.append_column (columnaHotel)

        celdaText2 = Gtk.CellRendererText (xalign = 1)
        columnaDir = Gtk.TreeViewColumn ('Dirección', celdaText2, text = 1)
        vista.append_column (columnaDir)

        celdaNum = Gtk.CellRendererProgress()
        columnaOcupacion = Gtk.TreeViewColumn ('Ocupación', celdaNum, value = 2)
        columnaOcupacion.set_sort_column_id (2)
        vista.append_column (columnaOcupacion)

        celdaMascotas = Gtk.CellRendererToggle()
        columnaMascotas = Gtk.TreeViewColumn ('Mascotas', celdaMascotas, active = 3)
        vista.append_column (columnaMascotas)

        celdaCategoria = Gtk.CellRendererCombo()
        celdaCategoria.set_property ("editable", True)
        celdaCategoria.set_property ("model", self.categoria)
        celdaCategoria.set_property ("text-column",0)
        celdaCategoria.connect("edited", self.on_combo_edited)
        columnaCategoria = Gtk.TreeViewColumn ('Categoria', celdaCategoria, text =4)
        vista.append_column (columnaCategoria)

        self.add(vista)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_combo_edited (self, control, fila, texto ):
        self.categoria [fila][0] = texto



if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()