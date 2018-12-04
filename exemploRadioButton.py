import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.RadioButton")

        caixaPrincipal = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 8)
        self.add (caixaPrincipal)

        rbtOpcion1 = Gtk.RadioButton(None)
        rbtOpcion1.set_label ("Opción 1")
        rbtOpcion1.connect ("toggled", self.on_rbtOpcion1_toggled, 1)
        caixaPrincipal.pack_start (rbtOpcion1, False, False, 0)

        rbtOpcion2 = Gtk.RadioButton.new_with_label_from_widget (rbtOpcion1, "Opción 2")
        rbtOpcion2.connect("toggled", self.on_rbtOpcion1_toggled, 2)
        caixaPrincipal.pack_start(rbtOpcion2, False, False, 0)

        rbtOpcion3 = Gtk.RadioButton.new_from_widget(rbtOpcion1)
        rbtOpcion3.set_label ("Opción 3")
        rbtOpcion3.connect("toggled", self.on_rbtOpcion1_toggled, 3)
        caixaPrincipal.pack_start(rbtOpcion3, False, False, 0)

        rbtOpcion4 = Gtk.RadioButton.new_with_mnemonic_from_widget (rbtOpcion1, "O_pción 4")
        rbtOpcion4.connect("toggled", self.on_rbtOpcion1_toggled, 4)
        caixaPrincipal.pack_start(rbtOpcion4, False, False, 0)

        self.chkCondicion1 = Gtk.CheckButton ()
        self.chkCondicion1.set_label ("Condición 1")
        self.chkCondicion1.connect("toggled", self.on_checkCondicion_toggled, 1)
        caixaPrincipal.pack_start(self.chkCondicion1, False, False, 0)

        chkCondicion2 = Gtk.CheckButton.new_with_label ("Concición 2")
        chkCondicion2.connect("toggled", self.on_checkCondicion_toggled, 2)
        caixaPrincipal.pack_start(chkCondicion2, False, False, 0)

        chkCondicion3 = Gtk.CheckButton.new_with_mnemonic ("_Condición 3")
        chkCondicion3.connect("toggled", self.on_checkCondicion_toggled, 3)
        caixaPrincipal.pack_start(chkCondicion3, False, False, 0)

        caixaH = Gtk.Box (orientation = Gtk.Orientation.HORIZONTAL)
        caixaPrincipal.pack_start(caixaH, False, False, 0)

        self.tgbBoton1 = Gtk.ToggleButton("Boton 1")
        self.tgbBoton1.connect("toggled", self.on_tgbBoton_toggled, 1)
        caixaH.pack_start (self.tgbBoton1, False, False, 0)

        self.tgbBoton2 = Gtk.ToggleButton("B_oton 2")
        caixaH.pack_start(self.tgbBoton2, False, False, 0)

        self.tgbBoton3 = Gtk.ToggleButton("Boton _3")
        caixaH.pack_start(self.tgbBoton3, False, False, 0)




        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_checkCondicion_toggled (self, control, numero):
        if control.get_active():
            if numero == 1:
                self.tgbBoton1.set_active(True)
            if numero == 2:
                self.tgbBoton2.set_active(True)
            if numero == 3:
                self.tgbBoton3.set_active(True)
        else:
            if numero == 1:
                self.tgbBoton1.set_active(False)
            if numero == 2:
                self.tgbBoton2.set_active(False)
            if numero == 3:
                self.tgbBoton3.set_active(False)


    def on_tgbBoton_toggled (self, control, numero):
        if control.get_active():
            if numero == 1:
                self.chkCondicion1.set_active(True)
        else:
            if numero == 1:
                self.chkCondicion1.set_active(False)




    def on_rbtOpcion1_toggled (self, control, numero):
        if control.get_active():
            estado = "On"
        else:
            estado = "Off"
        print ("Opción ", numero, "estado ", estado)





if __name__== "__main__":
    FiestraPrincipal()
    Gtk.main()
