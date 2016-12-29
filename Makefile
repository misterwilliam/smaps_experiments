CFLAGS := -Wall -g2 -O0 -Wno-unused

BINARIES :=
BINARIES += null

all: $(BINARIES)
clean:
	rm -f *.o $(BINARIES)
