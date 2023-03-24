from ui.gui import Screen
from services.game_logic import Game


def main():
    game_logic = Game()
    
    screen = Screen("score_service", game_logic)

    screen.main_loop()


if __name__ == "__main__":
    main()