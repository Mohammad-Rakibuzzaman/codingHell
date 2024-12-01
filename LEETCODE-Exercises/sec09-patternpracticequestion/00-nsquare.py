def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    '''
    Begin
    input x
    create Function generate_square
    
    
    return n * [n * "*"]    
    
    '''
    
    return n * [n * "*"]    
    
    # sum = []
    
    # for _ in range(n):
    #     sum.append("*" * n)
        
    # return sum

n = int(input())
final_res = generate_square(n)

print(final_res)