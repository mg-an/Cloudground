#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import subprocess
import browse
import ftp_client
import os

def xpm_label_box(parent, xpm_filename, label_text):
    # Create box for xpm and label
    box1 = gtk.HBox(False, 0)
    box1.set_border_width(2)

    # Now on to the image stuff
    image = gtk.Image()
    image.set_from_file(xpm_filename)

    # Create a label for the button
    label = gtk.Label(label_text)

    # Pack the pixmap and label into the box
    box1.pack_start(image, False, False, 3)
    box1.pack_start(label, False, False, 3)

    image.show()
    label.show()
    return box1

"""class Buttons:
    # Our usual callback method
    def callback(self, widget, data=None):
        print "Hello again - %s was pressed" % data"""

"""    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("Image'd Buttons!")

        # It's a good idea to do this for all windows.
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2:gtk.main_quit())

        # Sets the border width of the window.
        self.window.set_border_width(10)

        # Create a new button
        button = gtk.Button()

        # Connect the "clicked" signal of the button to our callback
        button.connect("clicked", self.callback, "cool button")

        # This calls our box creating function
        box1 = xpm_label_box(self.window, "info.xpm", "cool button")

        # Pack and show all our widgets
        button.add(box1)

        box1.show()
        button.show()

        self.window.add(button)
        self.window.show()"""


class EntryExample:
#    def enter_callback(self, widget, entry):
#        IP = entry.get_text()
#        print "Server Address is: %s\n" % IP


#    def enter_callback2(self, widget, entry2):
#        file_name = entry2.get_text()
#        print "Filename is: %s\n" % file_name

    def callback(self, widget, data=None):
	print "Browse button is clicked"
    
    def sample(self, widget, data = None):
        #execfile('ftp_client.py')
        #os.system('python /home/hasan/Downloads/RDpy/client.py')
        os.system('python ftp_client.py')

    def entry_toggle_editable(self, checkbutton, entry):
        entry.set_editable(checkbutton.active)

    def entry_toggle_visibility(self, checkbutton, entry):
        entry.set_visibility(checkbutton.active)

    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_usize(300, 300)
        window.set_title("CloudGround")
        window.connect("delete_event", gtk.mainquit)

        vbox = gtk.VBox(gtk.FALSE, 0)
        window.add(vbox)
        vbox.show()

        entry = gtk.Entry(50)
#        entry.connect("activate", self.enter_callback, entry)
#        entry.set_text("hello")
#        entry.append_text(" world")
#        entry.select_region(0, len(entry.get_text()))
#        vbox.pack_start(entry, gtk.TRUE, gtk.TRUE, 0)
#        entry.show()

#	entry2 = gtk.Entry(50)
#        entry2.connect("activate", self.enter_callback2, entry2)
#        entry.set_text("hello")
#        entry.append_text(" world")
#        entry2.select_region(0, len(entry2.get_text()))
#        vbox.pack_start(entry2, gtk.TRUE, gtk.TRUE, 0)
#        entry2.show()


        hbox = gtk.HBox(gtk.FALSE, 0)
        vbox.add(hbox)
        hbox.show()
                                  
#        check = gtk.CheckButton("Connect")
#        hbox.pack_start(check, gtk.TRUE, gtk.TRUE, 0)
#        check.connect("toggled", self.entry_toggle_editable, entry)
#        check.set_active(gtk.TRUE)
#        check.show()
    
#        check = gtk.CheckButton("Visible")
#        hbox.pack_start(check, gtk.TRUE, gtk.TRUE, 0)
#        check.connect("toggled", self.entry_toggle_visibility, entry)
#        check.set_active(gtk.TRUE)
#        check.show()
                                   
        button = gtk.Button("Browse")
        button.connect("clicked", self.browse)
#	button.connect_object("clicked", browse.py, window)
	button2 = gtk.Button("Live Window")
	button3 = gtk.Button("File Status")
        button3.connect("clicked", self.sample)

        vbox.pack_start(button, gtk.TRUE, gtk.TRUE, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()

	vbox.pack_start(button2, gtk.TRUE, gtk.TRUE, 0)
        button2.set_flags(gtk.CAN_DEFAULT)
        button2.grab_default()

        vbox.pack_start(button3, gtk.TRUE, gtk.TRUE, 0)
        button3.set_flags(gtk.CAN_DEFAULT)
        button3.grab_default()

	button.show()
	button2.show()
	button3.show()

        window.show()
    def browse(self, button):
	browse.browse()
    #def ftp_client(self, button):
        #client = ftp_client.FtpClient()
        #client.show()
        
def main():
    gtk.mainloop()
    return 0

if __name__ == "__main__":
    EntryExample()
#    Buttons()
    main()
