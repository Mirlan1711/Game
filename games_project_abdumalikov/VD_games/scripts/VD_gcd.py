from ..games.gcd import get_gcd_game
from ..cli import run_game

def main():
    run_game(
        'Find the greatest common divisor of given numbers.',
        get_gcd_game
    )

if __name__ == "__main__":
    main()
