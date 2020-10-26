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
