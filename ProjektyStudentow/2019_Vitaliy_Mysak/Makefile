
PROJ = example

headers = $(PROJ)/header.h $(PROJ)/declare.h $(PROJ)/define.c $(PROJ)/footer.c
additional-deps = Makefile  $(shell ls *.py)

CFLAGS = # -O3
TFLAGS =

# clang is faster. TCC is the fastest that I know of
CC = gcc

run: all
	./$(PROJ).exe

all: $(PROJ).exe
	@echo compiled

test:
	$(CC) $@/internal-test.c -O0 -g -o $@.internal.exe
	./$@.internal.exe

	$(MAKE) all PROJ=test CFLAGS='-O0' CC=tcc TFLAGS='--no-do-caching'
	test/checkout.sh
	$(MAKE) all PROJ=test CFLAGS='-O0' CC=tcc TFLAGS='--no-do-caching --no-use-typeid'
	test/checkout.sh
	$(MAKE) all PROJ=test CFLAGS='-O0' CC=tcc TFLAGS='--no-do-caching --no-use-typeid --make-inline'
	test/checkout.sh
	$(MAKE) all PROJ=test CFLAGS='-O0' CC=tcc TFLAGS='--do-caching    --no-use-typeid --make-inline'
	test/checkout.sh
	$(MAKE) all PROJ=test CFLAGS='-O0' CC=tcc
	test/checkout.sh

clean:
	- rm -f $(PROJ).c $(PROJ).exe $(PROJ)/script.inline.ini

$(PROJ).exe: $(PROJ).c $(PROJ)/header.c
	$(CC) -o $@ $^ $(CFLAGS)

$(PROJ).c: $(PROJ)/script.ini $(headers) $(additional-deps)
	./lambdacc.py --source $(PROJ)/script.ini --dest $(PROJ).c \
		--no-make-inline \
		--do-caching \
		--no-print-intermediate \
		--count-total-exec \
		--no-show-debug \
		--use-typeid \
		--echo-expr \
		--no-track-allocs \
		--no-track-pool-allocs \
		--flagsfile $(PROJ)/flags.h \
		--headerfile $(PROJ)/header.h \
		--declare-file $(PROJ)/declare.h \
		--define-file $(PROJ)/define.c \
		--footerfile $(PROJ)/footer.c \
		$(TFLAGS)

	@echo translated

$(PROJ)/declare.h $(PROJ)/define.c: $(PROJ)/custom.cfg.py $(additional-deps)
	./customwriter.py $(PROJ)/custom.cfg.py $(PROJ)/declare.h $(PROJ)/define.c

.PHONY: test clean all run
