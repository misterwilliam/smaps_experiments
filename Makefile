CFLAGS := -Wall -g2 -O0 -Wno-unused

BINARIES :=
BINARIES += baseline

all: $(BINARIES)
clean:
	rm -f *.o $(BINARIES)
