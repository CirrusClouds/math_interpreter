from lexer import lex

if __name__ == "__main__":
    while True:
        name = input("calc>")
        print(lex(name))
