# Rush hour puzzle game

A puzzle game where the goal is to move cars on the board in a way that allows the red car to drive out of the opening on the right side of the board. The game has multiple levels in increasing difficulty. Every player creates their own profile and the game keeps track of each player's progress and high scores in every level.

## Documentation

- [Työaikakirjanpito](https://github.com/samulioll/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/samulioll/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Vaativuusmäärittely](https://github.com/samulioll/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](https://github.com/samulioll/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

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
