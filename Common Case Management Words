myfile = open('CM.csv')
counts = dict()

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punc = " "

for line in myfile:
    line = line.rstrip()
    word = line.split()
    for char in word:
        smallword = char.lower()
        counts[smallword] = counts.get(smallword, 0) + 1

from collections import OrderedDict
counts_sorted_by_value = OrderedDict(sorted(counts.items(), key=lambda x: x[1]))
for k, v in counts_sorted_by_value.items():
    print ("%s: %s" % (k, v))
