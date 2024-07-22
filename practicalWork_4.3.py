import re
import math
letters_LV = list()
letters_ENG = list()
stats_LV = dict()
stats_ENG = dict()

input_LV = input("Enter a file(LV) name: ")
input_ENG = input("Enter a file(ENG) name: ")
fileHandle_LV = open(input_LV, encoding = "utf-8")
fileHandle_ENG = open(input_ENG)

# This 'for' cycle converts each line of the given file to a lower case letters, then iterates through each
# line and compares every character to the latin alphabet letters and if it is a match then adds it to the
# 'letters_LV' list.
for line in fileHandle_LV:
    text_LV = line.lower()
    for char in text_LV:
        letter_LV = re.findall("[a-z]", char)
        if char in letter_LV:
            letters_LV.append(char)
# This 'for' cycle makes a dictionary of letters, where 'key' is a letter and 'value' is a number of times a 
# letter appears in the text
for letter in letters_LV:
    if letter not in stats_LV:
        stats_LV[letter] = 1
    else:
        stats_LV[letter] = stats_LV[letter] + 1
totalCount_LV = len(letters_LV)
# This 'for' cycle changes the 'value' of dictionary from number of times a letter appears in the text to the 
# percentage of appearances
for letter in stats_LV:
    stats_LV[letter] = round((stats_LV[letter] / totalCount_LV * 100), 1)
result_LV = list()
# This 'for' cycle adds the letters and their respective percentages in a new list and sorts them by the 
# percentages in a descending order
for letter, count in stats_LV.items():
    result_LV.append((count, letter))
result_LV = sorted(result_LV, reverse=True)

# Same procedure just for the text in english
for line in fileHandle_ENG:
    text_ENG = line.lower()
    for char in text_ENG:
        letter_ENG = re.findall("[a-z]", char)
        if char in letter_ENG:
            letters_ENG.append(char)
for letter in letters_ENG:
    if letter not in stats_ENG:
        stats_ENG[letter] = 1
    else:
        stats_ENG[letter] = stats_ENG[letter] + 1
totalCount_ENG = len(letters_ENG)
for letter in stats_ENG:
    stats_ENG[letter] = round((stats_ENG[letter] / totalCount_ENG * 100), 1)
result_ENG = list()
for letter, count in stats_ENG.items():
    result_ENG.append((count, letter))
result_ENG = sorted(result_ENG, reverse=True)

print("")
# Prints out two columns of letter usage frequency in latvian and english texts
print(f"{'English:' :<12} Latvian:")
for i in range(len(result_ENG)):
    try:
        part_ENG = result_ENG[i]
        part_LV = result_LV[i]
        print(part_ENG[1] + ":", str(part_ENG[0]) + "%" , (part_LV[1] + ":").rjust(7) , str(part_LV[0]) + "%")
    except:
        print(part_ENG[1] + ":", str(part_ENG[0]) + "%")