from ..games.even import get_even_game
from ..cli import run_game

def main():
    run_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        get_even_game
    )

if __name__ == "__main__":
    main()
