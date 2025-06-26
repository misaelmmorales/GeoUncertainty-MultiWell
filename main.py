import os, time
from tqdm import tqdm
import numpy as np
from scipy import ndimage
from librosa.sequence import dtw
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

cmap, interp = 'binary', 'bicubic'

######### 3D Visualization #########
# p = pv.Plotter()
# mesh = pv.wrap(np.flip(d))
# m1 = mesh.slice_orthogonal()
# p.add_mesh(m1, cmap=cmap)
# p.show(jupyter_backend='static')
####################################

####################################
######### Load facies data #########
facies = np.load('data/facies.npy')
nrealizations, nx, ny, nz = facies.shape
print('Facies: {}'.format(facies.shape))
####################################
####################################

#############################################
######### Facies sample and filter ##########
sample = 214
d = ndimage.gaussian_filter(facies[sample], sigma=0.33) #facies[sample]
print('Sample: {}'.format(sample))
#############################################
#############################################

########################################################################
############################## Well Logs ###############################
nwells = 5
wscale = 3
extent = (15, 255-16)

# Wells (x,y) coordinates
depth = np.arange(d.shape[-1]) + 1000
wx, wy = np.random.randint(extent[0], extent[1], size=(2,nwells))
print('Wells (x,y): ({}, {})'.format(wx, wy))

# Well logs (clean, noisy)
well_log = d[wy, wx, :]
noise_log = d[wy, wx, :] + np.random.normal(0, 0.2*d.std(), d.shape[-1])
########################################################################
########################################################################

########################################################################
################################# DTW ##################################
w1, w2 = well_log[0], well_log[1]
D, wp = dtw(w1, w2)
print('D: {} | wp: {}'.format(D.shape, wp.shape))
########################################################################
########################################################################