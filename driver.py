import sys
from lang_lexer import lexical_analyzer

if __name__ == '__main__':
    mock_symbol_table = 'mock_symbol_table.csv'
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = lexical_analyzer(characters)
    # Create a new file to write the results of lexical analyzing the input file
    with open(mock_symbol_table, mode='w') as output_file:
        output_file.write(f'LEXEME, TOKEN\n')
        for lexeme, token in tokens:
            output_file.write(f'{lexeme}, {token}\n')