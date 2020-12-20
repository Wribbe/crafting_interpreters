#!/usr/bin/env python

source = """
←→
TABLE OF CONTENTS
I.WELCOME
1.Introduction
 Design Note: What’s in a Name?
2.A Map of the Territory
3.The Lox Language
 Design Note: Expressions and Statements
II.A TREE-WALK INTERPRETER
4.Scanning
 Design Note: Implicit Semicolons
5.Representing Code
6.Parsing Expressions
 Design Note: Logic Versus History
7.Evaluating Expressions
 Design Note: Static and Dynamic Typing
8.Statements and State
 Design Note: Implicit Variable Declaration
9.Control Flow
 Design Note: Spoonfuls of Syntactic Sugar
10.Functions
11.Resolving and Binding
12.Classes
 Design Note: Prototypes and Power
13.Inheritance
III.A BYTECODE VIRTUAL MACHINE
14.Chunks of Bytecode
 Design Note: Test Your Language
15.A Virtual Machine
 Design Note: Register-Based Bytecode
16.Scanning on Demand
17.Compiling Expressions
 Design Note: It’s Just Parsing
18.Types of Values
19.Strings
 Design Note: String Encoding
20.Hash Tables
21.Global Variables
22.Local Variables
23.Jumping Back and Forth
 Design Note: Considering Goto Harmful
24.Calls and Functions
25.Closures
 Design Note: Closing Over the Loop Variable
26.Garbage Collection
 Design Note: Generational Collectors
27.Classes and Instances
28.Methods and Initializers
 Design Note: Novelty Budget
29.Superclasses
30.Optimization
❧BACKMATTER
A1.Appendix I: Lox Grammar
A2.Appendix II: Generated Syntax Tree Classes
FIRST PART: “WELCOME” →Handcrafted by Robert Nystrom — © 2015 – 2020
"""

from pathlib import Path

files_to_create = []
files_total = []
PATH_ROOT = Path(__file__).parent.parent

for line in source.splitlines():

  if len(tok := line.split('.', 1)) < 2:
    continue
  if (num := tok[0]).isnumeric():
    title = tok[1].lower().replace(' ','_')
    filename = f"{num}_{title}.md"
    path_file = Path(PATH_ROOT,'docs',filename)
    files_total.append(path_file)
    if not path_file.is_file():
      files_to_create.append(path_file)

  PATH_README = PATH_ROOT/'README.md'
  links_in_readme = []

def path_in_readme(path):
  for line in PATH_README.read_text().splitlines():
    if path.name in line:
      return True
  return False

add_to_readme = []
for path in files_total:
  if path_in_readme(path):
    continue
  add_to_readme.append(path)

def path_to_name(path):
  return path.name.split('_', 1)[-1][:-3].replace("_"," ").title()

def path_to_md_link(path):
  name = path_to_name(path)
  link = f"docs/{path.name}"
  return f"1. [{name}]({link})"

import os
add_to_readme = os.linesep.join([path_to_md_link(p) for p in add_to_readme])
readme_new = PATH_README.read_text() + add_to_readme

print("The final README will be:")
print(readme_new)

print("And the following files will be created:")
for path in files_to_create:
  print(f"  {path}")

proceed = input("Proceed? (Y/N): ").lower()

import sys
if proceed != "y":
  print("Aborting.")
  sys.exit(-1)

for path in files_to_create:
  path.write_text(f"# {path_to_name(path)}")

PATH_README.write_text(readme_new)
