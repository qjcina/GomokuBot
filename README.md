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
## Maps
- **LineMapGenerator**:
Generates map based on horizontal and vertical average brightness. Algorithm:
1. For each vertical line calculate average brightness.
2. Cut off menu and save points, where brighness is very low.
3. For each horizonal line calculate average brightness.
4. Save points where brightness is very low.
5. If middle line is missing calculate it by average of lower and higher line.
6. Get points where lines intersect.
## Menu
- **BrightnessMenuGenerator**:
Calculates menu positions based on average brightness and colors. Algorithm:
1. Cut off board.
2. Estimate start button position.
3. Get average horizontal brightness of whole menu.
4. Estimate seats position.
5. Estimate position of left seat and check its color.
6. Estimate position of right seat and check its color.
7. Move alongside black bar above seats and get players color.
## Bot Logics
- **ZeroDepth**
WIP
# Other bots:
- Petriczi (C#):
https://github.com/petriczi/boty_jebane
