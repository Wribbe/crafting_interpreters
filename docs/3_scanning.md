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
