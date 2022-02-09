menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam", "tomato"],
]

# 1 remove spam from each list than print list

for meal in menu:
    for ing in meal[::-1]:
        if ing != 'spam':
            print(ing, end=' ')
    print()


# for index, meal in enumerate(menu):
#     meal_1 = [*menu[index]]
#     for a in meal_1:
#         if a == 'spam':
#             meal_1.remove(a)
#     print(', '.join(meal_1))

#  Method 2 print out item from list as long its not a spam
# for index, meal in enumerate(menu):
#     dish = []
#     dish.extend(meal for meal in [*menu[index]] if meal != 'spam')
#     print(dish)
### Workspace below
#print('this is meal {} with index {}'.format(meal, index))
# meal[index] = ''.join(a for a in [*menu[7]] if a != 'spam').split()
#print(meal_1)

#remove spam from each list & print
##M1##
# for meal in menu:
#     if 'spam' not in meal:
#         print(meal)
#     else:
#         for ing in meal:
#             if ing == 'spam':
#                 meal.remove('spam')
#         if 'spam' in meal:
#             meal.remove('spam')
#         print(meal)

# for meal[ing] in menu:
#     for ing in meal:

# print list of strings as list of numbs