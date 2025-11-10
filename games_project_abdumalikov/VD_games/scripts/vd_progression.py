from ..games.progression import get_progression_game
from ..cli import run_game

def main():
    run_game(
        'What number is missing in the progression?',
        get_progression_game
    )

if __name__ == "__main__":
    main()
