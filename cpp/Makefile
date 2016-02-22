CXX=g++
CXXFLAGS=-O3 -mtune=native -fopenmp -std=c++11
LD_LIB_FLAGS=-L./ -L./lib -lprotobuf
LD_INC_FLAGS=-I./ -I./include
EXE=ggsv

CPP_DIR=cpp
OBJ_DIR=obj
INC_DIR=include
BIN_DIR=bin
LIB_DIR=lib
SRC_DIR=src

$(EXE): $(OBJ_DIR)/main.o $(INC_DIR)/stream.hpp $(OBJ_DIR)/vg.pb.o
	$(CXX) $(CXXFLAGS) -o $@ $< $(OBJ_DIR)/vg.pb.o $(LD_INC_FLAGS) $(LD_LIB_FLAGS)

$(OBJ_DIR)/main.o: $(SRC_DIR)/main.cpp $(INC_DIR)/stream.hpp $(OBJ_DIR)/vg.pb.o
	$(CXX) $(CXXFLAGS) -c -o $@ $< $(LD_INC_FLAGS) $(LD_LIB_FLAGS)

all: $(CPP_DIR)/vg.pb.h .pre-build
	echo "Not implemented"

$(INC_DIR)/stream.hpp: .pre-build
	cp $(SRC_DIR)/stream.hpp $(INC_DIR)/stream.hpp

$(OBJ_DIR)/vg.pb.o: $(CPP_DIR)/vg.pb.cc .pre-build
	$(CXX) $(CXXFLAGS) -c -o $@ $< $(LD_INC_FLAGS) $(LD_LIB_FLAGS)

$(CPP_DIR)/vg.pb.cc: $(CPP_DIR)/vg.pb.h .pre-build
	$(CXX) $(CXXFLAGS) -c -o $(OBJ_DIR)/vg.pb.o $@ $(LD_INC_FLAGS) $(LD_LIB_FLAGS)

$(CPP_DIR)/vg.pb.h: .pre-build
	protoc --cpp_out=$(CPP_DIR) --proto_path=../ ../vg.proto && cp $(CPP_DIR)/vg.pb.h $(INC_DIR)/

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
