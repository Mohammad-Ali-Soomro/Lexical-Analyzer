import re
from token_definations import COMPILED_PATTERNS, is_keyword, TOKEN_TYPES

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
            
            # Special handling for multi-line comments
            if position + 1 < len(line) and line[position:position+2] == '/*':
                # We found the start of a multi-line comment
                # We need to read multiple lines to find the end
                comment_start = position
                comment_text = line[position:]
                end_found = '/*' in line and '*/' in line[line.find('/*') + 2:]
                current_line = line_number
                
                if not end_found:
                    # Need to read more lines to find the end of comment
                    comment_lines = [line[position:]]
                    with open(self.input_file, 'r') as file:
                        all_lines = file.readlines()
                        
                    for i in range(line_number, len(all_lines)):
                        if '*/' in all_lines[i]:
                            # Found the end
                            end_found = True
                            comment_lines.append(all_lines[i].rstrip('\n').split('*/')[0] + '*/')
                            break
                        elif i > line_number - 1:  # Skip current line as we already added it
                            comment_lines.append(all_lines[i].rstrip('\n'))
                    
                    # Combine all comment lines
                    comment_text = '\n'.join(comment_lines)
                    
                # Add the multi-line comment as a token
                self.tokens.append({
                    'line': line_number,
                    'type': TOKEN_TYPES['COMMENT'],
                    'value': comment_text if end_found else comment_text + "*/"  # Ensure it ends properly
                })
                
                # Move position to the end of the line
                position = len(line)
                continue
            
            # Regular token matching
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
                file.write(f"Line {token['line']}: Token = {token['value']} -> {token['type']}\n")

    def get_tokens(self):
        """
        Return the list of tokens
        """
        return self.tokens