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
    
    take an empty list box = []
    
    use a for loop
    inside of it use another loop 
    
    
    
    
    end
    
    """
    # box = []
    
    # currentNum = 1
    
    # for i in range(1, n+1):
    #     # print(i)
    #     row = ' '.join(str(currentNum + j) for j in range(i))
    #     box.append(row)
    #     currentNum += i
              
    # return box
    
    # box = []
    # currentNum = 1
    
    # for i in range(1, n + 1):
    #     row = ""
    #     for j in range(i):
    #         row += str(currentNum) + " "
    #         currentNum += 1
    #     box.append(row.strip())  # Remove the trailing space
    
    # return box
    
    # Generate all required numbers in advance
    numbers = [str(i) for i in range(1, n * (n + 1) // 2 + 1)]
    box = []
    start = 0
    
    for i in range(1, n + 1):
        end = start + i
        box.append(" ".join(numbers[start:end]))
        start = end
    
    return box

    
    
    
    
n = int(input())
probSolve = generate_floyds_triangle(n)
print(probSolve)