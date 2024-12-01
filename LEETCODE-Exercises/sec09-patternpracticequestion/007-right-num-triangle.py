def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    """
    begin
    
    first take the input n
    take a list
    range loop for first 1 to n + 1
    
    
    end
    """
    box = []
    
    for i in range(1, n+1):
        
        # box.append(f"{i}") 
        box.append(i * str(i))    
    
    
    return box


n = int(input())
probSol = generate_number_triangle(n)
print(probSol)