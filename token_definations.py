import re

# Define token types
TOKEN_TYPES = {
    'KEYWORD': 'Keyword',
    'IDENTIFIER': 'Identifier',
    'OPERATOR': 'Operator',
    'SEPARATOR': 'Separator',
    'INTEGER_LITERAL': 'Integer Literal',
    'FLOAT_LITERAL': 'Float Literal',
    'STRING_LITERAL': 'String Literal',
    'CHAR_LITERAL': 'Character Literal',
    'COMMENT': 'Comment',
    'PREPROCESSOR': 'Preprocessor Directive',
    'WHITESPACE': 'Whitespace',
    'UNKNOWN': 'Unknown'
}

# C++ keywords
CPP_KEYWORDS = [
    'alignas', 'alignof', 'and', 'and_eq', 'asm', 'auto', 'bitand', 'bitor',
    'bool', 'break', 'case', 'catch', 'char', 'char8_t', 'char16_t', 'char32_t',
    'class', 'compl', 'concept', 'const', 'consteval', 'constexpr', 'constinit',
    'const_cast', 'continue', 'co_await', 'co_return', 'co_yield', 'decltype',
    'default', 'delete', 'do', 'double', 'dynamic_cast', 'else', 'enum', 'explicit',
    'export', 'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'inline',
    'int', 'long', 'mutable', 'namespace', 'new', 'noexcept', 'not', 'not_eq',
    'nullptr', 'operator', 'or', 'or_eq', 'private', 'protected', 'public',
    'register', 'reinterpret_cast', 'requires', 'return', 'short', 'signed',
    'sizeof', 'static', 'static_assert', 'static_cast', 'struct', 'switch',
    'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef',
    'typeid', 'typename', 'union', 'unsigned', 'using', 'virtual', 'void',
    'volatile', 'wchar_t', 'while', 'xor', 'xor_eq'
]

# Token regex patterns
TOKEN_PATTERNS = [
    # Comments
    (r'\/\/.*', TOKEN_TYPES['COMMENT']),
    (r'\/\*(.|\n)*?\*\/', TOKEN_TYPES['COMMENT']),
    
    # Preprocessor directives
    (r'#\w+(?:\s+<.*?>|\s+".*?")?', TOKEN_TYPES['PREPROCESSOR']),
    
    # String literals
    (r'"[^"\\]*(\\.[^"\\]*)*"', TOKEN_TYPES['STRING_LITERAL']),
    
    # Character literals
    (r"'[^'\\]*(\\.[^'\\]*)*'", TOKEN_TYPES['CHAR_LITERAL']),
    
    # Float literals
    (r'\b\d+\.\d*([eE][+-]?\d+)?\b|\b\.\d+([eE][+-]?\d+)?\b|\b\d+[eE][+-]?\d+\b', TOKEN_TYPES['FLOAT_LITERAL']),
    
    # Integer literals (including hex and octal)
    (r'\b0[xX][0-9a-fA-F]+\b|\b0[0-7]+\b|\b\d+\b', TOKEN_TYPES['INTEGER_LITERAL']),
    
    # Keywords (added as a separate step)
    
    # Identifiers
    (r'\b[a-zA-Z_]\w*\b', TOKEN_TYPES['IDENTIFIER']),
    
    # Operators
    (r'(\+\+|--|\+=|-=|\*=|/=|%=|&=|\|=|\^=|<<=|>>=|<<|>>|<=|>=|==|!=|&&|\|\||[+\-*/%&|^<>=!~?:])', TOKEN_TYPES['OPERATOR']),
    
    # Separators
    (r'[{}()\[\];,.]', TOKEN_TYPES['SEPARATOR']),
    
    # Whitespace (usually ignored)
    (r'\s+', TOKEN_TYPES['WHITESPACE'])
]

# Compile regex patterns for efficiency
COMPILED_PATTERNS = [(re.compile(pattern), token_type) for pattern, token_type in TOKEN_PATTERNS]

# Add keywords to the patterns
def is_keyword(token):
    return token in CPP_KEYWORDS