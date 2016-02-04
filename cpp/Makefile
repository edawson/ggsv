CXX=g++
CXXFLAGS=-O3 -mtune=native -mSSE4.1 -fopenmp
LD_LIB_FLAGS=
LD_INC_FLAGS=
EXE=ggsv

CPP_DIR=cpp
OBJ_DIR=obj
INC_DIR=include
BIN_DIR=bin
LIB_DIR=lib


all: $(CPP_DIR)/vg.pb.h .pre-build
	echo "Not implemented"

$(INC_DIR)/stream.hpp: .pre-build
	cp $(SRC_DIR)/stream.hpp $(INC_DIR)/stream.hpp

$(OBJ_DIR)/vg.pb.o: $(CPP_DIR)/vg.pb.h .pre-build
	$(CXX) -O3 -msse4.1 -fopenmp -std=c++11 -c -o $@ $< $(LD_INCLUDE_FLAGS) $(LD_LIB_FLAGS)

$(CPP_DIR)/vg.pb.h: .pre-build
	protoc --cpp_out=$(CPP_DIR) vg.proto

.pre-build:
	if [ ! -d $(BIN_DIR) ]; then mkdir -p $(BIN_DIR); fi
	if [ ! -d $(LIB_DIR) ]; then mkdir -p $(LIB_DIR); fi
	if [ ! -d $(OBJ_DIR) ]; then mkdir -p $(OBJ_DIR); fi
	if [ ! -d $(INC_DIR) ]; then mkdir -p $(INC_DIR); fi
	if [ ! -d $(CPP_DIR) ]; then mkdir -p $(CPP_DIR); fi
	touch .pre-build

.PHONY: clean

clean:
	$(RM) -r $(BIN_DIR)
	$(RM) -r $(LIB_DIR)
	$(RM) -r $(INC_DIR)
	$(RM) -r $(OBJ_DIR)
	$(RM) -r $(CPP_DIR)
	rm .pre-build

