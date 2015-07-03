#!/usr/bin/env python

import pygst
pygst.require('0.10')
import gst
import gtk
import sys

name = ''

class Main:

    def __init__(self):

        self.pipeline = gst.Pipeline("pipeline")

        self.audiotestsrc = gst.element_factory_make("audiotestsrc", "audio")
        self.pipeline.add(self.audiotestsrc)

        self.sink = gst.element_factory_make("alsasink", "sink")
        self.pipeline.add(self.sink)

        self.audiotestsrc.link(self.sink)
        self.pipeline.set_state(gst.STATE_PLAYING)




if __name__ == '__main__':
    print( ' '.join(sys.argv) )
    name = sys.argv[1]
    start = Main()
    gtk.main()







