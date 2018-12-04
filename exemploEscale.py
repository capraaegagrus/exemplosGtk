import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.Scale")

        self.set_default_size (400,400)

        #val inicial, valor min , valor max , incremento de paso, incremento páxina, tamaño páxina

        ax1 = Gtk.Adjustment(0,0,100, 5, 10, 0)
        ax2 = Gtk.Adjustment (50, 0, 100, 5, 10, 0)

        sclHorizontal = Gtk.Scale (orientation = Gtk.Orientation.HORIZONTAL, adjustment = ax1)
        sclHorizontal.set_digits (0)
        sclHorizontal.set_hexpand(True)
        sclHorizontal.set_valign (Gtk.Align.START)
        sclHorizontal.connect ("value-changed", self.on_scale_value_changed, "h")




        grid = Gtk.Grid ()
        grid.set_column_spacing (10)
        grid.set_column_homogeneous (True)
        grid.add (sclHorizontal)



        sclVertical = Gtk.Scale (orientation = Gtk.Orientation.VERTICAL, adjustment = ax2)
        sclVertical.set_vexpand(True)
        sclVertical.connect("value-changed", self.on_scale_value_changed, "v")
        grid.attach_next_to (sclVertical, sclHorizontal, Gtk.PositionType.RIGHT,1,1)

        self.txtTexto = Gtk.Entry()
        grid.attach(self.txtTexto, 0, 1, 2, 1)

        self.add(grid)

        self.connect ("destroy", Gtk.main_quit)
        self.show_all()



    def on_scale_value_changed (self, control, tipo):
        if tipo =="v":
            self.txtTexto.set_text("A escala vertical é: " + str(control.get_value()))
        elif tipo =="h":
            self.txtTexto.set_text ("A escala horizontal é: "+ str ( control.get_value()))


if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()


