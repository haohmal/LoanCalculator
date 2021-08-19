# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
min_value = None
min_key = ""
max_key = ""
max_value = None
for key, value in test_dict.items():
    if min_value is None or min_value > value:
        min_value = value
        min_key = key
    elif max_value is None or max_value < value:
        max_value = value
        max_key = key

print("min: {}".format(min_key))
print("max: {}".format(max_key))