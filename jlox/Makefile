.SUFFIXES:

DIR_SRC := src

CLASSES = $(shell find -name "*.java")
CLASSES := ${CLASSES:.java=.class}

CC := javac

all: ${CLASSES}

%.class : %.java Makefile
	javac $(filter %.java,$^)
