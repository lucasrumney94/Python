import time


iterations = 100
word_list = ["Hello ", "there! ", "How ", "are ", "you ", " doing", " today?"]

with open('freebsddictionary.txt', 'r') as file_object:
    for line in file_object:
        word_list.append(file_object.readline())


# additive string concatenation
def join_words(words):
    sentence = ''
    for word in words:
        sentence = sentence + word
    return sentence

start_time = time.time()
for i in range(0, iterations):
    join_words(word_list)
end_time = time.time()
print ('Normal Concatenation Time ' + str(end_time-start_time))
##########################

# String builder function
def join_words_using_string_builder_idea(words):
    sentence = []
    for word in words:
        sentence.append(word)
    return ''.join(sentence)

start_time = time.time()
for i in range(0, iterations):
    join_words_using_string_builder_idea(word_list)
end_time = time.time()
print ('String Builder Time ' + str(end_time-start_time))
##########################
<<<<<<< HEAD
=======


# I think Python works differently than Java :) 
>>>>>>> 786116a4a3360cc80164907f3b52755bad2888e2
