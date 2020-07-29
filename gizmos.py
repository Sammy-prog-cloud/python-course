print('''   Gizmos and Widgets weights
                                        '''.upper())
widgets = 75
gizmos = 112
widgets_number = int(input('Please enter in Number of widgets >>> '))
gizmos_number = int(input('Please enter in Number of gizmos >>> '))
total_weight_of_order = widgets * widgets_number + gizmos * gizmos_number
print('The total weight of both is %.f(grams)' % total_weight_of_order)
