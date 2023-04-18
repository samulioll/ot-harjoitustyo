# Arkkitehtuurikuvaus

## Luokkarakenne

```mermaid
    classDiagram
        Engine ..> ViewManager
        Engine: +main()
        ViewManager: +dict allViews
        ViewManager: +View currentView
        ViewManager: +Profile currentProfile
        ViewManager ..> ProfileSelect
        ProfileSelect ..> ProfileMenuLogic
        ProfileSelect: +str nextView
        ViewManager ..> MainMenu
        MainMenu ..> MainMenuLogic
        MainMenu: +str nextView
        ViewManager ..> LevelSelect
        LevelSelect: +str nextView
        LevelSelect ..> LevelSelectLogic
        ViewManager ..> Highscores
        Highscores: +str nextView
        Highscores ..> HighscoresMenuLogic
        ViewManager ..> PostGame
        PostGame: +str nextView
        PostGame ..> PostGameLogic
        ViewManager ..> Game
        Game: +str nextView
        Game: +Levels levels
        Game ..> Board
        Board ..> Car
        Board ..> Levels
```
