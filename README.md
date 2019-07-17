# introAI-project1 A* Algorithm* 
By Tim Raymaker and Michael Rizzo

This Python project demonstrates the Repeat Forward Astar, Repeat Backward Astar, and Adaptive Astar Algorithms. It uses Pygame to display the 101x101 grid worlds.

## Getting Started ##
Start by downloading the repository/zip file. The main file to compile and run is DisplayStar.py. Please use python 3.6 or newer. 

Prequisites for running the DisplayStar.py are provided below. 

### Prerequisites ###
The only non-standard library our project uses is: 

[Pygame](https://www.pygame.org/)

To install this library, there exists a pip install for Pygame.


## How to Use DisplayStar.py ##

In the main pygame window:

Press l to load a map or clear a previous search path by reloading the same map
Press 1 to run Repeat Forward AStar that tie breaks on low g-values 
Press 2 to run Repeat Forward AStar that tie breaks on high g-values
Press 3 to run Repeat Backward AStar that tie breaks on low g-values
Press 4 to run Repeat Backward AStar that tie breaks on high g-values
Press 5 to run Adaptive AStar that tie breaks on high g-values

Key presses must be done in the game window. When pressing L, the user will be prompted in the terminal for which map number to load. Runtime and path length (if one is found) will also be presented in the terminal. 

Projected paths will be displayed in blue and they are only displayed for the first quadrant of the map, after which they stop. This is to improve runtime. Expanded cells are displayed in yellow. The total path is displayed in red. The start state is initially displayed in red and the goal state is initially displayed in green. Blocked cells are in black and unblocked cells are in white. 

## Also Included in the Repo##
