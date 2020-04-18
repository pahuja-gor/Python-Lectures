import random
from math import pow
import pandas as pd

number_pairs = []
letter_pairs = []

x = 0
same_count = 0
while x <= pow(9, 2) and same_count <= pow(9, 2):
    firstNum = random.randint(0, 9)
    secondNum = random.randint(0, 9)
    numPair = str(firstNum) + str(secondNum)

    if numPair not in number_pairs:
        number_pairs.append(numPair)
    else:
        same_count += 1
    x += 1

# print("Number Pairs:", number_pairs)
# print(len(number_pairs))

letter_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
           14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
           26: 'z'}
letters = list(letter_dict.values())
y = 0
same_count = 0
# while (y <= pow(26, 10) or same_count <= 1000000):
while (y <= pow(26, 4) and same_count <= pow(26, 4)):
    firstLetterKey = random.randint(0, 25)
    firstLetter = letters[firstLetterKey]

    secondLetterKey = random.randint(0, 25)
    secondLetter = letters[secondLetterKey]

    thirdLetterKey = random.randint(0, 25)
    thirdLetter = letters[thirdLetterKey]

    fourthLetterKey = random.randint(0, 25)
    fourthLetter = letters[fourthLetterKey]

    letter_combo = firstLetter + secondLetter + thirdLetter + fourthLetter

    if letter_combo not in letter_pairs:
        letter_pairs.append(letter_combo)
        # print(str(y), letter_combo)
    # else:
    #     same_count += 1
    #     print("SC:", same_count)
    y += 1

# print("Letter Pairs:", letter_pairs)
# print(len(letter_pairs))

num_letter_combo = []

for num_pair in number_pairs:
    for four_letter_combo in letter_pairs:
        num_letter_combo.append(four_letter_combo + num_pair)
# print("Num/Letter Combos:", num_letter_combo)
# print('\n')

dataframe = pd.DataFrame(num_letter_combo, columns = ["Number/Letter Combinations"])
# dataframe.to_excel('C:/Users/gorpa/Documents/prntCombos.xlsx')
dataframe.to_csv('C:/Users/gorpa/Documents/prntCombos.csv')

with open("combos.txt", "a") as f:
    for combo in num_letter_combo:
        f.write("https://prnt.sc/" + combo)
        f.write('\n')
f.close()

# for combo in num_letter_combo:
#     print("https://prnt.sc/" + combo)
print("Number of Combinations:", len(num_letter_combo))
# print("DONE!!!")