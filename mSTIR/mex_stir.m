clear all

if libisloaded('mutilities')
    unloadlibrary('mutilities')
end
if libisloaded('mstir')
    unloadlibrary('mstir')
end

util_path = getenv('IUTILITIES');
util_lib = getenv('IUTILITIES_LIBRARY');
util_ipath = ['-I' util_path];

cstir_path = getenv('CSTIR_SRC');
cstir_lib = [cstir_path '\x64\Release\cSTIR.lib'];

boost_path = getenv('BOOST');
boost_ipath = ['-I' boost_path];

stir_src = [getenv('STIR_INCLUDE') '\..\'];
stir_ipath = ['-I' getenv('STIR_INCLUDE')];

stir_libpath = [getenv('STIR_BUILD') '\'];
stir_lib1 = [stir_libpath 'buildblock\Release\buildblock.lib'];
stir_lib2 = [stir_libpath 'data_buildblock\Release\data_buildblock.lib'];
stir_lib3 = [stir_libpath 'display\Release\display.lib'];
stir_lib4 = [stir_libpath 'eval_buildblock\Release\eval_buildblock.lib'];
stir_lib5 = [stir_libpath 'IO\Release\IO.lib'];
stir_lib6 =...
    [stir_libpath 'iterative\OSMAPOSL\Release\iterative_OSMAPOSL.lib'];
stir_lib7 = [stir_libpath 'iterative\OSSPS\Release\iterative_OSSPS.lib'];
stir_lib8 =...
    [stir_libpath 'listmode_buildblock\Release\listmode_buildblock.lib'];
stir_lib9 =...
    [stir_libpath 'modelling_buildblock\Release\modelling_buildblock.lib'];
stir_lib10 =...
    [stir_libpath 'numerics_buildblock\Release\numerics_buildblock.lib'];
stir_lib11 =...
    [stir_libpath 'recon_buildblock\Release\recon_buildblock.lib'];
stir_lib12 =...
    [stir_libpath 'scatter_buildblock\Release\scatter_buildblock.lib'];
stir_lib13 =...
    [stir_libpath 'Shape_buildblock\Release\Shape_buildblock.lib'];
stir_lib14 =...
    [stir_libpath...
    'spatial_transformation_buildblock\Release\'...
    'spatial_transformation_buildblock.lib'];

stir_regpath = stir_src;
stir_reg1 = [stir_regpath 'buildblock\buildblock_registries.cxx'];
stir_reg2 = [stir_regpath 'data_buildblock\data_buildblock_registries.cxx'];
stir_reg3 = [stir_regpath 'IO\IO_registries.cxx'];
stir_reg4 = [stir_regpath 'modelling_buildblock\modelling_registries.cxx'];
stir_reg5 = [stir_regpath 'recon_buildblock\recon_buildblock_registries.cxx'];
stir_reg6 = [stir_regpath 'Shape_buildblock\Shape_buildblock_registries.cxx'];
stir_reg7 = [stir_regpath...
    'spatial_transformation_buildblock\spatial_transformation_registries.cxx'];

mex('-largeArrayDims', ...
    boost_ipath, util_ipath, ...
    'mutilities.c', ...
    util_lib) 

mex('-largeArrayDims',...
    boost_ipath, stir_ipath, util_ipath,...
    'mstir.c', 'printer.cpp',...
    stir_reg1, stir_reg2, stir_reg3, stir_reg4,...
    stir_reg5, stir_reg6, stir_reg7,...
    util_lib, cstir_lib,...
    stir_lib1, stir_lib2, stir_lib3, stir_lib4, stir_lib5,...
    stir_lib6, stir_lib7, stir_lib8, stir_lib9, stir_lib10,...
    stir_lib11, stir_lib12, stir_lib13, stir_lib14);
