def print_params(a = 1, b = 'строка', c = True):
  if a == None and b == None and c == None:
      print()
  elif b == None and c == None:
      print(a)
  elif a == None and c == None:
      print(b)
  elif a == None and b == None:
      print(c)
  elif a == None:
      print(b, c)
  elif b == None:
      print(a, c)
  elif c == None:
      print(a,b)
  else:
    print(a,b,c)

print_params()
print_params(a=None, b=None, c=None)
print_params(a=True, b=None, c=12.3)
print_params(a=None, b=10, c=None)

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, True, 'Hi']
values_dict = {'a': 5, 'b': False, 'c': 'Bye'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [25.5, False]
print_params(5, *values_list_2)
