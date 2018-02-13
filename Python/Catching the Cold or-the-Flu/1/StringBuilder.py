import time

word_list = ["Hello ", "there! ", "How ", "are ", "you ", " doing", " today?"]
iterations = 20000

# additive string concatenation
def join_words(words):
    sentence = ''
    for word in words:
        sentence = sentence + word
    return sentence

print (join_words(word_list))
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

print(join_words_using_string_builder_idea(word_list))
start_time = time.time()
for i in range(0, iterations):
    join_words_using_string_builder_idea(word_list)
end_time = time.time()
print ('String Builder Time ' + str(end_time-start_time))
##########################


# I think Python works differently than Java :) 
