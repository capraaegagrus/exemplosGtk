import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

libros = [["Tolstoy, Leo", ["Gerra e paz", True], ["Anna Karemina", False]],
         ["Shakespeare, Wiliam", ["Hamlet", True], ["Macbeth", True], ["Othello", False]],
          ["Tolkien, J.R.R", ["El señor de los anillos", False], ["El Hobbit", True]]]


class FiestraPrincipal(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Exemplo Gtk.TreeView con TreeStore")

        self.arbol = Gtk.TreeStore (str , bool)
        for i in range(len (libros)):
            punteiro = self.arbol.append (None, [libros[i][0], False])
            j = 1
            while j< len (libros [i]):
                self.arbol.append (punteiro, libros[i][j])
                j += 1

        vista = Gtk.TreeView ()
        vista.set_model(self.arbol)

        celdaLibros = Gtk.CellRendererText()
        columnaLibros = Gtk.TreeViewColumn ('Libros', celdaLibros, text=0)
        vista.append_column( columnaLibros)

        celdaPrestado = Gtk.CellRendererToggle()
        columnaPrestado = Gtk.TreeViewColumn ('Prestado', celdaPrestado, active=1)
        vista.append_column (columnaPrestado)
        celdaPrestado.connect ("toggled", self.on_celdaPrestadoToggled)

        self.add (vista)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_celdaPrestadoToggled(self, control, indice):
        """"""
        valor_actual = self.arbol [indice][1]
        self.arbol [indice][1]= not valor_actual
        valor_actual = not valor_actual
        if len (indice)==1:
            punteiroPai = self.arbol.get_iter(indice)
            punteiroFillo = self.arbol.iter_children(punteiroPai)

            while punteiroFillo is not None:
               self.arbol [punteiroFillo][1] =valor_actual
               punteiroFillo = self.arbol.iter_next(punteiroFillo)
        elif len (indice)!= 1:
            punteiroFillo = self.arbol.get_iter (indice)
            punteiroPai = self.arbol.iter_parent (punteiroFillo)
            punteiroFillo = self.arbol.iter_children (punteiroPai)
            todos_seleccionados = True
            while punteiroFillo is not None:
                if self.arbol [punteiroFillo][1]== False:
                    todos_seleccionados = False
                    break
                punteiroFillo = self.arbol.iter_next (punteiroFillo)
            self.arbol [punteiroPai][1]= todos_seleccionados

                                                                                                                                                    

if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()