# The Lox Language

```
// Your first Lox program!
print "Hello, world!";
```

Lox syntax is member of the C-family, `//` for comments and `;` on end of
lines. `print` is not a library function (no parenthesis), rather a built in
statement.


## A High-Level Language

### Dynamic typing

A variable can store a value of any type -> dynamic type.
Implementing it is easier than having static type-system -> faster
implementation and shorter book.


### Automatic memory management

Two main techniques for managing memory:
* **reference counting**
* **tracing garbage collection**

Easier to implement reference counting but are limited, usually need to expand
in order to at least handle object cycles.


## Data Types

The Lox built-in data types:

* **Booleans** - True / False.
* **Numbers** - double precision floats.
* **Strings** - enclosed in `"`.
* **Nil** - Represents "no value".


## Expressions

If the data types are atoms, expressions are molecules.


### Arithmetic

**Infix binary**
* **addition**: <operand> + <operand>
* **subtraction**: <operand> - <operand>
* **multiplication**: <operand> * <operand>
* **division**: <operand> / <operand>

**Prefix unary**:
* **subtraction**: -<operand>


### Comparisons and equality

Won't do implicit conversions, `Type1 != Type2`.

**Comparing** (Numbers): `<, <=, >=, >`
**Equality** (Any type): `== !=`


### Logical operator

**short-circuit** - If the first operand evaluates, return that one and don't
even evaluate the other.

`!` - not operator - _prefix
`and` - and operator - _infix_
`or` - or operator - _infix_
