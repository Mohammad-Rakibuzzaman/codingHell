def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    '''
    begin
        input n
        
        box = []
        i=1
        for i in range n
            appnd(i * *) 
    
    
    end
    
    '''
    
    # box = []

    # for i in range(1, n + 1):
    #     box.append(i * "*")
        
    # return box
    
    return [i * "*" for i in range(1, n+1)]

n = int(input())
solProb = generate_triangle(n)

print(solProb)