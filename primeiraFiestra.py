import gi
gi.require_version ('Gtk', '3.0')
from gi.repository import Gtk

fiestra = Gtk.Window()
fiestra.connect ("destroy",Gtk.main_quit)
fiestra.show_all()
Gtk.main()