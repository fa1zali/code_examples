# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix  is shown below:
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal 1 + 5 + 9 = 15. The right to left diagonal 3 + 5 + 9 = 17. Their absolute difference |15 - 17| is 2.
# Sample Input:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Output : 15

def diagonalDifference(arr):
    outer = len(arr)
    inner = len(arr[0])
    diagonal1 = 0
    diagonal2 = 0
    for i in range(outer):
        for j in range(inner):
            if i == j:
                diagonal1 += arr[i][j]

    for i in range(outer):
        for j in range(inner):
            if i + j == outer-1:
                diagonal2 += arr[i][j]
    
    if diagonal1 > diagonal2:
        print(diagonal1 - diagonal2)
    else:
        print(diagonal2 - diagonal1)

if __name__ == '__main__':
    arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
    diagonalDifference(arr)