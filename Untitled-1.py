def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def change_direction(n):
    return n * -1

numbers = [1, -2, 10.67]

apply_to_each(numbers, change_direction)
print(numbers)
