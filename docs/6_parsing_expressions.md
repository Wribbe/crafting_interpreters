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
the parser-technique the book is going to use.

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
