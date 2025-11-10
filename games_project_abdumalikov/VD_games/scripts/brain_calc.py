from ..games.calc import get_calc_game
from ..cli import run_game

def main():
    run_game(
        'What is the result of the expression?',
        get_calc_game
    )

if __name__ == "__main__":
    main()
