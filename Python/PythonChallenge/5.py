import pickle

#data = open('data/fivetext.', 'r')

unpickled_data = pickle.load(open('data/fivetext.p', 'rb'))
print(unpickled_data)

for i in unpickled_data:
    my_string = ''
    for j in i:
        for k in range(0, j[1]):
            my_string += j[0]
    print my_string
