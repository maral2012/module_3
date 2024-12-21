def print_parms(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [36.6, 37, 35.8]
values_dict = {'a' : 28, 'b' : 32, 'c' : 15}
values_list_2 = ['tip', 49]
print_parms(*values_list_2, 17)
print_parms(*values_list)
print_parms(**values_dict)