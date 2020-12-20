# Evaluating Expressions

Currently, the parser only knows how to handle expressions. So executing code
equates evaluating an expression and returning an value. There needs to be a
chunk of code that knows how to evaluate a tree and produce a result.

Raises two questions:
1. What kind of values do we produce?
1. How should the chunks of code be organized?


## Representing Values

Since Lox is dynamically typed, and the current implementation is done in Java,
there need to be a bridge between Java's static typing to Lox dynamic typing.
Which means that there needs to be an representation in Java that can hold
different types at different times -> `java.lang.Object`.
```
Lox type          Java Representation
=====================================
Any Lox value     Object
nil               null
Boolean           Boolean
number            Double
string            String
```
