CFLAGS = -O3 -fPIC -DNDEBUG -DGCC -I$(STIR_SRC)/include

IUTILITIES = $(SRC_PATH)/iUtilities
IUTILITIES_LIBRARY = $(BUILD_PATH)/iUtilities/libiutil.a
CSTIR = $(SRC_PATH)/xSTIR/cSTIR
CSTIR_LIBRARY = $(BUILD_PATH)/xSTIR/libcstir.a

INCLUDE =  -I$(MATLABROOT)/extern/include \
	-I$(IUTILITIES) -I$(CSTIR_SRC)

STIR_LIBS = \
			-lanalytic_FBP2D \
			-lanalytic_FBP3DRP \
			-literative_OSMAPOSL \
			-literative_OSSPS \
			-lrecon_buildblock \
			-lIO \
			-ldata_buildblock \
			-ldisplay \
			-leval_buildblock \
			-llistmode_buildblock \
			-lmodelling_buildblock \
			-lscatter_buildblock \
			-lShape_buildblock \
			-lnumerics_buildblock \
			-lspatial_transformation_buildblock \
			-lbuildblock

REG_OBJECTS = \
	buildblock_registries.o \
	data_buildblock_registries.o \
	IO_registries.o \
	modelling_registries.o \
	recon_buildblock_registries.o \
	Shape_buildblock_registries.o \
	spatial_transformation_registries.o

TARGET1 = mutilities.mexa64
TARGET2 = mstir.mexa64

all: TARGET1 TARGET2

buildblock_registries.o: $(STIR_SRC)/buildblock/buildblock_registries.cxx
	$(CXX) $(CFLAGS) -c -o $@ $<

data_buildblock_registries.o: $(STIR_SRC)/data_buildblock/data_buildblock_registries.cxx
	$(CXX) $(CFLAGS) -c -o $@ $<

IO_registries.o: $(STIR_SRC)/IO/IO_registries.cxx
	$(CXX) $(CFLAGS) -c -o $@ $<

modelling_registries.o: $(STIR_SRC)/modelling_buildblock/modelling_registries.cxx
	$(CXX) $(CFLAGS) -c -o $@ $<

recon_buildblock_registries.o: $(STIR_SRC)/recon_buildblock/recon_buildblock_registries.cxx
	$(CXX) $(CFLAGS) -c -o $@ $<

Shape_buildblock_registries.o: $(STIR_SRC)/Shape_buildblock/Shape_buildblock_registries.cxx
	$(CXX) $(CFLAGS) -c -o $@ $<

spatial_transformation_registries.o: \
		$(STIR_SRC)/spatial_transformation_buildblock/spatial_transformation_registries.cxx
	$(CXX) $(CFLAGS) -c -o $@ $<

OBJECTS1 = mutilities.o
OBJECTS2 = mstir.o

TARGET1: $(OBJECTS1)
	$(GCC) $(CFLAGS) \
	-shared -Wl,-soname,$(TARGET1) \
	-o $(TARGET1) $(OBJECTS1) $(IUTILITIES_LIBRARY)

TARGET2: $(OBJECTS2) $(REG_OBJECTS) printer.o
	$(GCC) $(CFLAGS) \
	-shared -Wl,-soname,$(TARGET2) \
	-o $(TARGET2) $(OBJECTS2) $(REG_OBJECTS) printer.o \
	$(IUTILITIES_LIBRARY) \
	$(CSTIR_LIBRARY) \
	-L$(STIR_LIBPATH) $(STIR_LIBS)

%.o: %.c
	$(GCC) $(CFLAGS) $(INCLUDE) -c -o $@ $<

%.o: %.cpp
	$(GCC) $(CFLAGS) $(INCLUDE) -c -o $@ $<

clean:
	rm -f *.o

