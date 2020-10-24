.SUFFIXES:

DIR_SRC := src
DIR_BIN := bin
DIR_LIB := lib

BINS := $(patsubst ${DIR_SRC}/%.c,${DIR_BIN}/%,$(wildcard ${DIR_SRC}/*.c))
LIBS := $(wildcard ${DIR_LIB}/*.c)
HEADERS := $(wildcard ${DIR_LIB}/%.h)

FLAGS := -g -Wall -pedantic
INCLUDE := -Iinclude

all: ${BINS}

${DIR_BIN}/% : ${DIR_SRC}/%.c ${LIBS} ${HEADERS} Makefile | ${DIR_BIN}
	gcc $(filter %.c,$^) -o $@ ${FLAGS} ${INCLUDE}

${DIR_BIN} :
	mkdir $@
