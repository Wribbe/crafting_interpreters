.SUFFIXES:

DIR_SRC := src
DIR_CLASSES := classes

CLASSES = $(shell find -name "*.java")
CLASSES := ${CLASSES:.java=.class}

CC := javac

all: ${CLASSES}

%.class : %.java Makefile
	javac $(filter %.java,$^)
