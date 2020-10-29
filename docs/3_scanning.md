# Scanning

series of characters -> **tokens** that is then fed into the parser.

`switch` statement with delusions of grandeur.


# The Interpreter Framework

Good engineering practice to separate code that _generates_ the errors from the
code that _reports_ them.

Ideally there would be an "ErrorReporter" interface that gets passed to scanner
and parser -> possible to switch strategies.


## Lexemes and Tokens
_lexical analysis_ - turn characters into groups of blobs that represents
something, each blob -> **lexeme**.

**token** - lexeme + other useful information.


### Token type

**keyword** - _reserved_ word that means something special for the parser.

### Literal value

Scanner has to process all the characters in order to identify correctly, might
as well create a runtime-object that can be used by the interpreter.


### Location information

Need to start tracking here in order to display where an error occurred later.
Line-number fine for this simple implementation, a more advanced implementation
could add column and length too.


## Regular Languages and Expressions

Scanner built around a loop: start at first character -> identify the lexeme ->
emit a token -> repeat.

**lexical grammar** - the rules that determine which group of characters that
should be lexemes.
