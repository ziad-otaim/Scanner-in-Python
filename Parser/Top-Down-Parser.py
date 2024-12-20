class Rule:
    def __init__(self, non_terminal, production):
        self.non_terminal = non_terminal
        self.production = production

grammar = []
input_string = ""
input_index = 0

def is_non_terminal(symbol):
    return 'A' <= symbol <= 'Z'

def parse(non_terminal):
    global input_index
    for rule in grammar:
        if rule.non_terminal == non_terminal:
            temp_index = input_index
            match = True
            for symbol in rule.production:
                if is_non_terminal(symbol):
                    if not parse(symbol):
                        match = False
                        break
                else:
                    if input_index < len(input_string) and symbol == input_string[input_index]:
                        input_index += 1
                    else:
                        match = False
                        break
            if match:
                return True
            else:
                input_index = temp_index
    return False

def is_simple_grammar():
    for rule in grammar:
        if rule.non_terminal == rule.production[0]:
            return False
    return True

def main():
    global grammar, input_string, input_index
    while True:
        print("🔻 Grammars 🔻")
        num_rules = int(input("Enter the number of grammar rules: "))
        grammar = []
        for i in range(num_rules):
            rule_input = input(f"Enter rule {i + 1} (e.g., S=aSb): ").strip()
            non_terminal = rule_input[0]
            production = rule_input[2:]
            grammar.append(Rule(non_terminal, production))
        if not is_simple_grammar():
            print("The grammar isn't simple. Try again.")
            continue
        print("The grammar is simple.")
        while True:
            print("\n1-Another Grammar")
            print("2-Another String")
            print("3-Exit")
            choice = int(input("Enter your choice: ").strip())
            if choice == 1:
                break
            elif choice == 2:
                input_string = input("Enter the string to be checked: ").strip()
                input_index = 0
                if parse(grammar[0].non_terminal) and input_index == len(input_string):
                    print("Your input string is Accepted.")
                else:
                    print("Your input string is Rejected.")
            elif choice == 3:
                print("Exiting program...")
                return
            else:
                print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()