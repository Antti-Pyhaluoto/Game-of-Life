# Game of Life
Python implementation of Conway's Game of Life.

# Functionality
Starting from randomly generated frame, script follows the rules of the Game of Life until either max number of frames is reached or generations become stale. Each frame is saved as a jpg image that can later be combined into a video with for example FFmpeg.

# Rules:
* Any live cell with fewer than two live neighbors dies, as if by under population.
* Any live cell with two or three live neighbors lives on to the next generation.
* Any live cell with more than three live neighbors dies, as if by overpopulation.
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
