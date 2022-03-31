
def calculate(a, b, op):
    
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "/":
        result = a / b
    elif op == "*":
        result = a * b
    
    return result

def main():
    while True:
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))
        op = input("Operation(+-/*): ")

        res = calculate(a, b, op)
        print(f"Result: {res}")

if __name__ == "__main__":
    main()