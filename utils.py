import re
import string
from collections import Counter
n = 5

stopwords = []
f = open('stopwords.txt','r')
for stop in f:
    stopwords.append(stop.strip('/n'))
stopwords = set(stopwords)




def get_statistics(data):
    lines = get_lines(data)
    words = get_words(lines)
    unique_words = list(set(words))
    top_n_words = get_top_n_words(words, n)
    statistics = {'line_count': len(lines), 'word_count': len(words), 'unique_words': len(unique_words),
                  'top_words': top_n_words}
    return statistics

def get_lines(data):
    lines = []
    for para in data:
        para_lines = re.split('[.!?]+', para)
        lines.extend(para_lines)
    cleaned_lines = clean_string(lines)
    return cleaned_lines


def clean_string(lines):
    st = str.maketrans("", "", string.punctuation)
    cleaned_lines = [line.translate(st).lower().strip() for line in lines if line]
    return cleaned_lines


def get_words(lines):
    words = []
    for line in lines:
        words.extend(line.split())
    return words



def get_top_n_words(words, n):
    words = set(words)
    new_words = list(words - stopwords)
    top_n_words = Counter(new_words).most_common(n)
    top_words = []
    for x, y in top_n_words:
        top_words.append(x)
    return top_words


