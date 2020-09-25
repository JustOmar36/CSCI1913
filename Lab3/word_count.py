# CSCI 1913, Spring 2020, Lab 3
# Student Names:
# Omar Masri!
# Brandon Weinstein!
# MASRI013@umn.edu
# WEINS127@umn.edu


#gets rid of punctuation
def clean_word(text):
    contin = True
    while contin:
        for i in range(len(text)):
            if text[i] in ["!", ",", "?", "."]:
                text = text[:i] + text[i+1:]
                contin = True
                break
            else:
                contin = False  
    return text


#splits text into word list, also calls clean_word function to get rid of punctuation
def my_split(text):
    cleaned_text = clean_word(text)
    text_list = []
    last_index = 0
    for i in range(len(cleaned_text)):
        if cleaned_text[i] == " ":
            text_list.append(cleaned_text[last_index:i])
            last_index = (i+1)
        elif i == len(cleaned_text) - 1:
            text_list.append(cleaned_text[last_index:(i+1)])
    return text_list

# counts number of words and creates dictionary containing word and count. (not using .count())
def count(words):
    word_dict = {}
    for i in words:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    return(word_dict)


# run similarity forumla on words, return similarity value from 0-1
def word_count_similarity(count1, count2):
    s1 = 0
    s2 = 0
    s3 = 0
    for i in count1.values():
        s1 += i*i
    for i in count2.values():
        s2 += i*i
    for i in count1.keys():
            if i in count2:
                s3 += count1[i]*count2[i]
    return (s3/(s1*s2))

# compares known "authors" to an unkown word sample, returns author with closest similarity value using word_count_similarity

def best_guess(known_author_counts, unknown_count):
    similarity = 0
    for i in known_author_counts:
        if word_count_similarity(known_author_counts[i], unknown_count) >= similarity:
            author = i
            similarity = word_count_similarity(known_author_counts[i], unknown_count)
    return author









            







