import builtins


def my_sum(*args, **kwargs):
    globals()['sum'] = my_sum
    return "This is my custom sum!"


numbers = [1, 2, 3]

print("The result of a built-in function 'sum':", sum(numbers))
print("The result of a custom function 'my_sum':", my_sum(numbers))
print("The result of an already overlapped function 'sum':", sum(numbers))
print("The result of calling the original function 'sum' using the built-in module 'builtins':", builtins.sum(numbers))
