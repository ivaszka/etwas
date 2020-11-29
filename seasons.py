# зад.1, вар.4 По номеру месяца напечатать пору года
a = (input('Enter a number of any month :\n'))
# print(type(a))
if a == '12' or a == '1' or a == '2':
    print('It is Winter!')
elif a == '3' or a == '4' or a == '5':
    print('It is Spring!')
elif a == '6' or a == '7' or a == '8':
    print('It is Summer!')
elif a == '9' or a == '10' or a == '11':
    print('It is Autumn!')
else:
    print('There is no such month in the year :(')
