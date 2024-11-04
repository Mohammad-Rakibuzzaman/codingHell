def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    '''
    input: 3
    begin

        box = []
        for i in n:
            box.append("*" * i)
        
    end
    outout :  *
             ***
            *****
    '''    
    # box = []
    
    # r = 2 * n - 1
    # p = n-1
    
    # # print(r)
    # for i in range(1, r + 1):  
    #     if (i%2 != 0):       
    #         for j in range(p, -1, -1):
                
    #             box.append(j * " " + i * "*")
    #             continue
    # return box
    
    box = []
    
    
    for i in range(1, n+1):
       
        countStars = "*" * (2 * i - 1)
        spaceCount = " " *  (n - i)
        box.append(spaceCount + countStars + spaceCount)
        
    return box
    
    
    

n = int(input())
probSol = generate_pyramid(n)
print(probSol)