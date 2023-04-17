# Rush hour puzzle game

A puzzle game where the goal is to move cars on the board in a way that allows the red car to drive out of the opening on the right side of the board. The game has multiple levels in increasing difficulty. Every player creates their own profile and the game keeps track of each player's progress and high scores in every level.

## Documentation

- [Työaikakirjanpito](https://github.com/samulioll/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/samulioll/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Vaativuusmäärittely](https://github.com/samulioll/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](https://github.com/samulioll/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Current state

!! The game currently only runs in 1200x1200 screen size, but additional resolution options will be made available in the next version. !!

### Profile selection
- A profile can be selected by clicking the "SELECT PROFILE" button and then clicking a profile username.
- A new profile can be created by clicking the "NEW PROFILE" button and then typing a username and submitting it with ENTER.
- A profile can be deleted by clicking the "DELETE PROFILE" button and then clicking the profile to be deleted.
    - In the next version the game will ask for confirmation for the deletion.

### Main menu
- The player can continue playing from the next unsolved level by clicking "CONTINUE".
- The player can go into the level selection menu by clicking "LEVELS".
- Highscores view is currently not finished and is disabled.
- The player can go back to the profile selection menu by clicking "SWITCH USERS".

### Levels menu
- Solved levels will be shown in dark black color, next unsolved level in green and the rest of the unsolved levels in light grey.
- The player can select any already solved level to play, as well as the next unsolved level.
- The player can go back to the main menu by clicking "MAIN MENU".

### Game view
- The player can move cars by dragging them.
- Information shown:
    - Current level
    - Completed moves (if a car is placed into the same square where it started at, no move is counted as completed)
    - Time (NOT YET FUNCTIONAL)
- The player can reset the level by clicking "RESET".
- The player can go back to the main menu by clicking "EXIT".

### Other
- The game will have 50 levels at release, but currently there are only 12.


## Installation

1. Clone the repository to your computer and install the dependencies:
```
poetry install
```
2. Start the program with:
```
poetry run invoke start
```

### Commands

Start the program with:
```
poetry run invoke start
```
Run tests with:
```
poetry run invoke test
```
Get test coverage with:
```
poetry run invoke coverage-report
```
