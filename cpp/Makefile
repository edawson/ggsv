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


all:
	echo "Not implemented"

$(CPP_DIR)/vg.pb.h: vg.proto .pre-build
	protoc --cpp_out=$(CPP_DIR) vg.proto

.pre-build:
	if [ ! -d $(BIN_DIR) ]; then mkdir -p $(BIN_DIR); fi
	if [ ! -d $(LIB_DIR) ]; then mkdir -p $(LIB_DIR); fi
	if [ ! -d $(OBJ_DIR) ]; then mkdir -p $(OBJ_DIR); fi
	if [ ! -d $(INC_DIR) ]; then mkdir -p $(INC_DIR); fi
	if [ ! -d $(CPP_DIR) ]; then mkdir -p $(CPP_DIR); fi
	touch .pre-build

