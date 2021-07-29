
Ultimate Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users can try and beat the computer by finding all of the computer's battleships before the computer finds theirs. Each 
battleship occupies one square on the board.

Here is the live version of my project <a href ="https://aoibhinnbattleship.herokuapp.com/" 

## How to play

Ultimate Battleships is based on the classic pen-and-paper game.

In this version, the player enters their name and two boards are randomly generated.

The player can see where their ships are, indicated by an @ sign, but cannot see where the computer's ships are. 

Guesses are marked on the board with an X. Hits are indicated by *.

The player and the computer then take turns to make guesses and try to sing each other's battleships. 

The winner is the player who sinks all of their opponent's battleships is first. 

## Features

Existing Features

- Random board generation
- Ships are randomly placed on both the player and computer boards
- The player cannot see where the computer's ships are

- Play against the computer
- Accepts user input

- Input validation and error checking
- You cannot enter coordinates outside the size of the grid
- You must enter numbers


## Data Model
The game creates two instances of the Board class to hold the player's and computer's board. 

The Board class stores the board size, the number of ships, the position of the ships, the guesses against that board and details such as board type (player's board or computer) and the player's name.

The class also has methods to help play the game, such as a print method to print out the current board, an add_ships method to add ships to the board and an add_guess method to add a guess and return the result. 

## Testing
I have manually tested the project by doing the following: 
- Passed the code through a PEP8 linter and confirmed there are no problems. 
- Given invalid inputs: strings when numbers are expected and out of bounds input. 
- Tested in my local terminal and the Code Institute Heroku terminal. 

## Remaining Bugs
- Computer board does not appear when the player inputs their first guess row and column. Only the player can continue to guess against the computer board.
- Game allows the user to input the same coordinates twice.
- Game doesn't end or give the player the option to play again.

## Validator Testing
PEP8
- No errors were returned from PEP8online.com

## Deployment
The project was deployed using Code Institute's mock terminal for Heroku. 

Steps for deployment: 
- Fork or clone this repository
- Create a new Heroku app
- Set the Buildbacks to Python and NodeJS in that order 
- Link the Heroku app to the repository 
- Click on Deploy

## Credits
- Code Institute for the deployment terminal 
- Code Institute for inspiration for the game
- Wikipedia for details of the Battleships game