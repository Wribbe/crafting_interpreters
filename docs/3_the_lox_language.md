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
Main job is to **produce** a **value**.


### Arithmetic

**Infix binary**
* **addition**: `<operand> + <operand>`
* **subtraction**: `<operand> - <operand>`
* **multiplication**: `<operand> * <operand>`
* **division**: `<operand> / <operand>`

**Prefix unary**:
* **subtraction**: `-<operand>`


### Comparisons and equality

Won't do implicit conversions, `Type1 != Type2`.

**Comparing** (Numbers): `<, <=, >=, >`

**Equality** (Any type): `== !=`


### Logical operator

**short-circuit** - If the first operand evaluates, return that one and don't
even evaluate the other.

`!` - not operator - _prefix_

`and` - and operator - _infix_

`or` - or operator - _infix_

### Precedence and grouping

Same associativity and precedence as C, use `(` and `)` to override.


## Statements

**Produce** an **effect**. `print` is a statement that evaluates a single
expression and displays the result.

**expression statement** -- `;` after expression promotes the expression to
statement-hood. `"some expression";`.

Possible to use `{` and `}` in order to pack a series of statements where one
was expected.


## Variables

Declared using `var`, defaults to `nil` without initializer.


## Control Flow

`Look up Smalltalk - No built-in branching uses dynamic dispatch. `

Lox implements `if | else`,`while` and `for`. Skips `for-in` and similar due to
book-layout constraints.


## Functions

Same function-call semantics as C, skipping parenthesis results in a reference
to the function.

New functions are declared using `fun`.

Semantics regarding functions:
* **argument**, **actual parameter** - The actual value passed to a function,
  a function _call_ has an list of _arguments_.
* **parameters**,**formal parameters** or **formals** - variable that holds the
  argument value inside of the function body.

Function body is always a block, use a `return` statement to pass values back
from a function. If nothing is specified, all functions default to returning
`nil`.


### Closures

_first class_ functions -> functions can be passed around as variables.

Functions declarations are statements -> possible to declare functions inside
of other functions.

**closures** - A data structure that bundles together function code with needed
variables.

A _closure_ is used by a function that has to _close over_ any variables in
order to "hold on" to references to variables that need to be accessible even
after any outer function has returned.

When closures are implemented the variable scope can no longer be seen as a
simple stack, local variables can no longer be thrown away the moment the
function returns.


## Classes

Classes declared with `class`, internal functions without the `var`.

Creating instances of classes through `ClassName()`.


### Instantiation and initialization

Want to encapsulate state and behaviour together.

Assigning to class-fields creates the field if it is missing.

Use `this` in order to access internal field and methods.

Initial state dictated by a defined `init()` method.


### Inheritance

Lox support **single inheritance**, use `<` in class declaration:
`class Child < Parent {`

`super.init()` is used to call parent-class `init()`.


## The Standard Library

**core**- **standard-library** the functionality implemented directly into the
interpreter.

Current **standard-library**:
* `print()`
* `clock()`
