import random

def calculate_expression(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2

def get_calc_game():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    correct_answer = calculate_expression(num1, num2, operation)
    question = f"{num1} {operation} {num2}"
    return question, correct_answer
