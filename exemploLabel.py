import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo etiquetas")

        hbox = Gtk.Box(spacing=10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        label = Gtk.Label("Esta é unha etiqueta normal")
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label()
        label.set_text("Esta é unha etiqueta aliñada a esquerda.\nCon multiple liñas.")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label(
            "Esta é unha etiqueta aliñada a dereita.\nCon multiples liñas.")
  _Press      label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label("Este é un exemplo de etiqueta formateada. EstaThis is an example of a line-wrapped label.  It "
                          "pode non estar seguida should not be taking up the entire             "
                          "e ter espacios entre si, pero automáticamentewidth allocated to it, but automatically "
                          "formatea as palabras. wraps the words to fit.\n"
                          "     Soporta multiples espazos correctamente,It supports multiple paragraphs correctly, "
                          "e engade correctamente and  correctly   adds "
                          "moitas        liñas extra.many          extra  spaces. ")
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)

        label = Gtk.Label("Este é un exemplo de liña formateada, completa This is an example of a line-wrapped, filled label. "
                          "Esta pode usar "
                          "todo a anchura asignada            para elo.  "
                          "Ista é a frase para probar "
                          "a afirmación.  Aqui outra frase. "
                          "Iste texto está para cubrir oco, e alongar a etiqueta.\n"
                          "    Ito é un novo paragrafo.\n"
                          "    Un novo paragrafo, mais longo e"
                          "brillante.  Estamos chegando o final, "
                          "afortunadamente.")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        label = Gtk.Label()
        label.set_markup("Este texto é <small>pequeno</small>, <big>grande</big>, "
                         "<b>negriña</b>, <i>cursiva</i> e pódese consultar mais "
                         "opcións en <a href=\"http://www.gtk.org\" "
                         "title=\"Pulsa para encontrar mais en\">interrede</a>.")
        label.set_line_wrap(True)
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label.new_with_mnemonic(
            "_Presiona Alt + P o boton da dereita para seleccionar")
        vbox_left.pack_start(label, True, True, 0)
        label.set_selectable(True)

        button = Gtk.Button(label="Pulsa baixo a túa responsabilidade")
        label.set_mnemonic_widget(button)
        vbox_right.pack_start(button, True, True, 0)

        self.add(hbox)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()




if __name__== "__main__":
    FiestraPrincipal()
    Gtk.main()
