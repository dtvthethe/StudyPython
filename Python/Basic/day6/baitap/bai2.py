from text_utility import read
from collections import Counter

paragraph = read('data.txt')
paragraphs = paragraph.split()
counte = Counter(paragraphs)
print(len(counte))
print(counte)