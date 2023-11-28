#!/usr/bin/env python
# coding: utf-8

# In[3]:


## Import libraries
## STEP 1 --> create a class containing relevant variables and functions
    ## class attributes (length and radius because board is not changing)

    ## initialize the object, using default values for iterations (50) and throws (10)
    
    ## STEP 2 --> simulate dart throws
    
    ## dartThrow takes no input, outputs two floats: 
        # x- and y-coordinates for where a random dart landed in a square 2x2 centered at (0,0)
    ## assumes the dart lands inside the square

        ## randomly generate an x- and y-coordinate between -1 and 1

    
    ## STEP 3 --> determine if throws are inside the circle
    
    ## inCircle takes x and y coordinate input, outputs boolean value for "in circle" 
        # determining if dart throw is in a circle (rad 1) centered at (0,0) in the square

        ## using formula from: 

    
    ## STEP 4 --> simulate a number of throws and save results
    
    ## output is a double nested dictionary. outside keys are number of iterations, within each iteration, 
        # keys are the number of throws. the value of the innermost dictionaries is a dictionary of info
        # about each throw, including the x and y coordinate, and whether it made it in the circle
    ## input is a number of iterations and a number of throws (default values from initializing)
        
        ## create an empty dataframe to return at the end
        
        ## loop through iterations based on iteration input

            
            ## for each iteration, create a dictionary to be added to the results at the end

            
            ## within the iteration, "throw" the dart a certain number of times
                
                ## within each throw: 
                
                ## "throw" the dart and record if it made it in the circle
                
                ## add to countervariable if dart "inside" circle

                ## store the dart inforamtion in a dictionary (x and y coords, and if it made it in)
                
                ## add the "throw" dictionary to iteration dictionary, key = throw number

            ## after all throws, append the iteration dictionary to results dataframe

        
        ## after all iterations are over, return the results
    
    
    ## STEP 5 --> math )): estimate pi (like a loser who doesn't know 3.14...) using circle and side lengths
        
        ## go through each iteration of the dataframe

            
            ## count the number of throws
   
            
            ## count the number of times the throw 'landed on the board"
            
            
            ## pi value = ins/throws * 4
            
            
            ## calculate error (distance of pi from actual pi value)
            
            
            ## append the individual pi and error values to their lists


            
    ## STEP 7 --> calculates the standard error of the pi estimates and returns them

        

    
    ## STEP 6 --> create a visualization of a dartboard after all the throws have landed
    
    ## creates a single dartboard using one simulation as input

        
        ## plot a matplotlib figure

        
        ## set the x and y range of the coordinate plane using .set()

        
        ## move the axes so they are centered using .spines().[location].set_position()


        
        ## remove the top and right lines for visualz


        
        ## add the circle to the middle of the plane


        
        ## remove ins from iteration using try to only run it once  

        

        
        
        ## loop through the iteration

            
            ## access the x and y value for each throw
            
            
            ## plot each point using .scatter()

            

    
    ## to plot several simulations on top of each other: 

        
        ## loop through the output of simulation

            
            ## access each simulation and provide it as input to visualization

    

