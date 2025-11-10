from ..games.prime import get_prime_game
from ..cli import run_game

def main():
    run_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        get_prime_game
    )

if __name__ == "__main__":
    main()
