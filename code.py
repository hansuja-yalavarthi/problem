"""
ID: hansuja1
LANG: PYTHON3
PROG: gift1 
"""
#opening the file, reading and storing it's content
from asyncore import write

file = open('/Users/hansujayalavarthi/Downloads/USACO programs/challenge1-2-2/input.txt', 'r')
content = file.readlines()

#storing the first line (the number of NPs) as a string first, and then an int
lin1 = content[0] # string form of 5
firstLine = int(lin1) # integer form of 5

#storing the names of the people as an array
temppeople = content[1 : firstLine+1]

#people array
people = []
for i in range(0, len(temppeople)):
    people.append(temppeople[i].strip())

#storing the balances as firstLine number of 0s
balance = []
for i in range(0, firstLine):
    balance.append(0)

#adding people and balance into one array to make it two dimensional
peopleAndBalance = [people, balance] # [['dave\n', 'laura\n', 'owen\n', 'vick\n', 'amr\n'], [0, 0, 0, 0, 0]]

#showing who the giver is and how much they gave
person1 = content[firstLine + 1] # dave
giver1 = content[firstLine + 2] # 200 3
giverOne = giver1.split() # ['200', '3']
giverOneAmount = int(giverOne[0]) # 200
giverOnePpl = int(giverOne[1]) # 3
person2 = content[firstLine + 3 + giverOnePpl] # owen
giver2 = content[firstLine + 4 + giverOnePpl] # 200 3
giverTwo = giver2.split() # ['200', '3']
giverTwoAmount = giverTwo[0]
giverTwoPpl = giverTwo[1]

for x in range(firstLine):
    outputp1 = "{fname} {balance}".format(fname = peopleAndBalance[0][x], balance = peopleAndBalance[1][x])
    #outputp1 = peopleAndBalance[0][x]
    print(outputp1)