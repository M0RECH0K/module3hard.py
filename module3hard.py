data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(summa):
    storage = 0
    for number in summa:
        if isinstance(number, list | tuple | set):
            storage += calculate_structure_sum(number)
        if isinstance(number, dict):
            for i in number:
                storage += len(i)
            storage += sum(number.values())
        if isinstance(number, int):
            storage += number
        if isinstance(number, str):
            storage += len(number)

    return storage


result = calculate_structure_sum(data_structure)
print(result)


