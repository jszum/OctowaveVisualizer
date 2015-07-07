#!/usr/bin/env python

import pygst
pygst.require('0.10')
import gst
import gtk
import gobject
import sys
import os

name = ''

class Main:

    def __init__(self):
        self.pl = gst.element_factory_make("playbin2", "player")
        self.pl.set_property('uri', 'file://'+os.path.abspath(name))
        self.pl.set_state(gst.STATE_PLAYING)



if __name__ == '__main__':
    print(' '.join(sys.argv))
    name = sys.argv[1]
    mainloop = gobject.MainLoop()
    start = Main()
    mainloop.run()
    mainloop.quit()







