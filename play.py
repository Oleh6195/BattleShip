from Game import Game


def main():
    game = Game()
    game.introduction()
    while game.play:
        print("There is your field: ")
        print(game.field_with_ships())
        print("\n")
        print("This is your rival's field: ")
        print(game.field_without_ships())
        game.read_position()
        consol = input("Enter exit if you want to finish game or press enter"
                       " and switch player: ")
        if consol == "exit":
            game.end_game()


main()
