import random

def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    
    return progression

def get_progression_game():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    
    return question, correct_answer
