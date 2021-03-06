from field import Field
from player import Player


class Game:
    play = True

    def __init__(self):
        self.__fields = [Field(), Field()]
        name1 = input("Enter first player name: ")
        name2 = input("Enter second player name: ")
        self.__players = [Player(name1), Player(name2)]
        self.__current_player = 1

    def change_player(self):
        """
        Change player
        """
        if self.__current_player == 1:
            self.__current_player = 2
        elif self.__current_player == 2:
            self.__current_player = 1

    def read_position(self):
        """
        Read postion from player
        """
        cord = 0
        if self.__current_player == 1:
            while cord == 0:
                cord = self.__players[0].read_position()
            if self.__fields[0].shoot_at(cord):
                print("Good job! You can shoot one more")
            else:
                self.change_player()
        elif self.__current_player == 2:
            while cord == 0:
                cord = self.__players[1].read_position()
            if self.__fields[1].shoot_at(cord):
                print("Good job! You can shoot one more")
            else:
                self.change_player()

    def field_with_ships(self):
        """
        Return on the screen field with ships
        """
        if self.__current_player == 1:
            return self.__fields[0].field_with_ships()
        elif self.__current_player == 2:
            return self.__fields[1].field_with_ships()

    def field_without_ships(self):
        """
        Return on the screen field without ships
        """
        if self.__current_player == 1:
            return self.__fields[1].field_without_ships()
        elif self.__current_player == 2:
            return self.__fields[0].field_without_ships()

    def end_game(self):
        """
        If you call this method game is over
        """
        print(str(self.__players[0]._Player__name) + " score is: "
              + str(self.__fields[0].score))
        print(str(self.__players[1]._Player__name) + " score is: "
              + str(self.__fields[1].score))
        Game.play = False

    def winner(self):
        """
        Show the winner and end the game
        """
        if self.__current_player == 1:
            if self.__fields[0].winner():
                print(self.__players[0]._Player__name + "is winner!")
                Game.play = False
        elif self.__current_player == 2:
            if self.__fields[1].winner():
                print(self.__players[1]._Player__name + "is winner!")
                Game.play = False

    @staticmethod
    def introduction():
        print("Welcome to the BATTLESHIP!!!")

