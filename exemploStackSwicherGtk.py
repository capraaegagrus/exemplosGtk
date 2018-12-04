import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.StackSwitcher")

        caixa = Gtk.Box (orientation= Gtk.Orientation.VERTICAL, spacing = 6)
        self.add (caixa)

        stack = Gtk.Stack ()
        stack.set_transition_type (Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        cadroChequeo = Gtk.CheckButton ("Seleccioname!")
        stack.add_titled (cadroChequeo, "check", "Botón chequeo")

        box= Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=6)
        etiqueta = Gtk.Label ()
        etiqueta.set_markup ("<big>Unha etiqueta distinta</big>")
        boton = Gtk.Button (label = "Pulsame")
        box.pack_start (etiqueta, True, True,0)
        box.pack_start (boton, True, False,0)


        stack.add_titled (box, "Panel", "Etiqueta e botón")

        selector_stack = Gtk.StackSwitcher()
        selector_stack.set_stack(stack)

        caixa.pack_start (selector_stack, True, True, 0)
        caixa.pack_start (stack, True, True, 0)



        self.connect ("destroy", Gtk.main_quit)
        self.show_all()




if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()