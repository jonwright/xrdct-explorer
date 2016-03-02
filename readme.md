A really minimalist graphical interface to try look at xrdct files interactively (I have been in need of this for ages):

Upper window is the image with a cut at the two theta of the vertical line in the lower image.

In the image window:
    right mouse button= zoom,
    left mouse button = drag
    move the red box to the selected pixel for the powder pattern below

In the powder pattern window
    right mouse button= zoom,
    left mouse button = drag
    left click moves the line selection for drawing the image above

Can be used on sinogram or reconstructions, e.g.:

python xrdct-explorer.py mydata.hdf DiffTomo/NXdata/irecon

python xrdct-explorer.py mydata.hdf DiffTomo/NXdata/sinogram

Needs python27 with pyqtgraph

Please send pull request and I will apply them to try to improve it!
