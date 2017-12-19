num_lines = 0
my_first_file = open('data/threetext.txt', 'r')
for line in my_first_file:
    num_lines += 1

print (num_lines)

my_first_file.close()

my_file = open('data/threetext.txt', 'r')

capture = ''

for i in range(0, num_lines):
    cipher_text = my_file.readline().strip()

    for j in range(4, len(cipher_text)-4):
        if ord(cipher_text[j]) > 96:
            if ord(cipher_text[j-1]) < 96:
                if ord(cipher_text[j-2]) < 96:
                    if ord(cipher_text[j-3]) < 96:
                        if ord(cipher_text[j+1]) < 96:
                            if ord(cipher_text[j+2]) < 96:
                                if ord(cipher_text[j+3]) < 96:
                                    if ord(cipher_text[j+4]) > 96:
                                        if ord(cipher_text[j-4]) > 96:
                                            capture += cipher_text[j]

or_do_this_and_save_typing = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"

print (capture)
