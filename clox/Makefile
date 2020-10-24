.SUFFIXES:

DIR_SRC := src
DIR_BIN := bin

BINS := $(patsubst ${DIR_SRC}/%.c,${DIR_BIN}/%,$(wildcard ${DIR_SRC}/*.c))

all: ${BINS}

${DIR_BIN}/% : ${DIR_SRC}/%.c Makefile | ${DIR_BIN}
	gcc $(filter %.c,$^) -o $@ -g -Wall -pedantic

${DIR_BIN} :
	mkdir $@
