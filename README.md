# PseudoCode Programming Language

## Core Philosophy
Designing a programming language which is as simple to understand and use as pseudocode.

This language is designed for people just entering into the world of programming as well as for experienced programmers who just want to prototype their ideas.

## About the Authors
This programming language is designed and developed by senior year B.Tech Computer Science students undertaking Compiler Design course at Apeejay Stya University in India.

The project is done under the mentorship of Dr. Manpreet Singh Sehgal who is the professor of the aforementioned course.

## About the Language

### Keywords

```
begin, end, function, return,
loop, do, break, continue,
if, else, then, and, or, not,
True, False, None
```

### Regular Grammar (expressed in Regular Expressions)

```
1. AssignOp -> =
2. RelOp -> < | > | <= | >= | != | ==
3. ArithOp -> + | - | * | / | % | ** | //
4. LogOp -> and | or | not
5. Op -> Relop | AssignOp | ArithOp | LogOp
6. Letter -> [a-zA-z]
7. Digit -> [0-9]
8. Variable -> Letter|_(Letter|Digit|_)*
9. Delim -> [ ] | \n | \t | \r | \v | \b | \f
10. Whitespace -> Delim+
12. AsciiChar -> ^[ -~]+$
13. StringType -> "(AsciiChar)*" | '(AsciiChar)*'
14. IntegerType -> (+| -)?Digit+
15. DecimalType -> Integer([.]Digit+)?(E(Integer))?
16. BooleanType -> True | False
17. NoneType -> None
```