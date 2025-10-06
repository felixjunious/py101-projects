import re

str1 = input('Enter first string : ')
str2 = input('Enter second string : ')

words1 = re.findall(r'\w+', str1.lower())
words2 = re.findall(r'\w+', str2.lower())

set1 = set(words1)
set2 = set(words2)

common_words = set1 & set2
unique_words = set1 | set2

jaccard_index = len(unique_words) / len(common_words)

print(f'Jaccard Similarity : {jaccard_index:.2f}')

