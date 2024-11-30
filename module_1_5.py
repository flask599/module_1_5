from turtledemo.penrose import start

immutable_var = 1, 2, 3, True, False, 'Здрасте'
print(immutable_var)
#immutable_var [0]= 'Здрасте'
# print(immutable_var) - тип элемента tuple (кортеж) не изменчив, выходит ошибка ('tuple' object does not support item assignment)
mutable_list = ['study','ready','go']
print(mutable_list)
mutable_list.append(1)
mutable_list.extend('apple')
mutable_list[0] = 'start'
mutable_list[1] = 'drive'
mutable_list[2] = 'finish'
mutable_list.remove('finish')
print(mutable_list)

