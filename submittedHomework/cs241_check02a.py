def prompt_number():
    while True:
        question = int(input("Enter a positive number: ")) 
        if (question >= 0):
            return question
        else:
            print("Invalid entry. The number must be positive.")
            question

def main():
    first_question = prompt_number()
    print("")
    second_question = prompt_number()
    print("")
    third_question = prompt_number()
    print("")
    result = compute_sum(first_question, second_question, third_question)
    print("The sum is: %d" % result)
    
def compute_sum(first_question, second_question, third_question):
    sum = first_question + second_question + third_question
    return sum

if __name__ == "__main__":
    main()