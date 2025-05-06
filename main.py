import os
import argparse
from lexer import Lexer

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='C++ Lexical Analyzer')
    parser.add_argument('input', help='Input C++ file')
    parser.add_argument('-o', '--output', help='Output file for tokens', default='')
    
    args = parser.parse_args()
    
    # Determine output file name if not specified
    if not args.output:
        input_base = os.path.splitext(args.input)[0]
        args.output = f"{input_base}_tokens.txt"
    
    # Check if input file exists
    if not os.path.isfile(args.input):
        print(f"Error: Input file '{args.input}' does not exist.")
        return
    
    # Create and run the lexer
    lexer = Lexer(args.input, args.output)
    lexer.tokenize()
    
    print(f"Lexical analysis complete.")
    print(f"Tokens written to '{args.output}'.")

if __name__ == "__main__":
    main()