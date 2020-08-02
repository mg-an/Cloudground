import pygtk
pygtk.require('2.0')
import gtk
import browse
import os

class HelloWorld:

    def hello(self, widget, data=None):
        execfile('inp.py')

    def back(self, widget, date = None):
        execfile('recieve.py')

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
    
        # Sets the border width of the window.
        self.window.set_border_width(100)
    
        # Creates a new button with the label "Hello World".
        self.button = gtk.Button("SEND")
        self.button.connect("clicked", self.hello)

        self.b = gtk.Button("RECD")
        self.b.connect("clicked", self.back)

        fixed = gtk.Fixed()
        fixed.put(self.button, 50, 50)
        fixed.put(self.b, 50, 80)
        
        #self.b.connect("clicked", self.hello, None)
    
        # This packs the button into the window (a GTK container).
        #self.window.add(self.button)
        #self.window.add(self.b)
    
        # The final step is to display this newly created widget.
        #self.button.show()
        #self.b.show()
    
        # and the window
        self.window.add(fixed)
        self.window.show_all()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()

