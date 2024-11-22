

def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here

    """
    begin
    
    take input
    
    make box list
    
    now loop and get the each number 
    
    now think about how to get each numbers for each line
    
    end
    
    """
    box = []
    k = 0
    for i in range(1, n+1):
        
    
        for j in range(k, i):
            box.append(j)
            k += 1
            
            
    return box



enterNum = int(input())
answerProb = generate_floyds_triangle(enterNum)
print(answerProb)