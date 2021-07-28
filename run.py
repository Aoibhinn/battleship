from random import randint


class Board:
    """
    Main board class, Sets board size, the number of ships,
    the player's name and the board type (player board or computer)
    Has methods for adding ships and guesses and printing the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

    def random_point(self, size):
        """
        Helper function to return a random integer between 0
        and size of the board
        """
        return randint(0, size - 1)


def new_game():
    """
    Starts a new game. Sets the board size and number of ships
    and initialises the boards.
    """

    size = 5
    num_ships = 4
    print("-" * 35)
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    print(player_board.name)
    print(player_board.print())
    print(computer_board.name)
    print(computer_board.print())

    make_guess_player(computer_board)
    validate_coordinates(make_guess_player)


def validate_coordinates(self, x, y, board):
    if (self.board[x] < 0 or self.board[x] > 4) or (y < 0 or y > 4):
        print("coordinates must be between 0 and 4")


def populate_board(board):
    type = board.type
    ship_row = board.random_point(board.size)
    ship_col = board.random_point(board.size)
    board.add_ship(ship_row, ship_col, type)


def make_guess_player(board):
    while True:
        try:
            x = int(input("Guess a row: "))
            y = int(input("Guess a col: "))
        except ValueError:
            print("Sorry, you must enter a number")
        else:
            if (self.board[x] < 0 or self.board[x] > 4) or (y < 0 or y > 4):
                print("coordinates must be between 0 and 4")
                
            board.guess(int(x), int(y),)
            print(board.print())
            print(f"Player guessed: {x}, {y}")
            print(board.guess(x, y))


def play_game(computer_board, player_board):
    return True


new_game()
