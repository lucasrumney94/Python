TestStrings = ['Hello World!',
                'quick lazy dog',
                'ABC',
                'DEFGHIJKL',
                'A B B A',
                '  B'
               ]

def unique_characters(string_to_check, whitespace_sensitive):
    if string_to_check is '':
        print ('Input String is empty!')
        return

    string_to_check = string_to_check.lower()

    character_collector = dict()
    if whitespace_sensitive:
        for character in string_to_check:
            if character in character_collector.keys():
                return False
            else:
                character_collector[character] = True

        return True
    else:
        for character in string_to_check:
            if character is not ' ':
                if character in character_collector.keys():
                    return False
                else:
                    character_collector[character] = True

        return True


print ('verify empty input case')
unique_characters('', whitespace_sensitive=False)

print ('{}'.format('#'*50))

for ts in TestStrings:
    print ('Without Whitespace Sensitivity')
    print ('String is "{}", and it is {} that it has only unique characters'.format(ts, unique_characters(ts, whitespace_sensitive=False)))
    print('')
    print ('With Whitespace Sensitivity')
    print ('String is "{}", and it is {} that it has only unique characters'.format(ts, unique_characters(ts, whitespace_sensitive=True)))
    print ('{}'.format('#'*50))
