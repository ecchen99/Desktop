'Write a program to read through the mbox-short.txt and'
'figure out who has the sent the greatest number of mail messages.'
'The program looks for 'From ' lines and takes the second word of those'
'lines as the person who sent the mail. The program creates a Python dictionary'
'that maps the senders mail address to a count of the number of times they appear in'
'the file. After the dictionary is produced,'
'the program reads through the dictionary using a maximum loop to find the most prolific committer'

fname = input("Enter file name: ")
emaillist = open(fname)
counts = dict()

for line in emaillist:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    else:
        words = line.split()
    if len(words[0]) == 4:
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
bigcount = None
bigword = None
for address,count in counts.items():
    if bigcount is None or counts[address] > bigcount:
        bigword = address
        bigcount = counts[address]

print(bigword, bigcount)
