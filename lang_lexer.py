import lexer

KEYWORD = 'KEYWORD'
NUMBER = 'NUMBER'
DECIMAL = 'DECIMAL'
STRING = 'STRING'
NONE_TYPE = 'NONE_TYPE'
IDENTIFIER = 'IDENTIFIER'
ASSIGN_OPERATOR = 'ASSIGN_OPERATOR'
EQUALS_OPERATOR = 'EQUALS_OPERATOR'
NOT_EQUALS_OPERATOR = 'NOT_EQUALS_OPERATOR'
GREATER_THAN_OPERATOR = 'GREATER_THAN_OPERATOR'
LESS_THAN_OPERATOR = 'LESS_THAN_OPERATOR'
GREATER_THAN_OR_EQUAL_TO_OPERATOR = 'GREATER_THAN_OR_EQUAL_TO_OPERATOR'
LESS_THAN_OR_EQUAL_TO_OPERATOR = 'LESS_THAN_OR_EQUAL_TO_OPERATOR'
ADDITION_OPERATOR = 'ADD_OPERATOR'
SUBTRACTION_OPERATOR = 'SUBTRACTION_OPERATOR'
MULTIPLICATION_OPERATOR = 'MULTIPLICATION_OPERATOR'
DIVISION_OPERATOR = 'DIVISION_OPERATOR'
EXPONENTIATION_OPERATOR = 'EXPONENTIATION_OPERATOR'
MODULO_OPERATOR = 'MODULO_OPERATOR'
LOGICAL_AND_OPERATOR = 'LOGICAL_AND_OPERATOR'
LOGICAL_OR_OPERATOR = 'LOGICAL_OR_OPERATOR'
LOGICAL_NOT_OPERATOR = 'LOGICAL_NOT_OPERATOR'
IF_KEYWORD = 'IF_KEYWORD'
ELSE_KEYWORD = 'ELSE_KEYWORD'
THEN_KEYWORD = 'THEN_KEYWORD'
BEGIN_KEYWORD = 'BEGIN_KEYWORD'
END_KEYWORD = 'END_KEYWORD'
LOOP_KEYWORD = 'LOOP_KEYWORD'
DO_KEYWORD = 'DO_KEYWORD'
BREAK_KEYWORD = 'BREAK_KEYWORD'
CONTINUE_KEYWORD = 'CONTINUE_KEYWORD'
TRUE_KEYWORD = 'TRUE_KEYWORD'
FALSE_KEYWORD = 'FALSE_KEYWORD'
FUNCTION_KEYWORD = 'FUNCTION_KEYWORD'
FUNCTION_DECLARATION = 'FUNCTION_DECLARATION'
RETURN_KEYWORD = 'RETURN_KEYWORD'
OPEN_PAREN_SYMBOL = 'OPEN_PAREN_SYMBOL'
CLOSE_PAREN_SYMBOL = 'CLOSE_PAREN_SYMBOL'
OPEN_BRACKET_SYMBOL = 'OPEN_BRACKET_SYMBOL'
CLOSE_BRACKET_SYMBOL = 'CLOSE_BRACKET_SYMBOL'

token_exprs = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'\=',                    ASSIGN_OPERATOR),
    (r'\(',                    OPEN_PAREN_SYMBOL),
    (r'\)',                    CLOSE_PAREN_SYMBOL),
    (r'\[',                    OPEN_BRACKET_SYMBOL),
    (r'\]',                    CLOSE_BRACKET_SYMBOL),
    (r'\+',                    ADDITION_OPERATOR),
    (r'-',                     SUBTRACTION_OPERATOR),
    (r'\*',                    MULTIPLICATION_OPERATOR),
    (r'/',                     DIVISION_OPERATOR),
    (r'\*\*',                  EXPONENTIATION_OPERATOR),
    (r'%',                     MODULO_OPERATOR),
    (r'<=',                    LESS_THAN_OR_EQUAL_TO_OPERATOR),
    (r'<',                     LESS_THAN_OPERATOR),
    (r'>=',                    GREATER_THAN_OR_EQUAL_TO_OPERATOR),
    (r'>',                     GREATER_THAN_OPERATOR),
    (r'==',                    EQUALS_OPERATOR),
    (r'!=',                    NOT_EQUALS_OPERATOR),
    (r'and',                   LOGICAL_AND_OPERATOR),
    (r'or',                    LOGICAL_OR_OPERATOR),
    (r'not',                   LOGICAL_NOT_OPERATOR),
    (r'if',                    IF_KEYWORD),
    (r'then',                  THEN_KEYWORD),
    (r'else',                  ELSE_KEYWORD),
    (r'loop',                  LOOP_KEYWORD),
    (r'do',                    DO_KEYWORD),
    (r'break',                 BREAK_KEYWORD),
    (r'continue',              CONTINUE_KEYWORD),
    (r'begin',                 BEGIN_KEYWORD),
    (r'end',                   END_KEYWORD),
    (r'function',              FUNCTION_KEYWORD),
    (r'return',                RETURN_KEYWORD),
    (r'True',                  TRUE_KEYWORD),
    (r'False',                 FALSE_KEYWORD),
    (r'None',                  NONE_TYPE),
    (r'[+-]?[0-9]+',           NUMBER),
    (r'[+-]?[0-9]+[.][0-9]+',  DECIMAL),
    (r'[A-Za-z][A-Za-z0-9_]*', IDENTIFIER),
    (r'"[^"]*"',               STRING)
]


def lexical_analyzer(characters):
    return lexer.lex(characters, token_exprs)
