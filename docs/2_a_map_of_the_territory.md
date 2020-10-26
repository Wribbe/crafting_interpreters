# A Map of the Territory

Language _implementation_ -- The nuts and bolts of how a particular language is
constructed.

## The Parts of a Language

Up and down a mountain.

### Scanning

**Scanning** or **lexing** -- taking linear string of characters and converting
them into **tokens**.

### Parsing

This step gives the syntax its **grammar** and it becomes possible to combine
smaller parts in order to compose larger expressions and statements.

The **parser** processes the token-sequence and constructs a **parse tree** or
**abstract syntax tree** that mirrors the nested structure of the grammar.
Also known as **syntax trees**, **ASTs** or **trees**.

Human language too messy/inconsistent for rigid parsing grammars, but they work
fine for the artificial grammars of programming languages.

Using the grammar incorrectly, the parser should report a **syntax error**.

### Static analysis

First stage where characteristics of a language start coming into play,
previous steps are mostly the same across language implementations.
The syntactic structure of the code is known, which expressions are nested
etc. but not much more.

**binding** or **resolution** -- for each **identifier** figure out where the
name is defined and couple them together.

**type error** -- If the language is statically typed, this is where the types
are figured out, and the error is generated if they are not valid.

**top of the mountain** -- Have good insight in the users programs semantics,
need to be stored away for usage later.

* Can be stored as **attributes** directly into the syntax tree.
* **Symbol table** -- lookup table off to the side keyed on identifiers where
  the values correspond to what the identifiers refers to.
* Transform the data into a structure that directly expresses then semantics of
  the code.

* **middle end** - More complex compilers -> outgrown **front end** and **back
  end**. New phases in **middle end**.

### Intermediate representations.

Compiler pipeline, organize the data in a way that makes the next step easier
to implement. **front end** -- source language the program is written in.
**back end** -- relates to the architecture where the program will run.

**IR** -- **intermediate representation** represents the code in the middle of
the pipeline and doesn't have to be dependent or either the source or final
platform. Common variants are:
* control flow graph
* static single-assignment
* continuation-passing style
* three-address-code

### Optimization

**optimization** -- When the wanted result is known -> can be possible to do it
more efficiently.

Skipped in this book, but can search for:
* constant propagation
* common subexpression elimination
* loop invariant code motion
* global value numbering
* strength reduction
* scalar replacement of aggregates
* dead code elimination
* loop unrolling


### Code generation

**generating code** or **codegen** is where the source finally becomes code
that the CPU can run, the **back end**. Can either run on the chipset directly
(lightning fast) or run on an intermediary virtual machine (portable).
**bytecode** are synthetic instructions that are designed to map closely to the
language's semantics without the chipset bagage.


### Virtual machine

With bytecode there are two ways forward:
* Use it as an intermediary and write a mini-compiler for each target. (fast)
* Writing a virtual machine that runs the bytecode. (portable)


### Runtime

At this point the code can be executed, either start up the VM and load the
program if it's bytecode, or if it is native code, tell the operating system to
load the code and execute.

If the codes makes use of any language-features like garbage collection or
type-checking, this is where these systems are initialized and managed -> the
**runtime**.


## Shortcuts and Alternate Routes

### Single-pass compilers

Due to resource constraints, no intermediate representation is generated.
No way to store information and does not revisit any already parsed part of the
the source.


### Tree-walk interpreters

Sometimes it's possible to execute code as soon as the AST has been generated.
The interpreter walks the syntax-tree evaluating nodes from branch to leaf.
Mostly used in learning contexts due to the slow speed, not used for
general-purpose languages.


### Transpilers

In this case another language is used as the intermediary. Instead of producing
a bytecode middle-step, a syntactically correct string of the other language is
generated and compiled with a compiler for that language.


### Just-in-time compilation

**JIT** -- Compile bytecode to native code supported by the architecture at
runtime. Can be coupled with profiling in order to figure out which part of a
the program flow needs to be compiled and/or optimized.


## Compilers and Interpreters

What is the difference between a compiler and an interpreter?

**Compiling** -- the _implementation technique_ of translating one type of
source code to another and not executing the result, that is left to the user.

**Interpreter** -- Runs at once by executing the given source-code directly.

**Compiling + Interpreter** - CPython _is_ an interpreter that _has_ a
compiler.

# Challenges

1. Pick an open source of a language you like. Download the source code and
   poke around in it. Try to find the code that implements the scanner and
   parser. Are they hand-written, or generated using tools like Lex and Yacc?
   (look for .l or .y files).
2. Just-in-time compilation tend to be the fastest way to implement a
   dynamically-typed language, but not all of them use it. What reason are
   there to _not_ JIT?
3. Most Lisp implementations that compile to C also contain an interpreter that
   lets them execute Lisp code on the fly as well. Why?

# Answers to challenges

_Answer 1_

Picked language: [Python](https://github.com/python/cpython).
* **Scanner**: Hand-written C, [cpython/Parser/tokenizer.c](https://github.com/python/cpython/blob/master/Parser/tokenizer.c)
* **Parser**: Hand-written C, [cpython/Parser/parser.c](https://github.com/python/cpython/blob/master/Parser/parser.c)

_Answer 2_

* Added overhead on startup and possibly runtime.
* Complexities due to requirement to be 'just-in-time'.

_Answer 3_

Easier to do iterative development with a script that can be reloaded instead
of having to re-compile the code in order to have the changes take effect.
