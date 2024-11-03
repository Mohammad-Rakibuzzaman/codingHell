def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    
    Output: ['******', '*    *', '*    *', '*    *', '******']
    """
    # Your code here
    '''
    begin
        box = []
        for i in range(n):
            if (i==0and i == n-1)
                box.append("*" * n)
            box.append(f""*" {" " * n-2}} )
    end
    '''
    box = []
    
    # print(len)
    
    for i in range(n):
        p = n-1
        r = n-2
        if (i == 0 or i == p):
            
            box.append("*" * n)
            
        else:
            
            box.append("*" + " " * r + "*")
        
            
        # box.append(f"'*'{" " * r}'*'")
    
    return box
    
    
    # def generate_hollow_square(n):
    # """
    # Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    # Parameters:
    # n (int): The size of the square.
    
    # Returns:
    # list: A list of strings where each string represents a row of the hollow square.
    # """
    # # Initialize an empty list to store the rows of the hollow square
    # square = []
    
    # # Handle the case when n is 1 separately
    # if n == 1:
    #     return ['*']
    
    # # The first and last rows are full of '*'
    # square.append('*' * n)  # First row
    
    # # For the middle rows, the first and last characters are '*', rest are spaces
    # for i in range(n - 2):
    #     square.append('*' + ' ' * (n - 2) + '*')
    
    # # The last row is also full of '*'
    # square.append('*' * n)  # Last row
    
    # # Return the list of rows
    # return square
    
    

num = int(input())

ansTotal = generate_hollow_square(num)

print(ansTotal) 