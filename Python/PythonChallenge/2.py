import os

my_file = open(os.path.dirname(__file__)+'/data/twotext.txt', 'r')
count_dict = dict()

cipher_text = my_file.read().strip()

for ch in cipher_text:
    if (ch is not '\n'):
        if (ch is not ''):
            if (ch in count_dict):
                count_dict[str(ch)] += 1
            else:
                count_dict[str(ch)] = 1

for entry in count_dict.items():
    if entry[1] < 5:
        print (entry[0])
