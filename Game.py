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
        if self.__current_player == 1:
            self.__current_player = 2
        elif self.__current_player == 2:
            self.__current_player = 1

    def read_position(self):
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
        if self.__current_player == 1:
            return self.__fields[0].field_with_ships()
        elif self.__current_player == 2:
            return self.__fields[1].field_with_ships()

    def field_without_ships(self):
        if self.__current_player == 1:
            return self.__fields[1].field_without_ships()
        elif self.__current_player == 2:
            return self.__fields[0].field_without_ships()

    def end_game(self):
        print(str(self.__players[0].name) + " score is: "
              + str(self.__fields[0].score))
        print(str(self.__players[1].name) + " score is: "
              + str(self.__fields[1].score))
        Game.play = False

    def winner(self):
        if self.__current_player == 1:
            if self.__fields[0].winner():
                print(self.__players[0].name + "is winner!")
                return False
        elif self.__current_player == 2:
            if self.__fields[1].winner():
                print(self.__players[1].name + "is winner!")
                return False
        return True

    @staticmethod
    def introduction():
        print("Welcome to the BATTLESHIP!!!")
