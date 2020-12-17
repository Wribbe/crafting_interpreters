.SUFFIXES:

DIR_SRC := src
PACKAGE := com/craftinginterpreters

EXPR := ${PACKAGE}/lox/Expr.java

CLASSES = $(shell find -name "*.java") ${EXPR}
CLASSES := ${CLASSES:.java=.class}


CC := javac

all: ${EXPR} ${CLASSES}

%.class : %.java Makefile
	javac $(filter %.java,$^)

${EXPR} : ${PACKAGE}/tool/GenerateAst.java
	javac $^ && java ${^:.java=} $(dir $@)
