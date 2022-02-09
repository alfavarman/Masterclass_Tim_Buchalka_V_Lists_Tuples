# list, ENUMERATE, COMPREHENTIONS
offer = ['Round Tour Thailand',
         'International Flight to Thailand',
         'Insurance',
         'Visa FEE',
         'Beach Stay Upgrade **** Hotel',
         'Business Class Upgrade',
         'Optional Tour']
#valid_choices = [str(i) for i in range(1, len(offer) +1)] #comprehentions
valid_choices = []
for i in range(1, len(offer) + 1):
    valid_choices.append(str(i))

#print(valid_choices)
choice = "-"
schopping_chart = []

while choice != '0':
    if choice in valid_choices:
        print('Selected Item: \n{} <- added to CHART'.format(offer[int(choice) - 1]))
        schopping_chart.append(offer[int(choice) - 1])
    else:
        print('Please Select Items to purchase:')
        #for position in offer:
        #    print('{0}: {1}'.format(offer.index(position) + 1, position))
        for index, position in enumerate(offer):
            print('{}: {}'.format(index + 1, position))
        print('0. Exit')
        print('Please Select Items to purchase:')
    choice = input()
print('Shopping chart: \n{}'.format(schopping_chart))
print('Bon Voyage')
