def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
def print_params1(**kwargs):
    print(kwargs)


values_list = [True, 45, 'stroke']
values_list_2 = [1, 'у']
values_dict = {'a': 24,
               'b': True,
               'c': "Ы"}

print_params()
print_params(b = 25, c = [1,2,3])
print_params(a=True)
print_params(*[0, 2, 1])
print_params(**values_dict)
print_params(*values_list)
print_params(*values_list_2, 42)
print_params1(**values_dict)
