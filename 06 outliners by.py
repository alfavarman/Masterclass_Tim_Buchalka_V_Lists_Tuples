#102-112 removing repeat
data = [1, 2.3, 99, 100, 133, 189, 101, 103, 5, 122, 179, 164, 188, 200, 201]

min_value = 100
max_value = 200

# method 1
# for index in range(len(data) -1, -1, -1):
#     if data[index] < min_value or data[index] > max_value:
#         print(index, data)
#         del data[index]
# print(data)

index_1 = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_value or value > max_value:
        print(index, value)
        del data[index_1 - index]

print(data)
