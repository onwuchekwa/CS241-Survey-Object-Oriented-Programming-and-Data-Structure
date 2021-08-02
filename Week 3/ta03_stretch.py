from fractions import Fraction

class Relational:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1
        
    def display(self):
        if (self.numerator > self.denominator):
            self.whole = self.numerator // self.denominator
            self.remainder = self.numerator % self.denominator
            print("{0} {1}/{2}".format(self.whole, self.remainder, self.denominator))
        else:
            print("{0}/{1}".format(self.numerator, self.denominator))
        
    def reduce(self):
        self.simplify = Fraction(self.numerator, self.denominator)
        print("{}".format(self.simplify))
        
    def prompt(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))
        return Relational
    
    def multiply_by(self):        
        self.numerator1 = int(input("Enter the numerator: "))
        self.denominator1 = int(input("Enter the denominator: "))
        print(Fraction(self.numerator, self.denominator) * Fraction(self.numerator1, self.denominator1))

def main():
    show = Relational()
    show1 = Relational()
    show.display()
    show.prompt()    
    show.display()
    show.reduce()
    show.multiply_by()
    
if __name__ == "__main__":
    main()
