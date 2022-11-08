# result = 0
# for i in range(10):
#     if i%2 ==0:
#         result += 1
# print(result)

result = sum(i for i in range(10) if i%2 ==0)
print(result)