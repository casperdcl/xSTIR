import numpy
import pylab
import stir
import time

# if anything goes wrong, an exception will be thrown 
# (cf. Error Handling section in the spec)
try:
    # direct all diagnostic printing to a file
    printer = stir.printerTo('stir_demo.txt')

    # create matrix to be used by projectors
    matrix = stir.RayTracingMatrix()
    matrix.set_num_tangential_LORs(2)

    # create projectors
    projectors = stir.ProjectorsUsingMatrix()
    projectors.set_matrix(matrix)

    # create prior
    prior = stir.QuadraticPrior()
    prior.set_penalisation_factor(0.5)

    # create filter
    filter = stir.TruncateToCylindricalFOVImageProcessor()

    # create initial image estimate
    voxel_dim = (60, 60, 31)
    voxel_size = (4.44114, 4.44114, 3.375)
    image = stir.Image()
    image.initialise(voxel_dim, voxel_size)
    image.fill(1.0)
    filter.set_strictly_less_than_radius(False)
    filter.apply(image)

    # restore the default value
    filter.set_strictly_less_than_radius(True)

    # create objective function
    obj_fun =\
        stir.PoissonLogLikelihoodWithLinearModelForMeanAndProjData()
    obj_fun.set_input_filename('Utahscat600k_ca_seg4.hs')
    obj_fun.set_sensitivity_filename('RPTsens_seg3_PM.hv')
    obj_fun.set_use_subset_sensitivities(False)
    obj_fun.set_zero_seg0_end_planes(True)
    obj_fun.set_max_segment_num_to_process(3)
    obj_fun.set_projector_pair(projectors)
    obj_fun.set_prior(prior)
    obj_fun.set_up()

    num_subiterations = 6

    # create OSMAPOSL reconstructor
    recon = stir.OSMAPOSLReconstruction()
    recon.set_MAP_model('multiplicative')
    recon.set_num_subsets(12)
    recon.set_num_subiterations(num_subiterations)
    recon.set_save_interval(6)
    recon.set_inter_iteration_filter_interval(1)
    recon.set_inter_iteration_filter(filter)
    recon.set_output_filename_prefix('reconstructedImage')
    recon.set_objective_function(obj_fun)

    # set up the reconstructor
    recon.set_up(image)

    # in order to see the reconstructed image evolution
    # take over the control of the iterative process
    # rather than allow recon.reconstruct to do all job at once

    start_time = time.time()

    for iter in range(1, num_subiterations + 1):
        print('\n--------------------- Subiteration ',\
              recon.get_subiteration_num())
        # perform an iteration
        recon.update(image)
        # plot the current image
##        data = image.density()
##        pylab.figure(iter)
##        pylab.imshow(data[10,:,:])

    elapsed_time = time.time() - start_time
    print('elapsed time:', elapsed_time)

##    pylab.show()

    # compare the reconstructed image to the expected image
    expectedImage = stir.Image('test_image_PM_QP_6.hv')
    diff = expectedImage.diff_from(image)
    print('difference from expected image:', diff)

    # let the user inspect any z-crossections of the image they want to
    data = image.density()
    nz = data.shape[0]
    while True:
        s = str(input('enter z-coordinate: '))
        if len(s) < 1:
            break
        z = int(s)
        if z < 0 or z >= nz:
            break
        pylab.figure(z)
        pylab.imshow(data[z,:,:])
        pylab.show()

except stir.error as err:
    # display error information
    print('STIR exception occured:\n', err.value)