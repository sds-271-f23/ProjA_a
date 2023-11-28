# sds271-F23-group6

prompt: Write a class that does the following uses a Monte Carlo simulation to calculate $\pi$ using the ratio of areas for a square of side length 2 and a circle of radius 1. 

Remember that:

$A_c= \pi R^2$
$A_s=L^2 = (2R)^2$

Your class should:

1. store the length, radius, number of monte carlo iterations, and number of dart throws as internal attributes (you can choose between class and instance attributes as you see fit)
2. simulate some large (but variable) number of dart throws inside the square
3. calculate how many of those throws also landed inside the circle if the circle is centered in the middle of the square
4. store the results of each experiment (set of dart throws) in a dataframe
5. use the relationship between the area of a circle and the area of a square to estimate pi from those two numbers (with error!)
6. create a visualization of the simulation (the dart throws on the circle/square)
7. return the estimate of pi along with the standard error on that estimation

We wrote our dartboard class within our jupyter notebook, but if you're interested in importing it, it's stored in the dartboard class.py document. 

We've broken down the class by the steps of the prompt that each function solves, and thoroughly commented to describe how we did what we did. 