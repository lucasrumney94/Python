def string_permutation_check(strings_to_compare):
    character_counts = dict()
    for my_string in strings_to_compare:
        character_counts[my_string] = dict()

        for character in my_string:
            if character in character_counts[my_string].keys():
                character_counts[my_string][character]+=1
            else:
                character_counts[my_string][character]=1

    for count in character_counts:
        if count == character_counts[strings_to_compare[0]]:
            continue
        else:
            return False
    return True




test_strings = [
                ["Hello","olleH"],
                ["NoNo", "YesYes"],
                ["ABC", "ABBC"]
                ]

for pair in test_strings:
    print('{} and {} are Permutations: {}'.format(pair[0], pair[1], string_permutation_check(pair)))
