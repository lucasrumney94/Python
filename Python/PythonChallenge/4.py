

import re
#import urllib
from urllib.request import urlopen
# First nothing page



next_nothing = "12345"
for i in range(0, 400):
    response = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(next_nothing))

    html = str(response.read())
    number = re.search("next nothing is (\d+)", html)
    if number is not None:
        next_nothing = number.group(1)
        print (html + "                 " + number.group(1))
    else:
        print (html)
    if next_nothing == "16044":
        next_nothing = "8022"
