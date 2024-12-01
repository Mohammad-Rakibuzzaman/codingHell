def generate_floyds_triangle(n):

    box = []
    k = 1
    for i in range(1, n + 1):

        # for j in range(k, k + i):
        #     box.append(j)
        #     k += 1
        row = " ".join(str(k + j) for j in range(i))
        box.append(row)
        k += i
    return box


enterNum = int(input())
answerProb = generate_floyds_triangle(enterNum)
print(answerProb)
