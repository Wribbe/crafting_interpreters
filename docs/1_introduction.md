# Introduction

Static type systems and mathematical theorems are two sides of the same coin
according to
[the Curry-Howard isomorphism.](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)
Language in question: Lox, one variant written in Java (jlox) and one written
in C (clox).

**self-hosting** - The language is compiled by a compiler written in the
language that it compiles.

**bootstrapping** - Building an initial compiler in another language that
compiles the first version of the self-hosting compiler.

**C-implementation requirements:**
* Dynamic arrays
* Hash tables.
* Object representation.
* Memory management / GC.

## Challenges

1. Six domain-specific languages used in the project?
  * CSS
  * SCSS
  * HTML
  * Make
  * .gitignore (UNIX - wildcard?)
  * .iml (IntelliJ IDEA module settings)

2. Java
  * Hello World up and running.

3. C
  * Hello world.
  * doubly-linked-list (heap-allocated strings) insert/find/delete.
  * test the list functionality.
