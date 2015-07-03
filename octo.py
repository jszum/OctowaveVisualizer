#!/usr/bin/env python

import pygst
pygst.require('0.10')
import gst
import gtk
import sys


def main():

    print 'GStreamer visualiser'
    pipeline = gst.Pipeline("pipeline")


if __name__ == '__main__':
    print( ' '.join(sys.argv) )
    main()







