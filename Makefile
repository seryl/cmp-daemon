prefix=/usr

.PHONY: install clean

all: cmp-daemon

cmp-daemon:
	gcc -Wall cmp-daemon.c -o cmp-daemon

install:
  install -m 0755 cmp-daemon $(prefix)/sbin

clean:
  rm -f cmp-daemon
