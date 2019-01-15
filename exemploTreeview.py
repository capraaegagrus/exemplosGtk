import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.TreeView")
        boxV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL)

        modelo = Gtk.ListStore (str, str, float,bool,str )

        modelo.append  (["Hotel Melia", "García Barbón 48", 75.38, True, '*'])
        modelo.append  (["Hotel Galeones", "Avda Madrid", 80.88, False, '**'])
        modelo.append  (["Hotel Baiha", "Paseo as avenidas 55", 60.38, True,'*****'])

        self.categoria = Gtk.ListStore (str)
        for estrelas in range (1,4):
            self.categoria.append([estrelas*'*'])


        vista = Gtk.TreeView(model = modelo)
        boxV.pack_start (vista, True, True, 0)

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
        celdaCategoria.set_property ("has-entry", False)
        celdaCategoria.connect("edited", self.on_combo_edited, modelo)
        columnaCategoria = Gtk.TreeViewColumn ('Categoria', celdaCategoria, text =4)
        vista.append_column (columnaCategoria)

        boxH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.txtHotel = Gtk.Entry ()
        self.txtDireccion = Gtk.Entry ()
        self.chkMascotas = Gtk.CheckButton ()
        self.txtOcupacion = Gtk.Entry ()
        self.cmbCategoria = Gtk.ComboBox ( model = self.categoria)
        celdaCombo = Gtk.CellRendererText()
        self.cmbCategoria.pack_start (celdaCombo, True)
        self.cmbCategoria.add_attribute (celdaCombo, "text",0)

        #Indicarlle que columna queremos mostrar
        boxH.pack_start(self.txtHotel, True, True, 0)
        boxH.pack_start(self.txtDireccion, True, True, 0)
        boxH.pack_start(self.chkMascotas, True, True, 0)
        boxH.pack_start(self.txtOcupacion, True, True, 0)
        boxH.pack_start(self.cmbCategoria, True, True, 0)
        btnEngadir = Gtk.Button (label = "Engadir")
        btnEngadir.connect ("clicked", self.on_btnEngadir_clicked, modelo)
        boxH.pack_start(btnEngadir, True, True, 0)

        boxV.pack_start(boxH, True, True, 0)

        self.add(boxV)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_combo_edited (self, control, fila, texto, modelo ):
        modelo [fila][4] = texto

    def on_btnEngadir_clicked (self, control, modelo):
        fila = self.cmbCategoria.get_active_iter()
        datos = [self.txtHotel.get_text(), self.txtDireccion.get_text(),self.txtOcupacion.get_text(),self.chkMascotas.get_mode(), self.cmbCategoria.get_model()[fila][0]]
        modelo.append (datos) #Engadir o recollido dos controis




if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()