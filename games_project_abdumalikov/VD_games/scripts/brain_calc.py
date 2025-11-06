import random
import prompt

def calculate_expression(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2

def play_calc_game():
    print("Welcome to the VD games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
    print('What is the result of the expression?')
    
    correct_answers_count = 0
    while correct_answers_count < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operation = random.choice(['+', '-', '*'])
        
        correct_answer = calculate_expression(num1, num2, operation)
        
        print(f"Question: {num1} {operation} {num2}")
        user_answer = prompt.string("Your answer: ")
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def main():
    play_calc_game()

if __name__ == "__main__":
    main()
