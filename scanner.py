import re

# List of C language keywords
keywords = {
    "int", "float", "return", "if", "else", "for", "while", "do", "void", 
    "char", "double", "struct", "switch", "case", "break", "continue", 
    "goto", "enum", "const", "static", "extern", "register", "sizeof", 
    "typedef", "union", "volatile", "default", "short", "long", 
    "unsigned", "signed"
}

# Set of single-character operators and delimiters
operators = {'+', '-', '*', '/', '%', '=', '<', '>', '&', '|', '^', '!', '~'}
delimiters = {' ', ',', ';', '(', ')', '[', ']', '{', '}', '\n', '\t'}

# Function to classify tokens
def classifyToken(token):
    if token in keywords:
        return "Keyword"
    elif re.match(r"^[a-zA-Z_]\w*$", token):
        return "Identifier"
    elif re.match(r"^\d+(\.\d+)?$", token):  # Matches integers and floats
        return "Number"
    elif token in operators:
        return "Operator"
    elif token in delimiters:
        return "Delimiter"
    else:
        return "Unknown"

def analyzeCode(code):
    tokens = []
    current_token = ""

    for ch in code:
        if ch in delimiters or ch in operators:
            if current_token:  # If there's a current token, analyzeCode it
                tokens.append((current_token, classifyToken(current_token)))
                current_token = ""
            
            if ch not in {' ', '\n', '\t'}:  # Skip whitespace
                tokens.append((ch, classifyToken(ch)))
        elif ch.isalnum() or ch == '_':
            current_token += ch
        else:
            if current_token:
                tokens.append((current_token, classifyToken(current_token)))
                current_token = ""
            tokens.append((ch, "Unknown"))

    # Final token check
    if current_token:
        tokens.append((current_token, classifyToken(current_token)))
    
    return tokens

# Main function
def main():
    print("Enter C-like code (end with '$' on a new line):")
    code = []
    while True:
        line = input()
        if line.strip() == "$":
            break
        code.append(line)
    
    code = "\n".join(code)
    
    print("\nTokenized Output:")
    tokens = analyzeCode(code)
    for token, token_type in tokens:
        print(f"{token_type}: {token}")

if __name__ == "__main__":
    main()
