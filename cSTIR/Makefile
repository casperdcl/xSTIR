CXX = g++
EXTRA_CFLAGS=-O3 -DNDEBUG
#EXTRA_CFLAGS=-g
CFLAGS = $(EXTRA_CFLAGS) -fpermissive -fPIC -std=c++11 -I$(IUTILITIES) -I$(STIR_SRC)/include -I$(CSTIR_SRC)

ARCH = ar
ARCHFLAGS = cr
RANLIB = ranlib

IUTILITIES = $(SRC_PATH)/iUtilities
CSTIR_SRC = $(SRC_PATH)/cSTIR

CSTIRLIB = libcstir.a
CSTIR_LIB = -lcstir

#OBJECTS = ci_stir.o stir_p.o ci_dh.o ci_ex.o ci_tw.o
OBJECTS = ci_stir.o stir_p.o ci_tw.o

all: libcstir.a

libcstir.a: $(OBJECTS)
	$(ARCH) $(ARCHFLAGS) $(CSTIRLIB) $(OBJECTS)
	$(RANLIB) $(CSTIRLIB)
	mv libcstir.a $(BUILD_PATH)/xSTIR

%.o: %.cpp
	$(CXX) $(CFLAGS) -c -o $@ $<

clean:
	rm -f *.o
