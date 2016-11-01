import argparse
import numpy
import pylab
import os
import sys
sys.path.append(os.environ.get('CSTIR_SRC') + '/../pSTIR')
import time

from pStir import *

parser = argparse.ArgumentParser(description = \
'''
OSMAPOSL reconstruction demo with all parameters defined in the script
and user-controlled iterations
''')
args = parser.parse_args()

def main():

    # direct all information and error printing to files
    info_printer = printerTo('info.txt', INFO_CHANNEL)
    warning_printer = printerTo('warn.txt', WARNING_CHANNEL)
    # direct all error printing to stdout
    error_printer = printerTo('stdout', ERROR_CHANNEL)

    # create matrix to be used by the acquisition model
    matrix = RayTracingMatrix()
    matrix.set_num_tangential_LORs(2)

    # create acquisition model
    am = AcquisitionModelUsingMatrix()
    am.set_matrix(matrix)

    # define acquisition data
    ad = AcquisitionData('my_forward_projection.hs')

    # create filter
    filter = CylindricFilter()

    # create initial image estimate
    image_size = (111, 111, 31)
    voxel_size = (3, 3, 3.375)
    image = Image()
    image.initialise(image_size, voxel_size)
    image.fill(1.0)

    # create objective function
    obj_fun = PoissonLogLh_LinModMean_AcqMod()
    obj_fun.set_acquisition_model(am)
    obj_fun.set_acquisition_data(ad)
    obj_fun.set_num_subsets(12)
    obj_fun.set_up(image)

    num_subiterations = 2

##    ss = obj_fun.get_subset_sensitivity(0)
##    data = ss.as_array()
##    pylab.figure(1)
##    pylab.imshow(data[20,:,:])
##    print('Figure 1: subset 0 sensitivity - close window to continue')
##    pylab.show()
##
##    grad = obj_fun.get_gradient_not_divided(image, 0)
##    data = grad.as_array()
##    pylab.figure(1)
##    pylab.imshow(data[20,:,:])
##    print('Figure 2: subset 0 gradient - close window to continue')
##    pylab.show()

    eps = 1e-6

    for iter in range(1, num_subiterations + 1):
        print('\n------------- Subiteration %d' % iter) 

        # select subset
        subset = iter - 1

        # get sensitivity as Image
        ss = obj_fun.get_subset_sensitivity(subset)

        # get gradient not divided by sensitivity (+prior) as Image
        grad = obj_fun.get_gradient_not_divided(image, subset)

        # copy to Python arrays
        data = image.as_array()
        sdata = ss.as_array()
        sdata[sdata < eps] = eps # avoid division by zero
        gdata = grad.as_array()

        # update image data
        data = data*gdata/sdata

        # fill current image with new values
        image.fill(data)

        # apply filter
        filter.apply(image)

        # show current image
        data = image.as_array()
        pylab.figure(iter + 1)
        pylab.imshow(data[20,:,:])
        print('close Figure %d window to continue' % (iter + 1))
        pylab.show()

# if anything goes wrong, an exception will be thrown 
# (cf. Error Handling section in the spec)
try:
    main()
except error as err:
    # display error information
    print('STIR exception occured: %s' % err.value)
