# elementary hash table
array = [[], [], [], [], []]

def convert_to_numbers(input_string):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    output_list = []

    for letter in input_string:
        output_list.append(alphabet.index(letter))

    return output_list


def hash(string):
    hash_list = convert_to_numbers(string)
    return sum(hash_list) % 5


def insert(array, key, value):
    bucket_index = hash(key)
    array[bucket_index].append((key, value))


def find(array, key):
    bucket_index = hash(key)
    for pair in array[bucket_index]:
        if pair[0] == key:
            return pair[1]


alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(array, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(array, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value