EXEC:= ggsv
CC:= g++
CXXFLAGS:= "-O3 -g -mtune=native -march=native"
SIMFLAGS:= "-O2 -g"
SIMEXE:= ./sim/sim
SIMSRC:= ./sim/sim.cpp
SIMINC:= -Ifastahack

ggsv:
	$(CC) -o $(EXEC) ggsv.cpp
	
.PHONY: clean

clean:
	$(RM) $(EXEC)
	$(RM) $(SIMEXE)
	
sim:
	$(CXX) $(SIMFLAGS) $(SIMINC) -o $(SIMEXE) $(SIMSRC)