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
