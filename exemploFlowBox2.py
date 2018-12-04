import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class NovoGrid (Gtk.Grid):

    def __init__(self):
        Gtk.Grid.__init__(self)


        boton1 = Gtk.Button(label = "Boton1")
        boton2 = Gtk.Button(label = "Boton2")
        boton3 = Gtk.Button(label = "Boton3")
        boton4 = Gtk.Button(label = "Boton4")
        boton5 = Gtk.Button(label = "Boton5")
        boton6 = Gtk.Button(label = "Boton6")

        self.attach (boton1, 0, 0, 1,1)
        self.attach (boton2, 1, 0, 2, 1) # control, columna, fila , ancho, alto
        self.attach_next_to (boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to (boton4, boton3, Gtk.PositionType.RIGHT, 2, 1)
        #grid.attach_next_to (boton4, boton2, Gtk.PositionType.BOTTOM, 2, 1)
        self.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach (boton6, 2, 2, 1, 1)




class FiestraPrincipal(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.FlowBox")
        self.set_default_size(300, 250)

        cabeceira = Gtk.HeaderBar(title = "FlowBox exemplo")
        cabeceira.set_subtitle ("Aplicación con HeaderBar")
        cabeceira.props.show_close_button = True

        self.set_titlebar (cabeceira)

        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        flowBox = Gtk.FlowBox ()
        flowBox.set_valign(Gtk.Align.START)
        flowBox.set_max_children_per_line (30)
        flowBox.set_selection_mode (Gtk.SelectionMode.NONE)

        self.creaFlowBox(flowBox)
        scroll.add(flowBox)

        self.add(scroll)

        self.connect ("destroy", Gtk.main_quit)
        self.show_all()

    def creaFlowBox(self, flowBox):

        for n in range (20):
            grid = NovoGrid ()
            flowBox.add(grid)









if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()