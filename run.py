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


def populate_board(board):
    """
    Board to be populated with ships at random points
    """
    type = board.type
    ship_row = board.random_point(board.size)
    ship_col = board.random_point(board.size)
    board.add_ship(ship_row, ship_col, type)


def make_guess_player(board):
    """
    Ask player to guess a row and a column on the board
    If number is lower than 0 or larger than 4, error message will appear
    If number is not an integer message to appear prompting user to
    input a number
    Add the players guesses to the board with the guess function
    """
    while True:
        try:
            x = int(input("Guess a row:\n "))
            y = int(input("Guess a col:\n "))
        except ValueError:
            print("Sorry, you must enter a number")
            continue
        if x not in range(0, 4) or y not in range(0, 4):
            print("\nThe numbers must be between 1-4!")
        else:
            board.guess(int(x), int(y),)
            print(board.print())
            print(f"Player guessed: {x}, {y}")
            print(board.guess(x, y))


def play_game(computer_board, player_board):
    return True


new_game()
