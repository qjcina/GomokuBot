# GomokuBot
GomokuBot is Python bot that can play Gomoku at http://kurnik.pl. Object-oriented model provides ability to modify robot to play Gomoku from other sources.

# Class register
All classes and their functionalities are listed below:
- WindowGrabber:
  Allows user to select screen region for robot preparation.
- InputReader:
  Simple class allowing reading user input from keyboard.
- ImagePreprocessor:
  Prepares necessary variables and assets for robot to work.
- BotMain:
  Contains main robot loop.
# Algorithms
- **LineMapGenerator**:
Generates map based on vertical and horizontal line detection.
![LineMapGenerator](https://i.imgur.com/8VEE40N.png)
Average lightness is lower when vertical line appears. This graph also lets you easily separate menu.
