# C++ Lexical Analyzer

This project implements a lexical analyzer (lexer) for C++ code using Python's `re` module. The analyzer tokenizes C++ source code without relying on external lexer/parser libraries.

## Project Structure

- `token_definitions.py`: Contains token type definitions and regex patterns
- `lexer.py`: Main lexical analyzer implementation
- `main.py`: Entry point for the program
- `test.cpp`: Sample C++ file for testing

## Requirements

- Python 3.6 or higher

## How to Use

1. Make sure all files are in the same directory
2. Run the analyzer using:

```bash
python main.py test.cpp
```

This will process `test.cpp` and generate a file named `test_tokens.txt` with the tokenized output.

3. To specify a custom output file:

```bash
python main.py test.cpp -o custom_output.txt
```

## Output Format

The analyzer produces output in the following format:

```
Line <line_number>: Token = <token_value> → <token_type>
```

## Example

Input (C++ code):
```cpp
int main() {
    float x = 3.14;
    // This is a comment
    if (x > 0) {
        x = x + 1;
    }
    return 0;
}
```

Output (tokens):
```
Line 1: Token = int → Keyword
Line 1: Token = main → Identifier
Line 1: Token = ( → Separator
Line 1: Token = ) → Separator
Line 1: Token = { → Separator
Line 2: Token = float → Keyword
Line 2: Token = x → Identifier
...
```

## Features

- Identifies keywords, identifiers, operators, separators, literals, comments, and preprocessor directives
- Handles multi-line comments
- Detects various numeric literals (integers, floats, hex, octal)
- Recognizes string and character literals
- Provides line number information for each token