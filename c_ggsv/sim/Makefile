CXX:= g++
CXXFLAGS:= -O2 -g -D_FILE_OFFSET_BITS=64 -I../io/fastahack
EXE:= svsim
SRC:= sim.cpp



sim: 
	$(CXX) $(CXXFLAGS) ../io/fastahack/Fasta.o ../io/fastahack/split.o -o $(EXE) $(SRC)

.PHONY: clean

clean:
	$(RM) $(EXE)