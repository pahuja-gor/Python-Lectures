# # Load words_alpha text file data
# wordList = []
#
# with open('words_alpha.txt') as wordFile:
#     for line in wordFile:
#         wordList.append(line.rstrip('\n'))
#
# # Dictionary counting pattern for first letter of word
# counts = {}
# for item in wordList:
#     firstChar = item[0]
#
#     if firstChar in counts:
#         counts[firstChar] = counts[firstChar] + 1
#     else:
#         counts[firstChar] = 1
#
# orderedKeys = list(counts.keys())
# orderedKeys.sort()
#
# print(orderedKeys)
#
# for key in orderedKeys:
#     print(key, counts[key])
#
# # Dictionary counting pattern for all characters
# counts = {}
# for item in wordList:
#     for char in item:
#
#         if char in counts:
#             counts[char] = counts[char] + 1
#         else:
#             counts[char] = 1
#
# orderedKeys = list(counts.keys())
# orderedKeys.sort()
#
# print(orderedKeys)
#
# for key in orderedKeys:
#     print(key, counts[key])
#
# # Moby Dick word frequency
# with open('mobydick.txt') as wordFile:
#     for line in wordFile:
#         wordList.append(line.rstrip('\n'))
#
# counts = {}
# punctuation = [",", ".", ";", ":"]
#
# for line in wordList:
#     words = line.split(" ")
#
#     for word in words:
#         word = word.lower()
#
#         for char in word:
#             if char is punctuation:
#                 location = word.find(char)
#                 word = word[:location] + word[location + 1:]
#
#         if word.isalpha():
#
#             if word in counts:
#                 counts[word] = counts[word] + 1
#             else:
#                 counts[word] = 1
#
# orderedKeys = list(counts.keys())
# orderedKeys.sort()
#
# print(orderedKeys)
#
# for key in orderedKeys:
#     print(key, counts[key])
#
# # Moby Dick mapping frequency to work
# frequencies = {}
#
# for key in counts.keys():
#     newKey = counts[key]
#     newValue = key
#     frequencies[newKey] = newValue
#
# orderedKeys = list(frequencies.keys())
# orderedKeys.sort()
#
# for key in orderedKeys:
#     print(key, frequencies[key])


# alreadyKnown = {0: 0, 1: 1}
#
# def fibonacci(fiboNumber):
#     # #base
#     # if fiboNumber < 2:
#     #     return fiboNumber
#     #
#     # #recursive
#     # else:
#     #     return fibonacci(fiboNumber - 1) + fibonacci(fiboNumber - 2)
#
#     if fiboNumber not in alreadyKnown:
#         new_value = fibonacci(fiboNumber - 1) + fibonacci(fiboNumber - 2)
#         alreadyKnown[fiboNumber] = new_value
#     return alreadyKnown[fiboNumber]
#
# print(fibonacci(30))

matrix_list = [[0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0],
               [0, 2, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 3, 0]]

matrix_dict = {
    (0, 3): 1,
    (2, 1): 2,
    (4, 3): 3
}
print(matrix_dict[(0, 3)])
matrix_dict.get((2, 3), "no data found")
