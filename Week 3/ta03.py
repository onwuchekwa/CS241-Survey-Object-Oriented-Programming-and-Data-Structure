class Fraction:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1
        
    def display(self):
        print("{0}/{1}".format(self.numerator, self.denominator))
        
    def prompt(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))
        return Fraction
    
    def display_decimal(self):
        print(self.numerator / self.denominator)

def main():
    show = Fraction()
    show.display()
    show.prompt()
    show.display()
    show.display_decimal()
    
if __name__ == "__main__":
    main()