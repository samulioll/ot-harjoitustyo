# Arkkitehtuurikuvaus

## Luokkarakenne

```mermaid
    classDiagram
        Engine ..> ViewManager
        Engine: +main()
        ViewManager: +View currentView
        ViewManager: +Profile currentProfile
        ViewManager ..> ProfileSelect
        ProfileSelect ..> Menus
        ViewManager ..> MainMenu
        MainMenu ..> Menus
        ViewManager ..> LevelSelect
        LevelSelect ..> Menus
        ViewManager ..> Highscores
        Highscores ..> Menus
        ViewManager ..> PostGame
        PostGame ..> Menus
        ViewManager ..> Game
        Game: +Levels levels
        Game ..> Board
        Board ..> Car
        Board ..> Levels
```
