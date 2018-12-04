import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ListBoxRowConDatos(Gtk.ListBoxRow):
    def __init__(self, dato):
        super(Gtk.ListBoxRow, self).__init__()
        self.dato = dato
        self.add(Gtk.Label(dato))


class FiestraPrincipal(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.ListBox")

        caixaExterna = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 8)
        self.add (caixaExterna)

        listBox = Gtk.ListBox()
        listBox.set_selection_mode (Gtk.SelectionMode.NONE)
        caixaExterna.pack_start(listBox, True, True, 0)

        fila = Gtk.ListBoxRow()
        caixah = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 50)
        fila.add(caixah)
        caixav = Gtk.Box (orientation = Gtk.Orientation.VERTICAL)
        caixah.pack_start (caixav, True, True, 0)

        etiqueta1 = Gtk.Label ("Hora e data automática", xalign=0)
        etiqueta2 = Gtk.Label ("Require acceso a interrede" , xalign=0)
        caixav.pack_start (etiqueta1, True, True, 0)
        caixav.pack_start(etiqueta2, True, True, 0)

        interruptor = Gtk.Switch()
        interruptor.props.valign = Gtk.Align.CENTER
        caixah.pack_start(interruptor, False, True, 0)

        listBox.add(fila)


        fila = Gtk.ListBoxRow()
        caixah = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(caixah)
        etiqueta = Gtk.Label("Formato de data", xalign=0)
        combo = Gtk.ComboBoxText()
        combo.insert (0, '0', "24-horas")
        combo.insert(1, '1', "AM-PM")
        caixah.pack_start (etiqueta, True, True, 0)
        caixah.pack_start(combo, False, True, 0)

        listBox.add(fila)

        fila = Gtk.ListBoxRow()
        caixah = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(caixah)
        etiqueta = Gtk.Label("Escribe a palabra a engadir no listBox de embaixo", xalign=0)
        self.txtPalabra = Gtk.Entry ()
        self.txtPalabra.connect ("activate", on_txtPalabra_activated)
        caixah.pack_start (etiqueta, True, True, 0)
        caixah.pack_start (self.txtPalabra, True, True, 0)







        listBox2 = Gtk.ListBox ()
        elementos = "Esta é unha listBox para ordear".split()

        for elemento in elementos:

            listBox2.add (ListBoxRowConDatos(elemento))

        def funcion_ordenacion (fila1, fila2, variable, notify_destroy ):
            return fila1.dato.lower() > fila2.dato.lower()

        def funcion_filtro (fila, variable, notify_destroy):
            return False if fila.dato == variable else True

        listBox2.set_sort_func( funcion_ordenacion, None, False)
        listBox2.set_filter_func ( funcion_filtro, "listBox", False)

        def on_fila_activated (listBox_control, fila):
            print (fila.dato)

        listBox2.connect ("row-activated", on_fila_activated)
        caixaExterna.pack_start(listBox2, True, True, 0)



        self.connect ("destroy", Gtk.main_quit)
        self.show_all()


     def on_txtPalabra_activated (control):
         """"""






if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()