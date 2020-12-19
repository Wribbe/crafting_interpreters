# Parsing Expressions

The result of this chapter will be a real parser, with coherent internal
structure, and decent error handling that can chew through sophisticated syntax.

_Parsing_ -> transforming `tokens sequences` into `syntax-trees`.


## Ambiguity and the Parsing Game

_ambiguous_ -- when there are more than one set of `productions` that
produce/generate the same string, but different syntax trees.

How math works with ambiguity, `Precedence` and `Associativity`.

_Precedence_ -- Handles `binding`, a _tighter-bound_ / _higher precedence_
operator will be evaluated first, before operators a _lower precedence_.

_Associativity_ -- Regulates how multiples of the same operator in a row
behaves. _left-associative_ (left -> right) will evaluate the left operator
first.

If there are no associativity and precedence rules, any expression with multiple
operators can become ambiguous.

Using same precedence rules as C (lowest -> highest):
```
Equaltiy      == !=       Left
Comparison    > >= < <=   Left
Term          - +         Left
Factor        / *         Left
Unary         ! -         Right
```

Need to stratify the grammar, since currently the expression rule makes it
possible to accept any kind of expression as a sub-expression, ignoring
precedence. Need one rule for each precedence level.

```
expression   -> ...
equlaity     -> ...
comparison   -> ...
term         -> ...
factor       -> ...
unary        -> ...
primary      -> ...
```

Where each rule only matches expressions at it's level or higher.

New rules:  
`expression -> equality ;` helps keep the `expression` keyword, reads better.  
`primary -> NUMBER | STRING | "true" | "false" | "nil" | "(" expression ")";`  

Unary operators can nest and be the operand itself -> recursive.  
`unary -> ( "!" | "-" ) unary ;`
but does not terminate, needs to be modified to:
```
unary -> ( "!" | "-" ) unary
         | primary
         ;
```

Define the remaining binary rules.
```
factor  -> factor ( "/" | "*" ) unary
         | unary
         ;
```

__left-recursive__: Since the first non-terminal of the rule-body is the same as
the head -> this rule is `left-recursive`. Which will cause some trouble with
the parser-technique the book is going to use. (recursive descent -> if a
method-function refers to itself the first thing it does (left-recursion) then
the program goes into an infinite loop and runs out of stack-space.)

Better to use the matching rule:
```
factor -> unary ( ( "/" | "*" ) unary )* ;
```
where the factor is defined as a sequence of multiplications and divisions.
Using the same approach for the remaining rules produce the following
expression-grammar:
```
expression  -> equalty;
equality    -> comparison ( ( "!=" | "==" ) comparison )* ;
comparison  -> term ( ( ">" | ">=" | "<" "<=" ) term )* ;
term        -> factor ( ( "-" | "+" ) factor )* ;
factor      -> unary ( ( "-" | "+" ) unary )* ;
unary       -> ( "!" | "-" ) unary
             | primary;
primary     -> NUMBER | STRING | "true" | "alse" | "nil" | "(" expression ")";
```


## Recursive Descent Parsing

__"L/R" - parsers:__
* [LL(k)](https://en.wikipedia.org/wiki/LL_parser)
* [LR(1)](https://en.wikipedia.org/wiki/LR_parser)
* [LALR](https://en.wikipedia.org/wiki/LALR_parser)

__"Exotic parsers:__
* [parser combinators](https://en.wikipedia.org/wiki/Parser_combinator)
* [Earley parsers](https://en.wikipedia.org/wiki/Earley_parser)
* [the shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)
* [packrat parsing](https://en.wikipedia.org/wiki/Parsing_expression_grammar)


This project will use __recursive descent__ as the parser-methodology.

__top-down__ vs __bottom-up__: recursive descent is a `top-down parser` since it
starts from the outer most part of the syntax, here `expression` and works it
way down the nested sub-expressions into the leaves. In contrast, __LR__ is a
parser that starts from the leaves and then combines them into larger and larger
chunks of syntax.

When implementing a recursive descent parser the grammar is translated into
imperative code where each rule becomes a function, and recursive calls call the
same function again.
```
Terminal    -> Code that matches and consumes a token
Nonterminal -> Call to rule's function
|           -> switch / if statement
* or +      -> while / for
?           -> if statement
```

__predictive parsers__ -- Includes recursive descent, if the parser looks ahead
to make a decision -> _predictive parser_.


## Syntax errors

The parsers two jobs:
* Produce a syntax tree if given a correct sequence of tokens.
* Detect any errors and report to user if given a non-correct sequence of
tokens.

Additional hard requirements for the parser:
* __Detect and report the error__
* __Must not crash or hang__
Additional requirements for a good parser.
* __Be fast__
* __Report as many errors as there are__ -- Easy to abort on first, but keep
going.
* __Minimize _cascade_ errors__ -- Don't report ghost-errors due to being of
track from an initial error.

__error recovery__ - The name of the process where an parser hits an error and
tries to keep going in order to find later errors. Was more of a problem when
parsing a program took hours->days.


### Panic mode error recovery

* __panic mode__ - The parser has seen at least one error
* __synchronization__ - After entering panic mode, find the next sequence that
matches the rule being parsed. Usually done between statements, which we don't
have currently.


### Synchronizing a recursive decent parser

The parser state == the Java call-stack. In order to reset the state -> unwind
the stack by throwing an exception and catching it where we want to retry, which
is between statements.

Boundary between statements generally signaled by _ending with a_`;` or starting
with a keyword, e.g. `for`, `if`, `return`, `var`, etc.

Since there is currently no support for statements, any error will unwind up to
the top and stop the parsing.
