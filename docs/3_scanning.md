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

## Reserved Words and Identifiers

**maximal munch** - If more than one grammar can match,
_the one that matches the most characters wins_.

**reserved word** - Hard to separate identifier from reserved word until
reaching the end of the identifier.

## Challanges

1. The lexical grammars of Python and Haskell are not regular. What does htat
   mean? _non-regular, there are multiple ways to do things._
2. How does space affect CoffeeScript, Ruby and the C preprocessor?
   _CoffeScript_ -- Significant whitespace, delimits blocks of code. _Ruby_ --
   Some method calls (usually single argument) can be called without
   parenthesis, if it's ambiguous the space between calls can make it work.
   _C-preprocessor_ -- In `#define f() x is different from #define f () x" but
   when calling, f() and f     () are the same.
3. Significant whitespace if your have a language like Python, comments could
   include processor directives, or possibly useful when generating
   documentation?
4. Main problem is making sure that you match the number of opening and closing
   comment symbols.
