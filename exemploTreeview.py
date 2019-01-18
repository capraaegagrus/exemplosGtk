import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.TreeView")
        boxV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL)

        modelo = Gtk.ListStore (str, str, float,bool,str )
        self.filtro_categoria = modelo.filter_new()
        self.filtro_categoria.set_visible_func (self.categoria_filtro)
        self.parametro_filtro_categoria = None


        modelo.append  (["Hotel Melia", "García Barbón 48", 75.38, True, '*'])
        modelo.append  (["Hotel Galeones", "Avda Madrid", 80.88, False, '**'])
        modelo.append  (["Hotel Baiha", "Paseo as avenidas 55", 60.38, True,'*****'])

        self.categoria = Gtk.ListStore (str)
        for estrelas in range (1,6):
            self.categoria.append([estrelas*'*'])


        vista = Gtk.TreeView(model = self.filtro_categoria)#modelo filtrado
        seleccion = vista.get_selection()
        seleccion.connect("changed", self.on_seleccion_changed)
        boxV.pack_start (vista, True, True, 0)

        celdaText = Gtk.CellRendererText()
        celdaText.set_property ("editable", True)
        celdaText.connect ("edited", self.on_celdaText_edited, modelo)
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

        boxHFiltro = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.cmbCategoriaF = Gtk.ComboBox(model=self.categoria)
        celdaComboF = Gtk.CellRendererText()
        self.cmbCategoriaF.pack_start(celdaComboF, True)
        self.cmbCategoriaF.add_attribute(celdaComboF, "text", 0)


        btnFiltrar = Gtk.Button (label="Filtrar")
        btnFiltrar.connect ("clicked", self.on_btnFiltrar_clicked)

        boxHFiltro.pack_end (btnFiltrar, False, False, 0)
        boxHFiltro.pack_end(self.cmbCategoriaF, False, False, 0)
        boxV.pack_start (boxHFiltro, True, True, 0)

        self.add(boxV)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_combo_edited (self, control, fila, texto, modelo ):
        modelo [fila][4] = texto

    def on_btnEngadir_clicked (self, control, modelo):
        fila = self.cmbCategoria.get_active_iter()
        datos = [self.txtHotel.get_text(), self.txtDireccion.get_text(),self.txtOcupacion.get_text(),self.chkMascotas.get_mode(), self.cmbCategoria.get_model()[fila][0]]
        modelo.append (datos) #Engadir o recollido dos controis

    def on_seleccion_changed (self, seleccion):
        modelo, punteiro = seleccion.get_selected()
        if punteiro is not None:
            self.txtHotel.set_text(modelo [punteiro][0])
            self.txtDireccion.set_text (modelo [punteiro][1])
            self.txtOcupacion.set_text (str (modelo [punteiro][2]))
            self.chkMascotas.set_active(modelo [punteiro][3])
            categorias = self.cmbCategoria.get_model()
            #Non funcionaaaaa, REVISAR
            i=0
            for categoria in categorias:

                if modelo [punteiro][4] == categoria[0] :
                    self.cmbCategoria.set_active (i)
                i = i + 1

    def on_celdaText_edited (self, control, punteiro, texto, modelo):
        modelo [punteiro][0] = texto

    def on_btnFiltrar_clicked (self, control):
        punteiro = self.cmbCategoriaF.get_active_iter()
        print ("Filtrando os hoteis da categoria: ", self.cmbCategoriaF.get_model()[punteiro][0])
        self.parametro_filtro_categoria = self.cmbCategoriaF.get_model()[punteiro][0]
        self.filtro_categoria.refilter()


    def categoria_filtro(self, modelo,  punteiro, datos):

        if self.parametro_filtro_categoria is None:
            return True
        else:
            if modelo[punteiro][4]==self.parametro_filtro_categoria:
                return True
            else:
                return False







if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()