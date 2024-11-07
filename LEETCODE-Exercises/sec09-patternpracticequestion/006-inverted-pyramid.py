def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here

    '''
    begin
    
    first take input
    
    split the process into 2 parts 
    
    spaceCount =  
    starCount = 2n-1
    
    
    
    
    main part should have(spacecount + startcout + spacecount)
    
    end
    
    
    '''

    box = []
    
    
    
    for i in range(n, 0, -1):
        starCount = (2 * i - 1) * "*"
        spaceCount = " " * (n - i)
        box.append(spaceCount + starCount + spaceCount)
        
    return box
    # pyramid = []
    
    # # Loop through each row from 1 to n
    # for i in range(1, n + 1):
    #     # Number of stars in the current row is 2 * (n - i + 1) - 1
    #     stars = '*' * (2 * (n - i + 1) - 1)
    #     # Number of leading spaces to center the stars is i - 1
    #     spaces = ' ' * (i - 1)
    #     # Add the centered row to the list
    #     pyramid.append(spaces + stars + spaces)
    
    # # Return the list of pyramid rows
    # return pyramid        
    

n = int(input())

probSol = generate_inverted_pyramid(n)

print(probSol)