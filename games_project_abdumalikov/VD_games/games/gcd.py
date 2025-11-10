import random
import math

def get_gcd_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = math.gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, correct_answer
