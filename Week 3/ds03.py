class EvenOddNumbers:
    def __init__(self):
        self.even_numbers = []
        self.odd_number = []
        
    def even_odd_numbers(self):
        self.even_numbers = []
        self.odd_numbers = []

        while True:
            number = int(input("Enter a number (0 to quit): "))
            if number != 0:
                if(number % 2 == 0):
                    self.even_numbers.append(number)
                else:
                    self.odd_numbers.append(number)
                number
            else:
                print("\nEven numbers:")
                for even_number in self.even_numbers:
                    print(even_number)
                
                print("\nOdd numbers:")
                for odd_number in self.odd_numbers:
                    print(odd_number)
                break

def main():
    get_number = EvenOddNumbers()
    get_number.even_odd_numbers()

if __name__ == "__main__":
    main()
