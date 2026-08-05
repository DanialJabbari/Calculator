print("welcome to the calculator")
print("(digits, ., +, -, *, /, c are valid)")

valid_chars = set("0123456789.+-*/")
expression = []

while True:
    entry = input()

    if entry == "c":
        expression = []
        print("cleared")
        continue

    if entry == "=":
        if expression:
            equation = " ".join(expression)
            result = eval(equation)
            print(equation)
            print(result)
            expression = []
        continue

    if entry != "" and all(ch in valid_chars for ch in entry):
        expression.append(entry)
    else:
        print("invalid input, try again")