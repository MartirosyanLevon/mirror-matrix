a = []
n = int(input('Enter a numbre: '))    # row & column


for i in range(n):                    # Create the matrix  
       a.append([0] * n)              


for i in range(n):                    #  Chechk index and fill our value's
    for j in range(n):
        if i == j:
            a[i][j] = 1
        elif i > j:
            a[i][j] = 0
        else:
            a[i][j] = 0


for i in a:                            # Show the Matrix
    print(i)
