

source = [1, 100, 133, 189, 101, 103, 122, 179, 164, 188, 200, 201]
data = sorted(source)

min_value = 100
max_value = 200

slice_1 = 0
slice_2 = 0

for index, value in enumerate(data):
    if value >= min_value:
        slice_1 = index
        break
#print(slice_1) #TODO for debugging
del data[:slice_1]
#print(data)
for index, value in enumerate(data):
    if value > max_value:
        slice_1 = index
        break
del data[slice_1:]
print(data)