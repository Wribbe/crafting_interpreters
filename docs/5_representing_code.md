# 5. Representing Code

Next chapter -> parser that will produce even more complex representation.
First we need to define that more complex representation, which is done in this
chapter.

Goals:
* Easily producible by parser.
* Easily consumed by interpreter.

Order of operations for arithmetics.

_post-order_ traversal -> traversing a tree from the leaves (end nodes) first
moving towards the top (root) node.

(One of the possible representation, human-friendly, other possibility for
representation is byte-code. Which is less human-readable but closer to the
machine.)

Going from regular-grammar -> context-free grammars. Need to be more precise
about the grammar, since the surrounding theory will be useful when impleenting
the interpreter.


## Context-Free Grammars

_regular language_ -> the rules how individual characters get grouped into
tokens. Not powerful enough to handle expressions that can be nested to an
arbitrary depth.

CFG (context-free grammar) is a _formal grammar_, which in turn is a grammar
consisting of an alphabet of atomic pieces/letters which define a set of strings
that are said to be "in" the grammar.

In the previous reglar-grammar each token was a character, and a string was a
'lexemes' ~= 'words'. Moving one abstraction up demotes the tokens into
characters, and a string becomes a sequence of tokens in order to form an entire
expression.

Lexical grammar: Characters -(make up a)-> Token.  
Syntactic grammar: Lexmes/tokens -(make up a)-> Expression.


### Rules for grammars

Since most grammars can produce an infinite amount of strings -> not possible to
list them all as an definition. Instead, finite set of rules are define in order
to define the grammar.

The rules defining the grammar can be applied in order to _generate_ strings
that are represented in the grammar. _derivations_ - the name of the generate
strings since they _derive_ from the rules of the grammar. _productions_ - the
rules themselves, since they _produce_ valid strings.

Anatomy of a _production_: _head_/_name_(1 symbol) + _body_(1-n symbols)  

Defining feature of context-free grammars -> single head/name symbol.
Symbols come in two different flavours:
* terminal -- letters from the grammars alphabet (no more moves -> terminal).
* nonterminal -- reference to another rule -> exec rule and insert result.

Possible to have multiple rules with with the same head/name, in that case,
allowed to choose whichever.

Codifying grammars is usually done by using BNF (Backus-Naur form) or a
flavoured version of it.

Lox grammar is defined as: `name -> terminal1 "non-terminal" terminal2 ;`

Since there are rules that expand a non-terminal on both sides -> non-regular
grammar. If the expansion is `X -> a X b` an we have `a X b` it can be
recursively expanded `N` times to `a a [...] a X b [...] b`. Here the `N`
number of the preceding `a`s needs to be matched by the same amount of
consecutive `b`s. Which is not possible to do with a regular grammar/language
since a regular language can _only repeat_, but _not count_.

Since a rule can have multiple productions + the rule is free to reference
itself directly or indirectly makes it possible to generate an infinite set of
strings for a small set of defining rules.


### Enhancing our notation

Adding som syntactic sugar to the notation:

`|` can be used to concatenate different productions.  
`bread -> "toast" | "biscuits" | "English muffin" ;`

`()` and `|` for grouping and selecting options within a grouping.  
`protein -> ( "scrambeled" | "poached" | "fried" ) "eggs" ;`

postfix `*` and `+` for repetition.  
`crispness -> "really" "really"* ; // repeates 0-n`  
`crispness -> "really"+ ; // repeats 1-n`

postfix `?` for optional production (one or zero).  
`breakfast -> protein ( "with" breakfast "on the side" )? ;`

Updated grammar using the new sugar:
```
breakfast -> protein ( "with" breakfast "on the side" )? |  bread ;

protein -> "realy"+ "crispy" "bacon"
         | "sausage'
         | ( "scrambled" | "poached" | "fried" ) eggs ;

bread -> "toast" | "biscuits" | "English muffin" ;
```

### A Grammar for lox expressions

Syntactical grammar > lexical grammar -> slog to implement it in one go. Will
implement a subset and then built on it in coming chapters.

```
expression -> literal | unary | binary | grouping ;
literal    -> NUMBER | STRING | "true" | "false" | "nil" ;
grouping   -> "(" expression ")" ;
unary      -> ( "-" | "!" ) expression ;
binary     -> expression operator expression ;
operator   -> "==" | "!=" | "<" | "<=" | ">" | ">=" | "+" | "-" | "*" | "/" ;
```

The above grammar is ambiguous, will be seen when parsing. 


## Implementing Syntax Trees

*syntax tree* -- The above grammar is recursive -> tree structure.  
*AST* -- _abstract_ syntax tree, does not include productions not needed later.  
*parse tree*  -- every single production becomes a tree-node.


## Metaprogramming the trees

Tedious to write all the classes -> generate them.


## Working with Trees

How to differentiate between different expressions with no type-enum? Could
compare class instances, but that's slow. Could do abstract `interpret()`
method, but that would not scale well, and forces different domains together.


## The Expression Problem

Object orientation -> easy to add row (new class). But hard to add a column,
(new functionality) since you have to crack open all the rows (classes). Given
pattern-matching, its easy to add columns (functionality) but hard to add new
types (rows) since you need new pattern-matches for all the old functionality.


## The Visitor pattern

This pattern helps approximate a functional programming style within an object
oriented language. By adding a layer of indirection, the new functionality for
all the current classes can be added in one place.


## Exercises

// Skipped.
