# -*- coding: utf-8 -*-
"""
Heavily based on the pyqtgraph example data slicer

- reads a 3D array from a hdf file [nx,ny,nz]

- displays a slice [:,:,roi3] at the top

- displays the line [roi1,roi2,:] at the bottom

roi1/2, to choose the 1D plot, is selected using the box on the upper image
roi3 is chosen from the lower plot

Jon Wright, 2 March 2016
"""

## Add path to library (just for examples; you do not need this)
import sys
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg

import h5py
h = h5py.File( sys.argv[1] )
name = sys.argv[2]
s = h[name]

roi0=s.shape[0]/2
roi1=s.shape[1]/2
roi2=s.shape[2]/2


app = QtGui.QApplication([])

## Create window with two ImageView widgets
win = QtGui.QMainWindow()
win.resize(1200,1000)
win.setWindowTitle('pyqtgraph example: xrdct explorer')
cw = QtGui.QWidget(parent=win)
win.setCentralWidget(cw)
l = QtGui.QGridLayout()
cw.setLayout(l)
imv1 = pg.ImageView()
imv2 = pg.plot()
l.addWidget(imv1, 0, 0)
l.addWidget(imv2, 1, 0)
win.show()


roi = pg.ROI([roi0,roi1], size=(1,1), pen='r')
imv1.addItem(roi)

plroi = pg.InfiniteLine(angle=90, movable=False)
imv2.addItem( plroi, ignoreBounds=True )
plroi.setPos(roi2)

curve = imv2.plot()



def updateimg():
    global data, imv1, imv2
    p =roi.pos()
    i , j =  np.round((p[0])),np.round(int(p[1]))
    curve.setData(s[int(i),int(j)])
    


def mouseClicked(evt):
    pos = evt[0]._scenePos  ## using signal proxy turns original arguments into a tuple
    if imv2.sceneBoundingRect().contains(pos):
        mousePoint = imv2.plotItem.vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        if index>0 and index<s.shape[2]:
            plroi.setPos(mousePoint.x())
            imv1.setImage(s[:,:,index])


imv1.setImage(s[:,:,roi2])

roi.sigRegionChanged.connect(updateimg)

proxy = pg.SignalProxy(imv2.scene().sigMouseClicked,
        rateLimit=60, slot=mouseClicked)

updateimg()


## Display the data

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
