from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        if self.value == 0:
            return True
        else:
            return False


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    HUMAN_WIN = (1, 1, 1)
    COMPUTER_WIN = (2, 2, 2)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    @staticmethod
    def __check_indexes(item):
        if isinstance(item[0], int) is False or isinstance(item[1], int) is False:
            return False
        elif item[0] < 0 or item[0] > 2 or item[1] < 0 or item[1] > 2:
            return False
        else:
            return True

    def __getitem__(self, item):
        if self.__check_indexes(item) is False:
            raise IndexError('некорректно указанные индексы')
        else:
            return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if self.__check_indexes(key) is False:
            raise IndexError('некорректно указанные индексы')
        elif value not in (self.FREE_CELL, self.HUMAN_X, self.COMPUTER_O):
            raise ValueError('некорректное значение клетки')
        else:
            self.pole[key[0]][key[1]].value = value

    def init(self):
        for i in range(len(self.pole[0])):
            for j in range(len(self.pole[1])):
                self[i, j] = 0

    def show(self):
        print('   1   2   3 ')
        print(' -------------')
        for i in range(len(self.pole[0])):
            print(f"{i + 1}|", end=" ")
            for j in range(len(self.pole[1])):
                if self[i, j] == 1:
                    print('X', end=" | ")
                elif self[i, j] == 2:
                    print('0', end=" | ")
                else:
                    print(' ', end=" | ")
            print()
            print(' -------------')

    def human_go(self):
        while True:
            i, j = tuple(map(int,
                             input("Введите два числа от одного до трёх(координаты клетки) через пробел: ").split(" ")))
            if self[i - 1, j - 1] == 0:
                self[i - 1, j - 1] = 1
                print("Игрок сделал ход")
                break
            else:
                print("Данная клетка занята введите пожалуйста координаты другой клетки")

    def computer_go(self):
        while True:
            i = randint(1, 3)
            j = randint(1, 3)

            if self[i - 1, j - 1] == 0:
                self[i - 1, j - 1] = 2
                print("Компьютер сделал ход")
                break

    @property
    def is_human_win(self):
        main_diagonal, other_diagonal = True, True

        for i in range(len(self.pole[0])):
            temp_row = tuple(self.pole[i][j].value for j in range(len(self.pole[1])))
            temp_column = tuple(self.pole[j][i].value for j in range(len(self.pole[1])))
            if temp_row == self.HUMAN_WIN or temp_column == self.HUMAN_WIN:
                return True

            if self.pole[i][i].value != 1:
                main_diagonal = False

            if self.pole[i][len(self.pole[0]) - 1 - i].value != 1:
                other_diagonal = False

        if main_diagonal is True or other_diagonal is True:
            return True
        else:
            return False

    @property
    def is_computer_win(self):
        main_diagonal, other_diagonal = True, True

        for i in range(len(self.pole[0])):
            temp_row = tuple(self.pole[i][j].value for j in range(len(self.pole[1])))
            temp_column = tuple(self.pole[j][i].value for j in range(len(self.pole[1])))
            if temp_row == self.COMPUTER_WIN or temp_column == self.COMPUTER_WIN:
                return True

            if self.pole[i][i].value != 2:
                main_diagonal = False

            if self.pole[i][len(self.pole[0]) - 1 - i].value != 2:
                other_diagonal = False

        if main_diagonal is True or other_diagonal is True:
            return True
        else:
            return False

    @property
    def is_draw(self):
        if self.is_computer_win is False and self.is_human_win is False and bool(self) is False:
            return True
        else:
            return False

    def __bool__(self):
        result = False
        if self.is_human_win is False and self.is_computer_win is False:
            result = True

        is_free_cell = False
        for i in range(len(self.pole[0])):
            for j in range(len(self.pole[1])):
                if bool(self.pole[i][j]) is True:
                    is_free_cell = True
                    break

        return result and is_free_cell


def play(game):
    step_game = 0
    while game:
        game.show()

        if step_game % 2 == 0:
            game.human_go()
        else:
            game.computer_go()

        step_game += 1

    game.show()

    if game.is_human_win:
        print("Поздравляем! Вы победили!")
    elif game.is_computer_win:
        print("Все получится, со временем")
    else:
        print("Ничья.")

    print(f"Игра состояла из {step_game} ходов")


my_game = TicTacToe()
play(my_game)
