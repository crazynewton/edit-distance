s1 = input("First string: ")
s2 = input("Second string: ")

def editDistance(s1, s2):
    m, n = len(s1), len(s2)

    d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j-1], d[i-1][j], d[i][j-1]) + 1
                
    return d[m][n]

print(editDistance(s1, s2))