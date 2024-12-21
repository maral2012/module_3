def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(5, 'ddder')
print_params( 7,None, False)
print_params(26)
print_params()
print_params(b=25)
print('Функция print_params(b=25) работает')
print_params(c = [1,2,3])
print('Функция print_params(c = [1,2,3]) работает')
values_list = [125, None, 'Текст']
values_dict = {'a':3.14, 'b':"Пи", 'c':False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['Тополь -', 38]
print_params(*values_list_2, 42)
print('Функция print_params(*values_list_2, 42) работает')