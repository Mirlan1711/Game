import prompt

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

def run_game(game_description, get_question_and_answer):
    print("Welcome to the VD Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
    print(game_description)
    
    correct_answers_count = 0
    rounds_count = 3
    
    while correct_answers_count < rounds_count:
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
   
    print(f"Congratulations, {name}!")
