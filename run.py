# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from time import time  # to record the time

#  Now to calculate the accuracy of input prompt
def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(in)):
        if i in (0, len(inwords)-1):
            if i in inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else :
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors