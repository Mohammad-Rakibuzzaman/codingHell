def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    # Your code here
    '''
    Begin

        take input n = rows or num of rows in list, 
        m = columns or number of symbol
        box = []
        
        for i in n
            append m * '*'
                
                
        return box
    
    End    
    '''
    box = []
    
    for i in range(n):
        
        box.append("*" * m) 
            
    return box         
    

n = int(input("n = "))
m = int(input("m = "))

solProb = generate_rectangle(n, m)
print(solProb)
