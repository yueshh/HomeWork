data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    sum = 0
    # dict
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)
    # lists
    elif isinstance(data_structure, (list, set, tuple)):
        for item in data_structure:
            sum += calculate_structure_sum(item)
    # int
    elif isinstance(data_structure, (int, float)):
        sum += data_structure
    #str
    elif isinstance(data_structure, str):
        sum += len(data_structure)
    return sum

result = calculate_structure_sum(data_structure)
print(result)
