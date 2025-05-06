import re
from token_definitions import COMPILED_PATTERNS, is_keyword, TOKEN_TYPES

class Lexer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.tokens = []
        
    def tokenize(self):
        """
        Read the input file and tokenize its contents
        """
        with open(self.input_file, 'r') as file:
            for line_number, line in enumerate(file, 1):
                self._tokenize_line(line, line_number)
                
        # Write tokens to output file
        self._write_output()
        
    def _tokenize_line(self, line, line_number):
        """
        Tokenize a single line of code
        """
        position = 0
        line = line.rstrip('\n')  # Remove trailing newline
        
        while position < len(line):
            match = None
            for pattern, token_type in COMPILED_PATTERNS:
                match = pattern.match(line, position)
                if match:
                    lexeme = match.group(0)
                    
                    # Skip whitespace tokens
                    if token_type == TOKEN_TYPES['WHITESPACE']:
                        position = match.end()
                        continue
                    
                    # Check if identifier is actually a keyword
                    if token_type == TOKEN_TYPES['IDENTIFIER'] and is_keyword(lexeme):
                        token_type = TOKEN_TYPES['KEYWORD']
                    
                    # Add token to our list
                    self.tokens.append({
                        'line': line_number,
                        'type': token_type,
                        'value': lexeme
                    })
                    
                    position = match.end()
                    break
            
            # If no match was found, treat the character as unknown and move on
            if not match:
                self.tokens.append({
                    'line': line_number,
                    'type': TOKEN_TYPES['UNKNOWN'],
                    'value': line[position]
                })
                position += 1
    
    def _write_output(self):
        """
        Write the tokens to the output file
        """
        with open(self.output_file, 'w') as file:
            for token in self.tokens:
                file.write(f"Line {token['line']}: Token = {token['value']} → {token['type']}\n")

    def get_tokens(self):
        """
        Return the list of tokens
        """
        return self.tokens