class Caculator: 

    def __init__(self, input1, input2) -> None:
        self.input1 = input1
        self.input2 = input2

    def adder(self):
        self.result = self.input1 + self.input2
        return self.result
        
    def subtractor(self):
        self.result = self.input1 - self.input2
        return self.result
        
    def multiplier(self):
        self.result = self.input1 * self.input2
        return self.result

    def divider(self):
        self.result = self.input1 / self.input2
        return self.result

    def clear(self):
        self.input1 = 0.0
        self.input2 = 0.0

input1 = input("\nEnter the first number: ")
input2 = input("Enter the second number: ")
calculate = Caculator(float(input1), float(input2))
print("\nSum of two inputs is:",calculate.adder())
print("Subtraction of two inputs is:",calculate.subtractor())
print("Mutiply of two inputs is:",calculate.multiplier())
print("Divide of two inputs is: {:.2f}".format(calculate.divider(),2))
calculate.clear()