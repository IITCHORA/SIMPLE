class calculator:
    def __init__(self, operation,num1, num2):
        try:
            self.operation = str(operation)
            self.num1 = float(num1)
            self.num2 = float(num2)
        except:
            print("PLEASE WRITE THE NUMBER OR OPERATION (+ , -, ** , )")
    
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def exponention(self):
        return self.num1 ** self.num2
while True:
    num1 = input("ENTER THE FIRST NUMBER: ")
    num2 = input("ENTER THE SECOND NUMBER: ")
    operation = input("ENTER THE OPERATION YOU WANT TO DO: ")
    calc = calculator(operation , num1, num2)
    match operation:
        case "+":
            print(calc.add())
        case "-":
            print(calc.subtract())
        case "*" | "X":
            print(calc.multiply())
        case "**":
            print(calc.exponention())
        case _:
            continue
