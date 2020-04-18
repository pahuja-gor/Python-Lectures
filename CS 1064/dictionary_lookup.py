import time

def load_words():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds the word with a different fake
    definition into both a list and a dictionary
    '''
    with open('words_alpha.txt') as word_file:
        word_list = []
        word_dictionary = {}
        counter = 0
        
        for line in word_file:
            word_list.append([line.rstrip('\n'), ('fake definition'+str(counter))])
            word_dictionary[line.rstrip('\n')] = ('fake definition'+str(counter))        
            counter += 1

    print("  First word: {}".format(word_list[0]))
    print("  Middle word: {}".format(word_list[int(len(word_list)/2)]))
    print("  Last word: {}".format(word_list[-1]))

    return (word_list, word_dictionary)

def timing_trial(word_to_find, word_list, word_dictionary, n_lookups):
    '''
    Given a word to search for, this function will look inside
    both the list and dictionary to check for its existence,
    timing the lookup time.

    In case lookup time is small, specify larger n_lookups
    '''
    
    # List timing
    list_start_time = time.time_ns()
    for i in range(n_lookups):
      wordInList = False
      for word, defn in word_list:
          if word == word_to_find:
              # Found it! Stop searching in this lap.
              wordInList = True
              break
    list_end_time = time.time_ns()
    list_total_time = (list_end_time - list_start_time) / 1000000000
    
    # Dictionary timing
    dict_start_time = time.time_ns()
    for i in range(n_lookups):
      wordInList = False
      if word_to_find in word_dictionary:
        wordInList = True
    dict_end_time = time.time_ns()
    dict_total_time = (dict_end_time - dict_start_time) / 1000000000

    return (list_total_time, dict_total_time)


if __name__ == '__main__':
    print("Building list and dictionary...")
    (english_list, english_dictionary) = load_words()
    print("List and dictionary complete!\n")

    search_for = input("Tell me to look up a word: ")
    while search_for:
        niter = 1000
        (list_time, dict_time) = timing_trial(search_for, english_list, english_dictionary, niter)
    
        print("Search time to retrieve the definition of " + search_for + ":")
        print("  list: {} seconds for {} lookups".format(list_time, niter))
        print("  dict: {} seconds for {} lookups".format(dict_time, niter))
        print("")
        search_for = input("Tell me to look up a word: ")

    print("Exiting!")
