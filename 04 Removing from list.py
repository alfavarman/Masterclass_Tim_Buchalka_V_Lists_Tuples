data = [2, 3.4, 45, 101, 103, 122, 179, 164, 188, 307, 399]

min_value = 100
max_value = 200

slice_1 = 0

for index, value in enumerate(data):
    if value >= min_value:
        slice_1 = index
        break
#print(slice_1) #TODO for debugging
del data[:slice_1]
#print(data)
for index, value in enumerate(data):
    if value >= max_value:
        slice_1 = index
        break
del data[slice_1:]
print(data)