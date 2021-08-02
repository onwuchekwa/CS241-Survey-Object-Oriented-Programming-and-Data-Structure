def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))
    
def main():
    number = int(input("Enter a Fibonacci index: "))
    if(number < 0):
        print("You must provide a number greater than 0")
    else:
        print("The Fibonacci number is: {}".format(fib(number)))
        
if __name__ == "__main__":
    main()