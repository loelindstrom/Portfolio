**(TurtleWorld) A class that keeps track of everything**  

Initiation:  
- create the window where the graphics can take place
- create the turtles
- create TurtleArray which keeps track of everything


Functions:
- Something that can convert what happens in the pixel to a corresponding numpy-array with either 1 or 0 so that it easily can be used for training a neural network.
- Something that updates everything in discrete time steps?
- Something that can load games?

**(TurtleArray) A class with modified list that contains the world.**
<br>The class is a 2x2 array, each spot holding the turtle responsible for each particular pixel. For indexing the turtles  
Needs to receive arguments:  
-Size of array (rows, columns)  
  
  
Functions:
- Inherits list()
- Function that access each turtle

**(PixelTurtle) A class with modified turtle**  
A class with functions that can perform the necessary on- and off-turning of the pixels.  
Needs to receive arguments:  
-size of pixel  
  
Functions:

- Inherits turtle.Turtle()
- _init_ which creates the pixel from the given size
  - Also needs to hide the turtle
- function that fills the pixel/square with color
- function that unfills the pixel