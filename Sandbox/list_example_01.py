a = [1, 4, 2, 9, 10, 3]
b = [2 * element for element in a]
print(b)

c = [2 * element for element in a if element % 2 ==1]
print(c)

d = [[1,2,3], [4,5,6],[7,8,9]]
for row in d:
    print(row[0])
    
for row in d:
    for element in row:
        print(element)
        
for i in range(3):
    print(d[i][i])
    
for i in range(3):
    print(f'The {i+1}-th diagonal element is: {d[i][i]}')
