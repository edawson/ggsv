EXEC:= ggsv
CC:= g++
CXXFLAGS:= "-O3 -g -mtune=native -march=native"

ggsv:
	$(CC) -o $(EXEC) ggsv.cpp
	
.PHONY: clean

clean:
	$(RM) $(EXEC)